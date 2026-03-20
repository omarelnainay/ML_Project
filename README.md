# Machine Learning Final Project (Phase 1)

## 📌 Project Overview

This project is part of the Machine Learning course requirements. The objective is to apply the full machine learning pipeline on two different datasets:

* A **Classification dataset**
* A **Regression dataset**

Each dataset is processed through data exploration, preprocessing, visualization, modeling, and evaluation phases.

---

## 📂 Datasets Used

### 1. Classification Dataset

* **Name:** Titanic Survival Dataset

* **Source:** Kaggle

* **Description:**
  This dataset contains information about passengers aboard the Titanic. The goal is to predict whether a passenger survived or not based on features such as age, gender, class, and fare.

* **Target Variable:** `Survived` (0 = No, 1 = Yes)

---

### 2. Regression Dataset

* **Name:** Housing Prices Dataset

* **Source:** Kaggle

* **Description:**
  This dataset includes various features related to houses, such as area, number of rooms, and location factors. The goal is to predict the price of a house.

* **Target Variable:** `Price`

---

## ⚙️ Project Structure

```
├── classification_dataset.csv
├── regression_dataset.csv
├── classification_model.ipynb
├── regression_model.ipynb
├── README.md
└── report.pdf
```

---

## 🔍 Project Phases

### 1. Data Retrieval

* Datasets were downloaded from Kaggle
* Each dataset was inspected and described
* Columns and their meanings were analyzed

---

### 2. Data Exploration

* Checked dataset structure (shape, data types)
* Identified missing values and duplicates
* Generated summary statistics
* Performed correlation analysis

---

### 3. Data Preprocessing

* Handled missing values (imputation/removal)
* Removed duplicates and outliers
* Encoded categorical variables (e.g., One-Hot Encoding)
* Scaled numerical features
* Applied feature engineering where needed

---

### 4. Data Visualization

* Used:

  * Matplotlib
  * Seaborn
* Created:

  * Histograms
  * Box plots
  * Correlation heatmaps
  * Count plots

---

### 5. Modeling

#### 📊 Classification Models

* Decision Tree Classifier
* AdaBoost Classifier

#### 📈 Regression Models

* Linear Regression
* Decision Tree Regressor
* AdaBoost Regressor

---

### 6. Model Evaluation

#### Classification Metrics:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

#### Regression Metrics:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Google Colab

---

## 🚀 How to Run the Project

1. Open the notebooks using Google Colab or Jupyter Notebook
2. Upload the dataset CSV files
3. Run all cells step-by-step
4. Review outputs and visualizations

---

## 👥 Team Members

* [Member 1 Name]
* [Member 2 Name]
* [Member 3 Name]
* [Member 4 Name]
* [Member 5 Name]
* [Member 6 Name]

---

## 📄 Submission Files

* 2 datasets (CSV format)
* 2 Jupyter notebooks (.ipynb)
* Final report (.pdf or .docx)
* README.md

---

## 💡 Notes

* Proper preprocessing significantly improves model performance
* Feature engineering plays an important role in both datasets
* Model comparison helps in selecting the best-performing algorithm

---

## ✅ Conclusion

This project demonstrates the application of machine learning techniques on both classification and regression problems. It highlights the importance of data preprocessing, model selection, and evaluation in building effective predictive models.

---
