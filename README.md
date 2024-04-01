# Student Performance Dashboard

## Introduction
The Student Performance Dashboard is an interactive tool designed to assist educators in understanding and analyzing student academic performance. It visualizes various indicators like attendance, health factors, and study habits to prioritize student support effectively.


## Features
- Interactive data visualization through scatter plots.
- Customizable thresholds for performance indicators.
- Data filtering based on user-defined criteria.
- Export functionality for filtered data sets.

## Running Tests

To ensure the functionality and reliability of the Student Performance Dashboard, we have included a suite of unit tests. Follow these steps to run the tests:

1. Navigate to the project's root directory in your terminal or command prompt.

2. Run the tests using the following command:

python -m pytest test_dashboard.py -vv 

3. Review the output in the terminal to check for any failed tests and their error messages.


## Installation
To set up the Student Performance Dashboard, follow these steps:

1. Navigate to the directory containing your App.py

2. Install required dependencies:

pip install -r requirements.txt

2. Run the application:

streamlit run app.py

## Docker Setup

If you prefer to run the application in a Docker container, follow these steps:

### Building the Docker Image
1. Navigate to the directory containing your Dockerfile.
2. Build the Docker image using the following command:

docker build -t student-performance-dashboard .


### Running the Docker Container
1. Once the image is built, you can run the container with:

docker run -p 8501:8501 student-performance-dashboard

This command maps port 8501 of the Docker container to port 8501 on your host machine.

2. Open your web browser and go to `http://localhost:8501` to access the dashboard.


## Usage
Navigate through the dashboard using the sidebar to adjust performance thresholds and visualize different student data subsets. Use the tabs to switch between various data views and download filtered datasets as needed.

## Configuration
The dashboard relies on the following configuration settings, defined in `config.py`:
- `GOOGLE_DRIVE_FILE_PATH`: Path to the dataset hosted on Google Drive.
- `WEIGHTS`: Weights assigned to the various performance indicators.
- `INDICATORS`: List of indicators used in performance analysis.


## Contact
For support or queries, please contact us at [marius.kwemou@gmail.com].

