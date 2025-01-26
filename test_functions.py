import unittest
from Reducer.__init__ import main as reducer_main
from Shuffler.__init__ import main as shuffler_main

class TestFunctions(unittest.TestCase):

    def test_reducer(self):
        input_pair = {"word": "example", "counts": [1, 2, 3, 4]}
        expected_output = {"word": "example", "total_count": 10}
        self.assertEqual(reducer_main(input_pair), expected_output)

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
