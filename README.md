# Linear-Regression-Model

## Project Overview
This repository contains the implementation of a Linear Regression model to predict house prices using the Boston Housing Dataset. The model is built without the use of the built-in functions from Scikit-learn for Linear Regression, instead employing the normal equations method for educational purposes.

## Motivation
The objective of this project is to understand and apply the fundamental concepts of Linear Regression in a real-world dataset. By manually implementing the model, the project explores the underlying mathematics and offers a deeper insight into machine learning model building.

## Dataset
The Boston Housing Dataset consists of 506 samples and 13 features which influence the median value of homes. This project uses this dataset to build a regression model to predict the median value of homes based on these features.

**Features**:
- CRIM: Per capita crime rate by town.
- ZN: Proportion of residential land zoned for lots over 25,000 sq. ft.
- INDUS: Proportion of non-retail business acres per town.
- CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise).
- NOX: Nitric oxide concentration (parts per 10 million).
- RM: Average number of rooms per dwelling.
- AGE: Proportion of owner-occupied units built prior to 1940.
- DIS: Weighted distances to five Boston employment centers.
- RAD: Index of accessibility to radial highways.
- TAX: Full-value property tax rate per $10,000.
- PTRATIO: Pupil-teacher ratio by town.
- B: 1000(Bk - 0.63)², where Bk is the proportion of people of African American descent by town.
- LSTAT: Percentage of lower status of the population.

**Target Variable**:
- MEDV: Median value of owner-occupied homes in $1000’s.

**Note**: Due to privacy and licensing reasons, the dataset is not included in this repository.

## Technologies Used
- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Features
- Implementation of Linear Regression using normal equations.
- Evaluation of the model with metrics like RSE and R².
- Analysis of model performance across different training/test splits.

## Results
The model was evaluated using the RSE (Residual Standard Error) and R² (Coefficient of Determination) metrics. Below are some highlighted results:

- **Test size 10%**:
   - Training RSE: 4.87
   - Test RSE: 3.86
   - Training R²: 0.727
   - Test R²: 0.771

- **Test size 20%**:
   - Training RSE: 4.74
   - Test RSE: 5.05
   - Training R²: 0.743
   - Test R²: 0.659

The detailed results for other test sizes and further insights into the discrepancies between training and testing performances are discussed in the script's output.

## Installation
To set up this project for use or development, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/spymavro/Linear-Regression-Model.git
   cd Linear-Regression-Model

2. **Install the required Python packages**:

- Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/downloads/).
- It's recommended to create a virtual environment to keep dependencies required by different projects separate and to avoid conflicts:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
- Install the required packages:
  ```bash
  pip install pandas numpy matplotlib scikit-learn

3. **Proceed with project setup and usage as required**:
### Explanation:
- **Step 1**: Cloning the repository is straightforward; make sure to replace `spymavro` with your actual GitHub username.
- **Step 2**: This step covers:
  - Checking for Python installation.
  - Setting up a virtual environment, which is optional but recommended.
  - Direct installation of each required Python package using `pip`.
 
## Usage
- Navigate to the cloned directory in your terminal and execute the Linear Regression model script by running:
  ```bash
  python linear_regression.py 

## Contact
For any inquiries or collaboration requests, please reach out via GitHub or email at spyros.mauromatis@gmail.com.



