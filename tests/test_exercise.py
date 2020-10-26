import os.path
import unittest

donefile = os.path.join(os.path.dirname(__file__), "..", "DONE")

class TestSolution(unittest.TestCase):
    def test_donefile_exists(self):
        self.assertTrue(os.path.exists(donefile), "File marking exercise is complete does not exist")

if __name__ == "__main__":
    unittest.main()
