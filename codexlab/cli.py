"""Dependency-free command line helpers; native agents run in Codex itself."""

from __future__ import annotations

import argparse
import html
import json
import shutil
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

from . import __version__
from .workspace import STAGES, WorkspaceError, artifact_path, check_gate, create_workspace, load_workspace, workspace_status


def doctor() -> dict:
    binary = shutil.which("codex")
    version = None
    error = None
    if binary:
        try:
            process = subprocess.run([binary, "--version"], capture_output=True, text=True, timeout=5, check=False)
            if process.returncode == 0:
                version = process.stdout.strip() or process.stderr.strip()
            else:
                error = f"codex --version exited with code {process.returncode}"
        except (OSError, subprocess.TimeoutExpired) as exc:
            error = str(exc)
    python_ok = sys.version_info >= (3, 11)
    return {"python": sys.version.split()[0], "python_ok": python_ok, "codex_path": binary, "codex_version": version, "codex_error": error, "ready": python_ok and bool(binary) and bool(version), "note": "Only checks executable availability. No credentials are read; login, plan availability, and agent execution must be checked in Codex."}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="codexlab", description="Local research workspaces for Codex's native multi-agent workflow.")
    parser.add_argument("--version", action="version", version=f"CodexLab {__version__}")
    commands = parser.add_subparsers(dest="command", required=True)
    init = commands.add_parser("init", help="Create a new research workspace; target must not exist")
    init.add_argument("target")
    init.add_argument("--topic", required=True)
    demo = commands.add_parser("demo", help="Create an explicitly synthetic workflow example")
    demo.add_argument("target")
    health = commands.add_parser("doctor", help="Check Python and the local Codex binary")
    health.add_argument("--json", action="store_true")
    for command in ("status", "prompt", "serve"):
        sub = commands.add_parser(command, help={"status": "Inspect artifacts and structural gates", "prompt": "Print the PI kickoff prompt for Codex", "serve": "Show a local read-only research dashboard"}[command])
        sub.add_argument("workspace", nargs="?", default=".")
        if command == "status":
            sub.add_argument("--json", action="store_true")
        if command == "serve":
            sub.add_argument("--port", type=int, default=8765)
    gate = commands.add_parser("gate", help="Check required artifacts and evidence for one stage")
    gate.add_argument("workspace", nargs="?", default=".")
    gate.add_argument("stage", choices=list(STAGES))
    gate.add_argument("--json", action="store_true")
    return parser


def _dump(value: dict) -> None:
    print(json.dumps(value, ensure_ascii=False, indent=2))


