import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# ----------------------------- Load and Train -----------------------------
print("🔄 Loading dataset and training model...")

# Load dataset
df = pd.read_csv('dataset.csv')

# Encode topic as category and numeric code
df['topic'] = df['topic'].astype('category')
df['topic_code'] = df['topic'].cat.codes

# Input features (excluding 'word_count' for better generalization)
X = df[['topic_code', 'study_times', 'total_time_mins', 'gap_days',
        'confidence', 'quiz_score', 'days_since_last']]
y = df['burn_rate_days']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# Save model to file (for Flask or other UI)
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)

# Save topic mapping for UI use
topic_mapping = dict(enumerate(df['topic'].cat.categories))

# ----------------------------- User Input -----------------------------
print("\n📘 MEMORY BURN RATE PREDICTOR — ALL TOPICS EDITION 📘")
print("Available Topics:")

for code, name in topic_mapping.items():
    print(f"{code} - {name}")

try:
    topic_code = int(input("\nEnter topic code (e.g., 3): "))
    study_times = int(input("How many times did you study this topic? "))
    total_time = int(input("Total time spent studying (in minutes): "))
    gap_days = int(input("Average days between study sessions: "))
    confidence = int(input("Your confidence level (1-10): "))
    quiz_score = int(input("Quiz/Test score (out of 100): "))
    days_since_last = int(input("Days since last revision: "))
except ValueError:
    print("❌ Invalid input. Please enter valid numbers only.")
    exit()

# ----------------------------- Prediction -----------------------------
user_input = [[
    topic_code, study_times, total_time, gap_days,
    confidence, quiz_score, days_since_last
]]

prediction = model.predict(user_input)[0]
print(f"\n🧠 Estimated Memory Burn Rate: {prediction:.1f} days")

# ----------------------------- Optional: Accuracy Display -----------------------------
score = model.score(X_test, y_test) * 100
print(f"📊 Model Accuracy (R² Score): {score:.2f}%")
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("✅ Model saved as model.pkl")