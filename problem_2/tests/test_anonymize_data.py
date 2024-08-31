import unittest
import os
import csv
import re
import glob
from generate_csv import generate_csv
from anonymize_data import anonymize_data

class TestAnonymizeData(unittest.TestCase):

    def setUp(self):
        self.input_file = "/app/output/test_input.csv"
        self.output_dir = "/app/output/test_output"
        self.output_file = "/app/output/test_output.csv"
        generate_csv(0.001, self.input_file)  # Approx 1MB file for testing
    
    def tearDown(self):
        # Cleanup: Remove the test input and output files if they exist
        if os.path.exists(self.input_file):
            os.remove(self.input_file)
        if os.path.exists(self.output_file):
            os.remove(self.output_file)
        if os.path.exists(self.output_dir):
            for file in glob.glob(f"{self.output_dir}/*"):
                os.remove(file)
            os.rmdir(self.output_dir)
    
    def test_anonymize_data(self):
        anonymize_data(self.input_file, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))

        with open(self.output_file, 'r') as f:
            reader = csv.reader(f)
            rows = list(reader)
        # Check that each row has exactly four fields
        self.assertTrue(all(len(row) == 4 for row in rows[1:]))

        # Check that names and addresses have been anonymized
        for row in rows[1:]:
            first_name, last_name, address, _ = row
            self.assertEqual(first_name.strip(), "JOHN")
            self.assertEqual(last_name.strip(), "DOE")
            self.assertEqual(address.strip(), "123 Main Street, City, State")

if __name__ == "__main__":
    unittest.main()
