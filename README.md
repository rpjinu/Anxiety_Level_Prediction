# Anxiety_Level_Prediction
"This project uses a machine learning model deployed with Streamlit to predict the severity of anxiety attacks based on user inputs like demographics, lifestyle, and health data."

<img src="https://github.com/rpjinu/Anxiety_Level_Prediction/blob/main/project_imag.png">

# Anxiety Attack Severity Prediction Project

## Overview

This project aims to predict the severity of anxiety attacks based on various user input features such as demographics, lifestyle habits, and health metrics. The model is deployed as a web application using Streamlit, allowing users to enter relevant data and receive real-time predictions about the severity of anxiety attacks (on a scale of 1 to 10).

## Table of Contents
1. [Project Description](#project-description)
2. [Data Description](#data-description)
3. [Features](#features)
4. [Model](#model)
5. [Deployment with Streamlit](#deployment-with-streamlit)
6. [How to Run the Project](#how-to-run-the-project)
7. [Installation Instructions](#installation-instructions)
8. [Dependencies](#dependencies)
9. [License](#license)

## Project Description

The project focuses on predicting the severity of anxiety attacks (on a scale of 1 to 10) using a regression model. The web application allows users to input data through an interactive interface built with Streamlit. Once the input is received, the machine learning model processes it and outputs a prediction for the severity of the user's anxiety attack.

The key goal of this project is to provide an easy-to-use tool to help individuals understand their anxiety levels based on specific personal and lifestyle factors.

## Data Description

The dataset used for this project includes 12,000 entries with 20 features, which include demographic information, health metrics, and lifestyle habits. The target column is "Severity of Anxiety Attack (1-10)" which represents the intensity of the anxiety attack. 

### Features:
- **Age**: Age of the individual.
- **Gender**: Gender of the individual (encoded: 0 = Female, 1 = Male).
- **Occupation**: Occupation of the individual (encoded: 0 = Student, 1 = Teacher, etc.).
- **Sleep Hours**: Number of hours of sleep per day.
- **Physical Activity (hrs/week)**: Hours of physical activity per week.
- **Caffeine Intake (mg/day)**: Daily caffeine intake (in mg).
- **Alcohol Consumption (drinks/week)**: Weekly alcohol consumption.
- **Smoking**: Whether the individual smokes or not.
- **Stress Level (1-10)**: Self-reported stress level (on a scale from 1 to 10).
- **Breathing Rate (breaths/min)**: Breathing rate during an anxiety attack.
- **Sweating Level (1-5)**: Sweating level during an anxiety attack.
- **Dizziness**: Whether the individual feels dizzy during an anxiety attack.
- **Therapy Sessions (per month)**: Number of therapy sessions per month.
- **Recent Major Life Event**: Whether the individual has had a recent major life event (e.g., loss, divorce).
- **Diet Quality (1-10)**: Quality of the individual’s diet (on a scale from 1 to 10).

## Model

The machine learning model is trained using the dataset with the goal of predicting the severity of anxiety attacks (a continuous numerical value from 1 to 10). 

### Model Evaluation:
The model is evaluated using Mean Squared Error (MSE) and R² score to determine the accuracy and goodness of fit. Various models were tested, including:
- **Linear Regression**
- **Random Forest**
- **Gradient Boosting**

The model with the best performance (lowest MSE and highest R²) was selected for deployment.

## Deployment with Streamlit

The model is deployed as a web application using Streamlit. The application allows users to input their personal details and lifestyle factors, which are then passed through the trained machine learning model to predict the severity of an anxiety attack.

The Streamlit interface is simple and interactive, where users can provide inputs via sliders and text inputs. Once the input is submitted, the model predicts the severity of the anxiety attack, which is displayed on the webpage.

### Key Features of the Streamlit Application:
- Input fields for demographic and lifestyle data.
- Real-time prediction of anxiety attack severity.
- User-friendly interface with bar sliders for 1-10 scale input values.
- Immediate feedback to the user on their anxiety attack severity.

## How to Run the Project

To run this project, you will need Python installed on your machine. Follow these steps:

1. **Clone the repository** (or download the project files).
   
   ```bash
   git clone <repository-link>
