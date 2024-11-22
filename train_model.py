import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Sample data
data = {
    'wins': [10, 20, 30, 40, 50],
    'losses': [5, 10, 15, 20, 25],
    'outcome': [1, 1, 1, 0, 0]  # 1 for win, 0 for loss
}

df = pd.DataFrame(data)
print("DataFrame created.")

# Features and target
X = df[['wins', 'losses']]
y = df['outcome']
print("Features and target defined.")

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split into training and testing sets.")

# Train the model
model = LogisticRegression()
model.fit(X_train, y_train)
print("Model trained.")

# Save the model
joblib.dump(model, 'model.pkl')
print("Model saved as 'model.pkl'.")