"""This module contains  functions for the dashboard application.
"""
# app.py
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

import config as config_m
import dashboard_utils as dashboard_m

# load data
@st.cache_data
def load_data(path_to_file):
    """
    Load data from a Google Drive URL and calculate the complexity score.

    This function takes a path to a CSV file hosted on Google Drive, converts it
    to a direct download link, loads the data into a pandas DataFrame, and then
    applies a complexity score calculation to the DataFrame.

    Parameters:
    path_to_file (str): The URL path to the CSV file on Google Drive.

    Returns:
    DataFrame: A pandas DataFrame containing the loaded data with an additional
    column for the complexity score calculated based on predefined weights.
    """
    google_drive_url = path_to_file
    csv_url = f'https://drive.google.com/uc?id={google_drive_url.split("/")[-2]}'
    raw_data = pd.read_csv(csv_url)
    df = dashboard_m.complexity_score(
        raw_data, weights=config_m.WEIGHTS
    )
    return df


# data path
GOOGLE_DRIVE_FILE_PATH = config_m.GOOGLE_DRIVE_FILE_PATH
data = load_data(GOOGLE_DRIVE_FILE_PATH)


# Streamlit app
def main():
    """
    Main function to run the Streamlit app for the Student Performance Dashboard.

    This function sets up the dashboard title, user input controls in the sidebar for 
    threshold selection, and displays tabs for different views - the main dashboard with
    a scatter plot and a statistics tab. 

    In the main dashboard, it identifies students falling below the set thresholds and
    visualizes them using a scatter plot. It also allows downloading a CSV file of the
    filtered data. The 'Statistics' tab provides options for custom scatter plot visualizations.

    The scatter plot contrasts students who need support (below threshold) against others, 
    helping to prioritize interventions based on the final grade and complexity score. 
    """
    st.title("Student Performance Dashboard")

    # User input for thresholds in the sidebar
    st.sidebar.title("Select the thresholds")
    final_grade_threshold = st.sidebar.slider(
        "Final Grade Threshold", min_value=0, max_value=20, value=10
    )
    complexity_score_threshold = st.sidebar.slider(
        "Complexity Score Threshold", min_value=0.0, max_value=1.0, value=0.5
    )

    # Identifying students below thresholds
    below_threshold_students = data[
        (data["FinalGrade"] < final_grade_threshold)
        & (data["complexity_score"] < complexity_score_threshold)
    ]

    tab1, tab2 = st.tabs(["Student Performance Dashboard", "Statistics"])

    with tab1:
        # Scatter plot and DataFrame
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.scatter(
            below_threshold_students["FinalGrade"],
            below_threshold_students["complexity_score"],
            color="red",
            alpha=0.5,
        )
        other_students = data[~data.index.isin(below_threshold_students.index)]
        ax.scatter(
            other_students["FinalGrade"],
            other_students["complexity_score"],
            color="blue",
            alpha=0.5,
        )
        ax.axhline(y=complexity_score_threshold, color="r", linestyle="-")
        ax.axvline(x=final_grade_threshold, color="r", linestyle="-")
        ax.set_xlabel("Final Grade")
        ax.set_ylabel("Complexity Score")
        ax.set_title("Final Grade vs Complexity Score")
        ax.legend(["student to support", "other student"], loc="upper left", ncols=2)
        st.pyplot(fig)

        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("Students to prioritize for support:")
            st.dataframe(below_threshold_students)
        # Convert DataFrame to CSV
        with col2:
            csv = dashboard_m.convert_df_to_csv(below_threshold_students)
            st.download_button(
                label="Download data as CSV",
                data=csv,
                file_name="students_below_thresholds.csv",
                mime="text/csv",
            )
    with tab2:
        # Sélection des colonnes pour l'axe X et l'axe Y
        x_axis = st.selectbox(
            "Choose X-axis:", data.columns, index=list(data.columns).index("FinalGrade")
        )
        y_axis = st.selectbox(
            "Choise Y-axis:",
            data.columns,
            index=list(data.columns).index("complexity_score"),
        )

        # Création et affichage du graphique
        fig = dashboard_m.create_scatter_plot(data, x_axis, y_axis)
        st.pyplot(fig)


if __name__ == "__main__":
    main()
