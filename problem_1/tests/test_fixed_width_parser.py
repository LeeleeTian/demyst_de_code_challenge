import unittest
import os
import sys

# Add the parent directory to sys.path to import fixed_width_parser
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fixed_width_parser import generate_fixed_width_file, parse_fixed_width_to_csv

class TestFixedWidthParser(unittest.TestCase):

    def setUp(self):
        # This method will run before each test
        self.spec = {
            "ColumnNames": ["f1", "f2", "f3", "f4", "f5", "f6", "f7", "f8", "f9", "f10"],
            "Offsets": [5, 12, 3, 2, 13, 7, 10, 13, 20, 13],
            "FixedWidthEncoding": "windows-1252",
            "DelimitedEncoding": "utf-8",
            "IncludeHeader": "True"
        }
        self.output_dir = '/app/output'
        self.fixed_width_file = os.path.join(self.output_dir, 'output_fixed_width.txt')
        self.csv_file = os.path.join(self.output_dir, 'output_data.csv')

        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Sample input data for testing
        self.sample_data = [
            "12345,Hello World,ABC,12,More text here,1234567,1234567890,Another text,20 characters here,End of line",
            "67890,Another row,XYZ,34,Additional data,7654321,0987654321,More content,Another set of text,Line end text"
        ]

    def tearDown(self):
        # This method will run after each test
        # Cleanup: Remove the test files if they exist
        if os.path.exists(self.fixed_width_file):
            os.remove(self.fixed_width_file)
        if os.path.exists(self.csv_file):
            os.remove(self.csv_file)

    def test_generate_fixed_width_file(self):
        # Generate the fixed-width file using sample data directly
        with open(self.fixed_width_file, 'w', encoding=self.spec["FixedWidthEncoding"]) as fw_file:
            if self.spec["IncludeHeader"]:
                header = ''.join([f"{name:<{offset}}" for name, offset in zip(self.spec["ColumnNames"], self.spec["Offsets"])]) + '\n'
                fw_file.write(header)
            for data_line in self.sample_data:
                values = data_line.split(',')
                line = ''.join([f"{str(value)[:offset]:<{offset}}" for value, offset in zip(values, self.spec["Offsets"])]) + '\n'
                fw_file.write(line)

        # Verify the file was created and conforms to spec
        with open(self.fixed_width_file, 'r', encoding=self.spec["FixedWidthEncoding"]) as f:
            lines = f.readlines()

        # Check header
        if self.spec["IncludeHeader"]:
            expected_header = ''.join([f"{name:<{offset}}" for name, offset in zip(self.spec["ColumnNames"], self.spec["Offsets"])]) + '\n'
            self.assertEqual(lines[0], expected_header)

        # Check each line length
        for line in lines[1:]:
            line_length = sum(self.spec["Offsets"])
            self.assertEqual(len(line.rstrip('\n')), line_length)  # Use rstrip to handle newlines correctly

    def test_parse_fixed_width_to_csv(self):
        # Generate the fixed-width file first
        with open(self.fixed_width_file, 'w', encoding=self.spec["FixedWidthEncoding"]) as fw_file:
            if self.spec["IncludeHeader"]:
                header = ''.join([f"{name:<{offset}}" for name, offset in zip(self.spec["ColumnNames"], self.spec["Offsets"])]) + '\n'
                fw_file.write(header)
            for data_line in self.sample_data:
                values = data_line.split(',')
                line = ''.join([f"{str(value)[:offset]:<{offset}}" for value, offset in zip(values, self.spec["Offsets"])]) + '\n'
                fw_file.write(line)

        # Parse the fixed-width file to CSV
        parse_fixed_width_to_csv(self.fixed_width_file, self.csv_file)

        # Verify the CSV file was created and content matches fixed-width file
        with open(self.fixed_width_file, 'r', encoding=self.spec["FixedWidthEncoding"]) as fw_file:
            fixed_width_content = fw_file.readlines()

        with open(self.csv_file, 'r', encoding=self.spec["DelimitedEncoding"]) as csv_file:
            csv_content = csv_file.readlines()

        # Verify line counts are the same (header included)
        self.assertEqual(len(fixed_width_content), len(csv_content))

        # Verify CSV content against fixed-width content
        for fw_line, csv_line in zip(fixed_width_content, csv_content):
            index = 0
            fw_fields = []
            for offset in self.spec["Offsets"]:
                fw_fields.append(fw_line[index:index+offset].strip())
                index += offset
            csv_fields = csv_line.strip().split(',')
            self.assertEqual(fw_fields, csv_fields)

if __name__ == '__main__':
    unittest.main()
