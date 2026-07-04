# 🏦 Loan Prediction Model

A Machine Learning-powered web application that predicts whether a loan application is likely to be approved based on applicant information. The project uses a **Decision Tree Classifier** and is deployed as a **Flask** web application with an interactive user interface.

---

## 📌 Project Overview

Financial institutions receive thousands of loan applications every day. Evaluating each application manually is time-consuming and prone to errors.

This project automates the loan approval prediction process by using Machine Learning to analyze applicant details and predict whether a loan should be approved.

---

## 🚀 Features

* User-friendly Flask web interface
* Predicts loan approval in real time
* Decision Tree Machine Learning model
* Simple and responsive UI
* Fast and lightweight deployment
* Easy to customize and extend

---

## 🛠️ Technologies Used

* Python
* Flask
* Scikit-learn
* Pandas
* NumPy
* Joblib
* HTML
* CSS

---

## 📂 Project Structure

```
Loan_Prediction_Model/
│
├── model/
│   └── decision_tree.pkl
│
├── templates/
│   └── index.html
│
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Preprocessing
3. Feature Encoding
4. Train-Test Split
5. Model Training (Decision Tree Classifier)
6. Model Evaluation
7. Save Model using Joblib
8. Deploy with Flask

---

## 📥 Input Features

The application accepts the following applicant information:

* Gender
* Marital Status
* Applicant Income
* Co-applicant Income
* Loan Amount
* Loan Amount Term
* Credit History
* Property Area
* Education
* Self Employed Status

---

## 📈 Output

The model predicts one of the following:

* ✅ Loan Approved
* ❌ Loan Not Approved

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/vaibhavbaranwal15/Loan_Prediction_Model.git
```

### Navigate to the project folder

```bash
cd Loan_Prediction_Model
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 📸 Application Preview

Add screenshots of your Flask application here.

Example:

```
Home Page

Prediction Result
```

---

## 📌 Future Improvements

* Deploy on Render or Railway
* Add Random Forest and XGBoost models
* Improve UI with Bootstrap
* Add user authentication
* Upload CSV for batch predictions
* Visualize prediction statistics

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vaibhav Baranwal**

* GitHub: https://github.com/vaibhavbaranwal15
* LinkedIn: Add your LinkedIn profile here if available.

---

⭐ If you found this project useful, don't forget to **Star** the repository!
