# MLOps: Industry-Ready Machine Learning Pipeline with MLflow

This project demonstrates an **end-to-end MLOps architecture**, designed to mimic how machine learning pipelines are built and managed in real-world production environments. Developed as part of my Master’s in Artificial Intelligence & Robotics, this repository focuses on modular design, reproducibility, experiment tracking, and automation.

---

## Project Goals

- Simulate an **industry-standard MLOps pipeline**
- Apply modular development from data ingestion to model evaluation 
- Use **MLflow** for experiment tracking
- Implement **CI/CD workflows** using GitHub Actions
- Prepare for deployment and scaling

---


## Project Structure

```bash
MLOps/
├── .github/workflows/       # GitHub Actions workflow with CI/CD 
├── config/                  # YAML configuration
│   └── config.yaml
├── logs
├── mlruns                   # MLflow tracking data
├── research                 # pre configure all the steps in notebook
├── src/
│   └── mlProject/
│       ├── components/      # Core modules: ingestion, transformation, trainer
│       ├── pipeline/        # Stage-wise pipeline execution scripts
│       ├── config/          # Project-level config and schema
├       ├── constants        # Define all the constant values
├       ├── entity/          # Define all the custom dataclasses
│       └── utils/           # Utility functions
├── templates/               # HTML templates for Flask app
├── static                   # Defines all the static files(e.g, css)
├── Dockerfile               # Container setup (optional)
├── main.py                  # Desine and Define whole process of pipeline
├── app.py                   # Flask web app (prediction UI)
├── params.yaml              # Parameter configuration
├── requirements.txt         # Project dependencies
├── schema.yaml              # Data schema definition
├── template.py              # Define folder structure for automate the manual process
└── README.md


```

## Pipeline Overview

Each pipeline stage is modular and traceable:

1. **Data Ingestion**  
   Reads raw data and stores it for processing.

2. **Data Validation**  
   Ensures the input data adheres to the expected schema.

3. **Data Transformation**  
   Handles missing values, encodes features, and scales and divide in train and test data.

4. **Model Training**  
   Trains the ML model and logs metrics using MLflow.

5. **Model Evaluation**  
   Compares predictions and evaluates the model using predefined metrics.

---

## Technologies Used

- **Python** – Core language
- **MLflow** – Experiment tracking
- **PyYAML** – Configuration management
- **Flask** – Simple web app for inference
- **GitHub Actions** – Automating workflows
- **Docker** – Containerization 

---

## Analyze the parameters in dagshub(MLFlow)
use this like for getting access thought its already in project
    https://dagshub.com/preetdhanani/MLOps.mlflow

## Getting Started

### Installation

```bash
git clone https://github.com/preetdhanani/MLOps.git
cd MLOps
python -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Run the Flask Web Interface

This project includes a simple **Flask-based interface** to manually trigger the model training process via a web browser.

### Step 1: Start the Flask App

Run the following command in your terminal:

```bash
python app.py
```

This will start the server at:

```
http://localhost:8080
```

### Step 2: Trigger Model Training from the Browser

To start model training:

1. Open your browser

2. Go to:
    http://localhost:8080/train

This will:

    Automatically run the training pipeline (python main.py)

    Log the training run in MLflow

    Return a success or error message in the browser

### Step 3: Prediction

After training come back to main page and start entering your values then press the button to see the result

