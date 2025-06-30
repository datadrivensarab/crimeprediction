# Toronto Crime Prediction

This project predicts crime types and trends in Toronto using machine learning, with an interactive Streamlit app for visualization and prediction.

It includes data cleaning, exploratory data analysis, model training, and a streamlit application to make predictions.

---

## 📂 Project Overview

- Analyze historical crime data in Toronto
- Build predictive models to classify crime types
- Provide an Streamlit interface to make real-time predictions

---

## 🗂️  Project Structure

- `Phase_1_1.ipynb`: Data cleaning and exploration
- `explore.py`: Data exploration scripts
- `predict.py`: Prediction script
- `app.py`: Streamlit app
- `crime_integrated.csv`: Raw dataset
- `crimeintegrated_cleaned.csv`: Cleaned dataset
- `model_and_encoder.pkl`: Trained model and encoder

---

## ⚙️ Installation

1. Clone the repository:    
    ```bash
   git clone https://github.com/datadrivensarab/crimeprediction.git
   cd crimeprediction-main
   ```

3. Create and activate a virtual environment:  
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
   
4. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
   
---

## 🚀 Usage

- **Explore Data:**
  ```bash
  jupyter notebook Phase_1_1.ipynb
  ```
  or
  ```bash
  python explore.py
  ```    

- **Train / Predict:**  
  ```bash
  python predict.py
  ``` 
  
- **Run Streamlit App:**  
  ```bash
  streamlit run app.py
  ```
  The app will open automatically in your default browser.  

---

## 🧠 Technologies Used

- Python 3
- Pandas
- scikit-learn
- Flask
- Jupyter Notebook

## 📈 Results & Next Steps

- ✅ Data cleaning completed
- ✅ Model training completed
- ✅ Streamlit app implemented
- 🔜 Next steps: improve model accuracy and enrich visualizations


 





