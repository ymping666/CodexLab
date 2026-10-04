"""Isolated packaging and preparation tests, without model or scientific execution."""
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

SOURCE = Path(__file__).resolve().parents[1] / 'skills' / 'codexlab'

class StylePickerHelperTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='codexlab-style-test-')
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.skill = self.root / 'skill'
        shutil.copytree(SOURCE, self.skill)
        self.script = self.skill / 'scripts/prepare_role_picker.py'
        self.target = self.root / 'preview.html'

    def run_helper(self, *args):
        return subprocess.run([sys.executable, '-I', str(self.script), '--output', str(self.target), *args], cwd=self.root, capture_output=True, text=True, encoding='utf-8')

    def payload(self, element):
        html = self.target.read_text(encoding='utf-8')
        return json.loads(re.search(r'<script id="'+element+r'" type="application/json">(.*?)</script>', html, re.S)[1])

    def test_isolated_skill_prepares_complete_self_contained_page(self):
        result = self.run_helper()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(self.payload('codexlab-style-catalog'),json.loads((self.skill/'references/catalog.json').read_text(encoding='utf-8')))
        self.assertEqual(self.payload('codexlab-picker-options'),{'selection':None,'ignoreSavedState':False,'language':None})
        self.assertEqual(sorted(p.name for p in self.root.iterdir()),['preview.html','skill'])

    def test_no_overwrite_and_no_implicit_parent_creation(self):
        self.target.write_bytes(b'existing human data')
        result = self.run_helper()
        self.assertEqual(result.returncode,2)
        self.assertEqual(self.target.read_bytes(),b'existing human data')
        self.target = self.root/'missing-parent'/'preview.html'
        self.assertEqual(self.run_helper().returncode,2)
        self.assertFalse(self.target.parent.exists())

    def test_invalid_slots_are_rejected_without_output(self):
        baseline = {'pi':'Aster','literature':'Atlas','method':'Nova','experiment':None,'reviewer':None}
        for changed in ({'pi':None},{'method':'Sage'},{'experiment':['Forge','Pulse']},{'surprise':'Rook'}):
            with self.subTest(changed=changed):
                result = self.run_helper('--selection',json.dumps({**baseline,**changed}))
                self.assertEqual(result.returncode,2,result.stdout)
                self.assertFalse(self.target.exists())

    def test_confirmed_choices_automatically_override_saved_draft(self):
        choice = {'pi':'Quinn','literature':'Flint','method':'Mira','experiment':None,'reviewer':'Trace'}
        result = self.run_helper('--selection',json.dumps(choice))
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(self.payload('codexlab-picker-options'),{'selection':choice,'ignoreSavedState':True,'language':None})

    def test_explicit_language_is_embedded_without_initializing_research(self):
        result = self.run_helper('--language','zh-CN')
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(self.payload('codexlab-picker-options')['language'],'zh-CN')
        self.assertEqual(sorted(p.name for p in self.root.iterdir()),['preview.html','skill'])

    def test_unknown_language_is_rejected_without_output(self):
        self.assertEqual(self.run_helper('--language','unknown').returncode,2)
        self.assertFalse(self.target.exists())

    def test_incomplete_display_translation_is_rejected_without_output(self):
        catalog_file = self.skill/'references/catalog.json'
        catalog = json.loads(catalog_file.read_text(encoding='utf-8'))
        del catalog['categories'][2]['profiles'][0]['translations']['zh-CN']['summary']
        catalog_file.write_text(json.dumps(catalog,ensure_ascii=False),encoding='utf-8')
        self.assertEqual(self.run_helper().returncode,2)
        self.assertFalse(self.target.exists())

    def test_catalog_extends_without_code_changes_and_cannot_close_script(self):
        catalog_file = self.skill/'references/catalog.json'
        catalog = json.loads(catalog_file.read_text(encoding='utf-8'))
        extra = dict(catalog['categories'][1]['profiles'][0],name='Echo',summary='</script><script>window.bad=true</script>')
        catalog['categories'][1]['profiles'].append(extra)
        catalog_file.write_text(json.dumps(catalog,ensure_ascii=False),encoding='utf-8')
        result = self.run_helper()
        self.assertEqual(result.returncode,0,result.stderr)
        self.assertEqual(self.payload('codexlab-style-catalog'),catalog)
        self.assertNotIn('<script>window.bad=true',self.target.read_text(encoding='utf-8'))

    def test_traversal_is_rejected(self):
        self.target = self.root/'child'/'..'/'preview.html'
        self.assertEqual(self.run_helper().returncode,2)
        self.assertFalse((self.root/'preview.html').exists())

    def test_invalid_entry_points_do_not_write_a_preview(self):
        catalog_file = self.skill/'references/catalog.json'
        original = json.loads(catalog_file.read_text(encoding='utf-8'))
        for mutation in ('duplicate', 'cross-role', 'missing-reason'):
            with self.subTest(mutation=mutation):
                catalog = json.loads(json.dumps(original))
                if mutation == 'duplicate':
                    catalog['entry_points'][1]['id'] = catalog['entry_points'][0]['id']
                elif mutation == 'cross-role':
                    catalog['entry_points'][0]['selection']['method'] = 'Sage'
                else:
                    del catalog['entry_points'][0]['reason']
                catalog_file.write_text(json.dumps(catalog,ensure_ascii=False),encoding='utf-8')
                self.assertEqual(self.run_helper().returncode,2)
                self.assertFalse(self.target.exists())

if __name__=='__main__':
    unittest.main()
