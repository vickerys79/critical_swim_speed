import unittest
import tkinter as tk
from critical_swim_speed import CSSCalculator  # Replace 'your_module_name' with the actual module name


class TestCSSCalculator(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = CSSCalculator(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_create_table(self):
        # Test if the table creation adds the expected number of widgets
        self.assertEqual(len(self.app.table), 1)  # One row should be created initially
        self.assertEqual(len(self.app.table[0]), 4)  # Four columns

    def test_add_row(self):
        initial_rows = len(self.app.table)
        self.app.add_row()
        self.assertEqual(len(self.app.table), initial_rows + 1)  # Check if a new row is added

    def test_parse_time(self):
        time_str = "03:45"
        parsed_time = self.app.parse_time(time_str)
        self.assertEqual(parsed_time.total_seconds(), 3 * 60 + 45)  # Check if time string is parsed correctly

    def test_calculate_css(self):
        # Test CSS calculation with valid input
        valid_input = [("01:30", "00:40"), ("02:15", "01:00")]
        expected_results = ["00:25", "00:38"]
        self.app.add_row()
        for i, (time_400_str, time_200_str) in enumerate(valid_input):
            self.app.table[i][1].insert(0, time_400_str)
            self.app.table[i][2].insert(0, time_200_str)
        self.app.calculate_css()
        for i, expected_result in enumerate(expected_results):
            self.assertEqual(self.app.table[i][3].get(), expected_result)
