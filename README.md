# Toronto Crime Prediction

This project predicts crime types and trends in Toronto using machine learning.

It includes data cleaning, exploratory data analysis, model training, and a streamlit application to make predictions.

---

## Project Overview

- Analyze historical crime data in Toronto
- Build predictive models to classify crime types
- Provide an interface to make real-time predictions

---

## Project Structure

- `Phase_1_1.ipynb`: Data cleaning and exploration
- `explore.py`: Data exploration scripts
- `predict.py`: Prediction script
- `app.py`: Flask web application
- `crime_integrated.csv`: Raw dataset
- `crimeintegrated_cleaned.csv`: Cleaned dataset
- `model_and_encoder.pkl`: Trained model and encoder

---

## Installation

1. Clone the repository:    
   git clone https://github.com/datadrivensarab/crimeprediction.git   
   cd crimeprediction-main  

2. Create and activate a virtual environment:  
   python -m venv venv    
   source venv/bin/activate # On Windows: venv\Scripts\activate  
   
3. Install dependencies:  
   pip install -r requirements.txt
   
---

## Usage

- **Explore Data:**  
  jupyter notebook Phase_1_1.ipynb  
  or  
  python explore.py      

- **Train / Predict:**  
  python predict.py  
  
- **Run Application:**  
  python app.py  

---

## Technologies Used

- Python 3
- Pandas
- scikit-learn
- Flask
- Jupyter Notebook


 





