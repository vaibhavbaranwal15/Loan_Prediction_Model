import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Load dataset
df = pd.read_csv(r"C:\Users\lenovo\OneDrive\Desktop\training\loan_prediction\loan_data.csv")

# Features and target
X = df.drop("Approved", axis=1)
y = df["Approved"]

print("Columns:", X.columns.tolist())
print("Number of features:", X.shape[1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = DecisionTreeClassifier(random_state=42, max_depth=4)
model.fit(X_train, y_train)

# Evaluate
accuracy = model.score(X_test, y_test)
print(f"Model Accuracy: {accuracy:.2f}")

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/decision_tree.pkl")

print("Model saved successfully!")