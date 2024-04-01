"""
Configuration for Student Performance Dashboard.

This module defines several constants used across the dashboard application. It includes
the Google Drive file path for data source, the weights assigned to various performance
indicators, and a list of these indicators.

Constants:
- GOOGLE_DRIVE_FILE_PATH: URL to the Google Drive file containing student data.
- WEIGHTS: Relative importance weights for each performance indicator.
- INDICATORS: Specific performance indicators considered for analysis.
"""
GOOGLE_DRIVE_FILE_PATH = (
    "https://drive.google.com/file/d/1w_47MwSWwvJUW_2e7HdaFQwxyL036alY/view"
)
WEIGHTS = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
INDICATORS = ["absences", "illness", "Dalc", "Walc", "inv_studytime", "failures"]
