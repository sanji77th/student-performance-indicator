# Student Performance Indicator

The Student Performance Indicator project is an end-to-end machine learning project that aims to analyze the impact of various variables on the test scores of students. By considering factors such as gender, ethnicity, lunch, test preparation, and parental level, this project provides insights into student performance.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [Credits](#credits)
- [License](#license)
- [Contact](#contact)

## Installation

To set up the project, follow these steps:

1. Clone the repository from GitHub.
2. Install the required packages and dependencies by executing the package installation script.

   ```bash
   pip install -r requirements.txt

## Usage

The project consists of the following steps:

### Step 1: GitHub Setup and Code Setup

Set up the GitHub repository and configure the code structure. Ensure that the required packages are installed.

### Step 2: Project Structure, Logging, and Exception Handling

Define the project structure and implement logging and exception handling mechanisms to facilitate debugging and error handling.

### Step 3: Project Problem Statement, EDA, and Model Training

Define the problem statement of the project, perform exploratory data analysis (EDA) using Jupyter Notebook, Pandas, and Matplotlib for data visualization. Evaluate various machine learning models, such as KNeighborsRegressor, DecisionTreeRegressor, RandomForestRegressor, AdaBoostRegressor, SVR, LinearRegression, Ridge, Lasso, CatBoostRegressor, and XGBRegressor, to identify the model with the highest accuracy. In this project, Linear Regression is selected as the final model.

### Step 4: Data Ingestion

Implement data ingestion mechanisms to load and preprocess the dataset for model training and evaluation.

### Step 5: Pipeline Development for Data Transformation

Develop pipelines for data transformation to streamline the preprocessing steps and ensure consistent and efficient data handling.

### Step 6: Training and Evaluation of Linear Regression Model

Train the Linear Regression model using the preprocessed dataset and evaluate its performance against the test data.

### Step 7: Hyperparameter Optimization

Perform hyperparameter optimization to fine-tune the Linear Regression model for improved accuracy and performance.

### Step 8: Prediction Pipeline and Web Application

Create a prediction pipeline with Flask to provide a user-friendly web application. The web app allows users to predict student performance based on criteria such as gender, ethnicity, lunch, test preparation, and parental level. The app is built using Flask, HTML, and Bootstrap.

### Step 9: Deployment using AWS Cloud and CI/CD Pipelines

Deploy the project using AWS Elastic Beanstalk, leveraging CI/CD pipelines for continuous integration and deployment. This ensures seamless updates and scalability.

## Features

- Comprehensive analysis of student performance indicators based on various factors
- Implementation of multiple machine learning models for accurate predictions
- User-friendly web application for predicting student performance

## Contributing

Contributions to this project are welcome. If you would like to contribute, please follow the guidelines outlined in the CONTRIBUTING.md file.

## Credits

We would like to acknowledge the following resources and individuals for their contributions to this project:

- Scikit-learn - Machine learning library for Python
- NumPy - Numerical computing library for Python
- Pandas - Data manipulation and analysis library for Python
- Matplotlib - Data visualization library for Python
- Dill - Serialization library for Python objects
- CatBoost - Gradient boosting library for Python
- XGBoost - Gradient boosting library for Python
- Flask - Web framework for Python
- CI/CD Pipelines - Continuous integration and deployment pipelines
- Amazon Web Services (AWS) - Cloud platform for deployment

## License

This project is licensed under the MIT License.

## Contact

For any inquiries or questions, feel free to contact the project maintainers:

- Sanjitha Amarathunga: sanjithaamarathunga.ai@gmail.com

