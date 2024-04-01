"""
This module provides various utilities for analyzing student performance. 

It includes functions to calculate complexity scores based on various indicators, 
create scatter plots for visual analysis, extract names of students based on certain 
criteria, and convert DataFrames to CSV format. These utilities are designed to support
data-driven insights into student performance and needs.
"""

import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import config as config_m


# Calcul complexity score
def complexity_score(data, weights):
    """
    Calculate the complexity score for a dataset based on specified indicators and weights.

    This function computes a 'complexity score' for each entry in the dataset. It first
    introduces an 'illness' indicator derived from the 'health' column and 'inv_studytime'
    indicator derived from the 'studytime' column. It then normalizes
    a set of indicators, which include 'absences', 'illness', 'Dalc' (Daily alcohol consumption),
    'Walc' (Weekly alcohol consumption), 'inv_studytime', and 'failures'. The normalization is
    followed by calculating the complexity score as a weighted sum of these indicators.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing the dataset with required columns.
    - weights (array-like): A set of weights for the respective indicators.

    Returns:
    - DataFrame: The input DataFrame with an additional column 'complexity_score'
                  representing the computed score for each entry.
    """
    # Illness indicator
    data["illness"] = 6 - data["health"]
    # inverse study : Adjust the study time variable so that a lower amount
    # of study time corresponds to a higher value. This reflects the increased
    # need for support among students who spend less time studying
    data["inv_studytime"] = 5 - data["studytime"]

    indicators = config_m.INDICATORS

    # Replace missing values with the median of each column
    for column in indicators:
        median_value = data[column].median()
        data[column].fillna(median_value, inplace=True)
    # Normalize indicators
    scaler = MinMaxScaler()
    data_normalized = scaler.fit_transform(data[indicators])

    # Compute complexity score
    data["complexity_score"] = data_normalized.dot(weights)

    return data


# create scater plot
def create_scatter_plot(data, x_col, y_col):
    """
    Creates and returns a scatter plot with given data and specified columns.

    This function generates a scatter plot for visualizing the relationship
    between two variables in a dataset. The x-axis of the plot corresponds to
    the values in the column named 'x_col', and the y-axis corresponds to
    the values in the column named 'y_col'. The plot is sized at 10x6 inches
    and uses a transparency (alpha) value of 0.6 for the scatter points.

    Parameters:
    - data (DataFrame): A pandas DataFrame containing the data to plot.
    - x_col (str): The name of the column in 'data' to be used for the x-axis.
    - y_col (str): The name of the column in 'data' to be used for the y-axis.

    Returns:
    - matplotlib.pyplot: The matplotlib pyplot object with the scatter plot.
    """
    plt.figure(figsize=(10, 6))
    plt.scatter(data[x_col], data[y_col], alpha=0.6)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f"Relationship between {x_col} and {y_col}")

    return plt


# extract student names
def extract_student_names(data, final_grade_threshold, complexity_score_threshold):
    """
    Extract names of students whose final grade is below the final_grade_threshold
    and whose complexity score is below the complexity_score_threshold.

    Parameters:
    data (DataFrame): The dataset containing student information.
    final_grade_threshold (float): The threshold for the final grade.
    complexity_score_threshold (float): The threshold for the complexity score.

    Returns:
    DataFrame: A DataFrame containing the students meeting the criteria.
    """
    # Filter the DataFrame based on the given thresholds
    filtered_students = data[
        (data["FinalGrade"] <= final_grade_threshold)
        & (data["complexity_score"] <= complexity_score_threshold)
    ]

    return filtered_students


# Convert to CSV
def convert_df_to_csv(df):
    """Create a csv file from dataframe"""
    return df.to_csv(index=False).encode("utf-8")
