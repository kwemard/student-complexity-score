"""
This module contains unit tests for the Streamlit Dashboard application.

It covers tests for data loading functionalities, ensuring the correct data structure
and the presence of essential indicators, as well as the proper functioning of utility
functions like CSV conversion.
"""

import unittest
import pandas as pd
import app as app_m
import dashboard_utils as dashboard_m
import config as config_m


class TestDashboard(unittest.TestCase):
    """
    Test suite for validating the functionality of the Streamlit Dashboard.

    This class includes unit tests for verifying data loading from a Google Drive file path,
    ensuring the correct DataFrame structure, and testing the conversion of DataFrame
    to CSV format.
    """

    def test_data_loading(self):
        """Test if data loads correctly"""
        data = app_m.load_data(config_m.GOOGLE_DRIVE_FILE_PATH)
        self.assertIsInstance(data, pd.DataFrame)
        self.assertNotEqual(len(data), 0)
        # Check for the presence of indicators columns
        for column in config_m.INDICATORS:
            self.assertIn(column, data.columns)

    def test_csv_conversion(self):
        """Test the CSV conversion function"""
        data = pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})
        csv_data = dashboard_m.convert_df_to_csv(data)
        self.assertIsInstance(csv_data, bytes)


if __name__ == "__main__":
    unittest.main()
