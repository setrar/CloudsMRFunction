import unittest
from Shuffler.__init__ import main as shuffler_main

class TestShuffler(unittest.TestCase):

    def test_shuffler(self):
        map_results = [
            [("example", 1), ("test", 2)],
            [("example", 3), ("demo", 4)],
        ]
        expected_output = {
            "example": [1, 3],
            "test": [2],
            "demo": [4],
        }
        self.assertEqual(shuffler_main(map_results), expected_output)

if __name__ == "__main__":
    unittest.main()
