# Student Performance Predictor (ML Project)

An intelligent Machine Learning-based web application that predicts student academic performance based on various input features. This project demonstrates end-to-end ML pipeline development, deployment, and frontend integration.

---

## Overview

The **Student Performance Predictor** is a Machine Learning-based web application that predicts student math performance using features such as reading and writing scores, demographic background, parental education, lunch type, and test preparation status. It integrates a backend ML model via API to deliver real-time predictions and includes a fallback estimation mechanism for reliability.

---

## Features

- Predict student performance instantly  
- ML-powered insights  
- Fast API response  
- Clean and responsive UI  
- Light/Dark theme support  
- Fully integrated frontend + backend  
- Deployment-ready (Render + Vercel)

---

## Machine Learning Workflow

1. Data Collection  
2. Data Preprocessing  
3. Feature Engineering  
4. Model Training  
5. Model Evaluation  
6. Prediction Pipeline  

---

## Tech Stack

### Frontend
- React.js / Vite  
- Tailwind CSS  
- Axios  

### Backend
- Python  
- Flask / FastAPI  

### Machine Learning
- Scikit-learn  
- Pandas  
- NumPy  

---
## Project Structure

```
Student_Predictor_ML/
│
├── artifacts/
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── test.csv
│   └── train.csv
│
├── notebook/
│   ├── catboost_info/
│   ├── data/
│   │   └── StudentsPerformance.csv
│   ├── eda_student_performance.ipynb
│   └── model_training.ipynb
│
├── src/
│   ├── components/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   │
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   │
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
│
├── templates/
│   └── home.html
│
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
├── runtime.txt
└── setup.py
```


---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/AYUSH4951/Student_Predictor_ML.git
cd Student_Predictor_ML
```
## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt
python app.py
```

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

## API Endpoint

POST /predict

---

## Sample Input

```json
{
  "gender": "female",
  "race_ethnicity": "group B",
  "parental_level_of_education": "bachelor's degree",
  "lunch": "standard",
  "test_preparation_course": "completed",
  "reading_score": 72,
  "writing_score": 74
}
```

---

## Response

```json
{
  "prediction": 75.34
}
```

## Deployment

- Frontend: Deployed on Vercel  
- Backend: Deployed on Render  

For the frontend source code, visit:  
https://github.com/AYUSH4951/student-predictor-frontend

---

## Contributions, suggestions, and improvements are always welcome.