def _render_dashboard(status: dict) -> str:
    name = html.escape(str(status["name"]))
    topic = html.escape(status["topic"])
    rows = []
    for gate in status["gates"]:
        label = "READY" if gate["passed"] else "PENDING"
        issues = "".join(f"<li><code>{html.escape(path)}</code>: {html.escape('; '.join(messages))}</li>" for path, messages in gate["issues"].items())
        artifacts = " · ".join(html.escape(path) for path in gate["required_artifacts"])
        rows.append(f'<article><div class="stage">{html.escape(gate["stage"].upper())}<span>{label}</span></div><p>{artifacts}</p><ul>{issues}</ul></article>')
    banner = '<div class="demo">SYNTHETIC DEMO · invented fixtures, not empirical research</div>' if status["synthetic_demo"] else ""
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta http-equiv="refresh" content="15"><title>CodexLab · {name}</title><style>
    *{{box-sizing:border-box}}body{{background:#0b1020;color:#e8edf6;font:15px system-ui,sans-serif;margin:0}}main{{max-width:1100px;padding:55px 28px;margin:auto}}.eyebrow{{color:#7c9fff;letter-spacing:.2em;font-size:12px}}h1{{font-size:44px;line-height:1.1;margin:18px 0}}.subtitle{{color:#9daec9;max-width:800px;line-height:1.65}}.roles{{display:flex;flex-wrap:wrap;gap:9px;margin:28px 0}}.roles span{{border:1px solid #334264;border-radius:30px;padding:9px 15px;color:#b9caf0}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:14px}}article{{border:1px solid #293653;background:#131c30;padding:22px;border-radius:15px}}.stage{{color:#91b1ff;font-weight:700;display:flex;justify-content:space-between;gap:10px}}.stage span{{color:#d5b978;font-size:11px;border:1px solid #695f3c;padding:4px 8px;border-radius:6px}}article p{{font-size:12px;color:#8699bb;overflow-wrap:anywhere;line-height:1.6}}li{{font-size:13px;color:#b3c0d9;line-height:1.6;margin-bottom:7px}}ul{{padding-left:17px}}code{{font-size:11px}}.demo{{background:#4a3520;color:#ffd093;border:1px solid #85613b;padding:14px;border-radius:9px;margin:24px 0}}footer{{font-size:12px;color:#7e8fad;line-height:1.7;margin-top:28px}}a{{color:#91b1ff}}
    </style></head><body><main><div class="eyebrow">CODEXLAB / NATIVE RESEARCH WORKSPACE</div><h1>{name}</h1><p class="subtitle">{topic}</p>{banner}<div class="roles"><span>PI / Leader</span><span>Literature Scout</span><span>Method Designer</span><span>Experiment Engineer</span><span>Independent Reviewer</span></div><section class="grid">{''.join(rows)}</section><footer>Local read-only artifact dashboard · refreshes every 15 seconds · <a href="/api/status">JSON status</a><br>Structural checks do not verify scientific truth, live agent activity, or publication readiness. Run the kickoff prompt in Codex to coordinate native agents.</footer></main></body></html>"""


def _serve(root: Path, manifest: dict, port: int) -> None:
    if not 0 <= port <= 65535:
        raise WorkspaceError("Port must be between 0 and 65535.")

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            if self.path not in ("/", "/api/status"):
                self.send_error(404)
                return
            try:
                current_root, current_manifest = load_workspace(root)
                status = workspace_status(current_root, current_manifest)
            except WorkspaceError as error:
                self.send_error(500, str(error))
                return
            body = (json.dumps(status, ensure_ascii=False) if self.path == "/api/status" else _render_dashboard(status)).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8" if self.path == "/api/status" else "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'none'; style-src 'unsafe-inline'; base-uri 'none'; frame-ancestors 'none'")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args) -> None:
            pass

    with ThreadingHTTPServer(("127.0.0.1", port), Handler) as server:
        print(f"CodexLab read-only dashboard: http://127.0.0.1:{server.server_port}", flush=True)
        print("Press Ctrl+C to stop. This view reads artifacts; it does not run agents.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command in ("init", "demo"):
            topic = args.topic if args.command == "init" else "Confidence-guided retrieval for scientific question answering (synthetic demo)"
            root = create_workspace(args.target, topic, demo=args.command == "demo")
            print(f"Created {'synthetic demo' if args.command == 'demo' else 'research workspace'}: {root}")
            print(f'Next: codexlab prompt "{root}"')
            return 0
        if args.command == "doctor":
            result = doctor()
            if args.json:
                _dump(result)
            else:
                print(f"Python {result['python']}: {'OK' if result['python_ok'] else 'requires >=3.11'}")
                print(f"Codex: {result['codex_version'] or 'not available'}")
                if result["codex_error"]:
                    print(result["codex_error"])
                print(result["note"])
            return 0 if result["ready"] else 1
        root, manifest = load_workspace(args.workspace)
        if args.command == "prompt":
            kickoff = artifact_path(root, "research/kickoff.md")
            if not kickoff.is_file():
                raise WorkspaceError(f"Kickoff prompt missing: {kickoff}")
            print(kickoff.read_text(encoding="utf-8"))
        elif args.command == "serve":
            _serve(root, manifest, args.port)
        elif args.command == "status":
            status = workspace_status(root, manifest)
            if args.json:
                _dump(status)
            else:
                print(f"CodexLab: {status['name']}\nTopic: {status['topic']}\nWorkspace: {root}")
                if status["synthetic_demo"]:
                    print("SYNTHETIC DEMO — invented artifacts; not research evidence")
                for gate in status["gates"]:
                    print(f"  {gate['stage']}: {'ready' if gate['passed'] else 'pending'}")
                print("Run 'codexlab gate WORKSPACE STAGE' for artifact-level details.")
        elif args.command == "gate":
            gate = check_gate(root, manifest, args.stage)
            if args.json:
                _dump(gate)
            else:
                print(f"{args.stage}: {'PASS' if gate['passed'] else 'BLOCKED'}")
                for path, issues in gate["issues"].items():
                    print(f"  {path}: {'; '.join(issues)}")
                print(gate["note"])
            return 0 if gate["passed"] else 1
        return 0
    except (WorkspaceError, OSError, UnicodeError) as error:
        print(f"codexlab: {error}", file=sys.stderr)
        return 2
