import unittest
from packer import Packer
from packer import Installer

class TestPacker(unittest.TestCase):
    test_template = './tests/docker.pkr.hcl'
    packer = Packer(template=test_template)

    @classmethod
    def setUpClass(self):
        self.packer.init('tests')

    @unittest.skip("Already used for setup")
    def test_init(self):
      self.packer.init('tests')
      pass

    def test_build(self):
      build_output = self.packer.build(parallel=False, debug=True, force=False)
      build_success = build_output.find("artifacts of successful builds")
      self.assertGreater(build_success, 0)

    def test_fix(self):
      self.assertEqual("TODO", "FIXME")

    def test_inspect(self):
      self.assertEqual("TODO", "FIXME")

    def test_push(self):
      self.assertEqual("TODO", "FIXME")

    def test_validate(self):
      self.assertEqual("TODO", "FIXME")

    def test_version(self):
      self.assertEqual("TODO", "FIXME")

    def test_add_opt(self):
      self.assertEqual("TODO", "FIXME")

    def test_validate_argtype(self):
      self.assertEqual("TODO", "FIXME")

    def test_append_base_arguments(self):
      self.assertEqual("TODO", "FIXME")

    def test_join_comma(self):
      self.assertEqual("TODO", "FIXME")

    def test_parse_inspection_output(self):
      self.assertEqual("TODO", "FIXME")

class TestInstaller(unittest.TestCase):
    def test_install(self):
      self.assertEqual("TODO", "FIXME")
    def test_verify_packer_installed(self):
      self.assertEqual("TODO", "FIXME")

if __name__ == "__main__":
    unittest.main()

