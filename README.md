# 🧠 MLOps: Industry-Ready Machine Learning Pipeline with MLflow

This project demonstrates an **end-to-end MLOps architecture**, designed to mimic how machine learning pipelines are built and managed in real-world production environments. Developed as part of my Master’s in Artificial Intelligence & Robotics, this repository focuses on modular design, reproducibility, experiment tracking, and automation.

---

## 🚀 Project Goals

- Simulate an **industry-standard MLOps pipeline**
- Apply modular development from data to model evaluation
- Use **MLflow** for experiment tracking
- Implement **CI/CD workflows** using GitHub Actions
- Prepare for deployment and scaling (deployment not included due to financial constraints)

---

## 🧱 Project Structure

```bash
MLOps/
├── .github/workflows/       # GitHub Actions workflow
├── artifacts/               # Intermediate data and model files
│   └── [data_ingestion, transformation, evaluation...]
├── config/                  # YAML configuration
│   └── config.yaml
├── mlruns/                  # MLflow tracking data
├── src/
│   └── mlProject/
│       ├── components/      # Core modules: ingestion, transformation, trainer
│       ├── pipeline/        # Stage-wise pipeline execution scripts
│       ├── config/          # Project-level config and schema
│       └── utils/           # Utility functions
├── templates/               # HTML templates for Flask app
├── Dockerfile               # Container setup (optional)
├── app.py                   # Flask web app (prediction UI)
├── params.yaml              # Parameter configuration
├── requirements.txt         # Project dependencies
├── schema.yaml              # Data schema definition
└── README.md


```

## 🔄 Pipeline Overview

Each pipeline stage is modular and traceable:

1. **Data Ingestion**  
   Reads raw data and stores it for processing.

2. **Data Validation**  
   Ensures the input data adheres to the expected schema.

3. **Data Transformation**  
   Handles missing values, encodes features, and scales the data.

4. **Model Training**  
   Trains the ML model and logs metrics using MLflow.

5. **Model Evaluation**  
   Compares predictions and evaluates the model using predefined metrics.

---

## 🛠️ Technologies Used

- **Python** – Core language
- **MLflow** – Experiment tracking
- **PyYAML** – Configuration management
- **Flask** – Simple web app for inference
- **GitHub Actions** – Automating workflows
- **Docker** – Containerization (optional)

---

## ⚙️ Getting Started

### 🔧 Installation

```bash
git clone https://github.com/preetdhanani/MLOps.git
cd MLOps
python -m venv venv
source venv/bin/activate  # or use venv\Scripts\activate on Windows
pip install -r requirements.txt
