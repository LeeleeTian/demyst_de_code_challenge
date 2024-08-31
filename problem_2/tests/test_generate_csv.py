import unittest
import os
import csv
from generate_csv import generate_csv

class TestGenerateCSV(unittest.TestCase):

    def setUp(self):
        self.output_file = "/app/output/test_generate.csv"
    
    def tearDown(self):
        # Cleanup: Remove the test output file if it exists
        if os.path.exists(self.output_file):
            os.remove(self.output_file)

    def test_generate_csv(self):
        generate_csv(0.001, self.output_file)  # Approx 1MB file for testing
        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
        # Check that each row has exactly four fields
        self.assertTrue(all(len(row) == 4 for row in rows[1:]))

if __name__ == "__main__":
    unittest.main()
