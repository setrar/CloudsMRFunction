import unittest
# test/test_reducer.py
from Reducer import main as reducer_main

class TestReducer(unittest.TestCase):

    def test_reducer(self):
        input_pair = {"word": "example", "counts": [1, 2, 3, 4]}
        expected_output = {"word": "example", "total_count": 10}
        self.assertEqual(reducer_main(input_pair), expected_output)

if __name__ == "__main__":
    unittest.main()
