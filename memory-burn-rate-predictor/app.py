from flask import Flask, render_template, request
import pandas as pd
import pickle  # If you're saving/loading your trained model

app = Flask(__name__)

# Load your trained model (assumes it's saved as model.pkl)
model = pickle.load(open('model.pkl', 'rb'))

# Load topic mapping
df = pd.read_csv('dataset.csv')
df['topic'] = df['topic'].astype('category')
topic_mapping = dict(enumerate(df['topic'].cat.categories))

@app.route('/')
def index():
    return render_template('index.html', topics=topic_mapping)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        topic_code = int(request.form['topic_code'])
        study_times = int(request.form['study_times'])
        total_time = int(request.form['total_time'])
        gap_days = int(request.form['gap_days'])
        confidence = int(request.form['confidence'])
        quiz_score = int(request.form['quiz_score'])
        days_since_last = int(request.form['days_since_last'])

        user_input = [[
            topic_code, study_times, total_time, gap_days,
            confidence, quiz_score, days_since_last
        ]]

        prediction = model.predict(user_input)[0]
        return render_template('index.html', topics=topic_mapping, prediction=round(prediction, 1))
    
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
