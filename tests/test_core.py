import unittest

from releasekit import is_valid, next_version


class ReleaseKitTests(unittest.TestCase):
    def test_valid(self):
        self.assertTrue(is_valid("1.2.3"))
        self.assertFalse(is_valid("1.2"))

    def test_increment(self):
        self.assertEqual(next_version("1.2.3", "patch"), "1.2.4")
        self.assertEqual(next_version("1.2.3", "minor"), "1.3.0")
        self.assertEqual(next_version("1.2.3", "major"), "2.0.0")


if __name__ == "__main__":
    unittest.main()
