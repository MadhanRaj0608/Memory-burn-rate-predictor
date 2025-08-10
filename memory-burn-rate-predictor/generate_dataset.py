import pandas as pd
import random

# Define the full list of topics: Engineering, Medical, Accounts, and School Subjects
topics = [
    # Engineering Topics
    'Operating Systems', 'DBMS', 'Computer Networks', 'Machine Learning', 'Artificial Intelligence',
    'Cyber Security', 'Software Engineering', 'Compiler Design', 'Data Structures', 'Algorithms',
    
    # Medical Topics
    'Anatomy', 'Physiology', 'Biochemistry', 'Pathology', 'Pharmacology', 'Microbiology',
    
    # Accounts and Finance Topics
    'Financial Accounting', 'Cost Accounting', 'Management Accounting', 'Auditing', 'Corporate Finance',
    
    # 10th Grade Subjects
    'Mathematics', 'Science', 'English', 'Social Studies', 'Hindi', 'Geography', 'History',
    
    # 12th Grade Subjects
    'Physics', 'Chemistry', 'Biology', 'Mathematics', 'English', 'Economics'
]

# Initialize an empty list to store dataset entries
data = []

# Function to simulate burn rate based on the study pattern
def simulate_burn_rate(word_count, study_times, total_time, gap_days, confidence, quiz_score, days_since_last):
    rate = (
        (word_count / 1000) * 0.5 +
        (total_time / (study_times + 1)) * 0.05 +
        (10 - gap_days) * 0.8 +
        confidence * 1.0 +
        quiz_score * 0.03 -
        days_since_last * 0.4
    )
    return max(1, min(int(rate), 30))  # Ensure the burn rate is between 1 and 30 days

# Generate 10,000 data entries
for _ in range(10000):  # Changed to generate 10,000 entries
    topic = random.choice(topics)  # Choose a random topic from the updated topics list
    word_count = random.randint(300, 5000)  # Word count can now be from 300 to 5000
    study_times = random.randint(1, 15)  # Increased study times from 1 to 15
    total_time = random.randint(30, 480)  # Total time can be from 30 to 480 minutes (8 hours)
    gap_days = random.randint(1, 14)  # Gap can range from 1 to 14 days
    confidence = random.randint(1, 10)  # Confidence between 1 and 10
    quiz_score = random.randint(30, 100)  # Quiz score from 30 to 100
    days_since_last = random.randint(0, 30)  # Days since last revision from 0 to 30 days

    burn_rate = simulate_burn_rate(word_count, study_times, total_time, gap_days,
                                   confidence, quiz_score, days_since_last)

    # Append the generated data to the list
    data.append([topic, word_count, study_times, total_time, gap_days, confidence,
                 quiz_score, days_since_last, burn_rate])

# Create a pandas DataFrame to structure the dataset
df = pd.DataFrame(data, columns=[
    'topic', 'word_count', 'study_times', 'total_time_mins', 'gap_days',
    'confidence', 'quiz_score', 'days_since_last', 'burn_rate_days'
])

# Save the dataset to a CSV file
df.to_csv('dataset.csv', index=False)
print("✅ Full dataset generated with 10,000 entries: dataset.csv")
