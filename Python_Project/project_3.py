import random

# Define a list of questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "choices": ["London", "Paris", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which country is known for the Great Barrier Reef?",
        "choices": ["Brazil", "Australia", "India", "South Africa"],
        "answer": "Australia"
    },
    {
        "question": "What is the largest country in the world by land area?",
        "choices": ["Russia", "Canada", "China", "United States"],
        "answer": "Russia"
    },
    {
        "question": "What is the currency of Japan?",
        "choices": ["Euro", "Yen", "Pound", "Dollar"],
        "answer": "Yen"
    },
]

# Define a function to ask a question and return True if the answer is correct
def ask_question(question):
    print(question["question"])
    for i, choice in enumerate(question["choices"]):
        print(f"{i + 1}. {choice}")
    user_answer = input("Enter your answer (1-4): ")
    if user_answer == str(question["choices"].index(question["answer"]) + 1):
        print("Correct!")
        return True
    else:
        print(f"Incorrect! The correct answer is {question['answer']}.")
        return False

# Shuffle the list of questions
random.shuffle(quiz_questions)

# Keep track of the user's score
score = 0

# Ask each question and update the score
for question in quiz_questions:
    if ask_question(question):
        score += 1

# Print the user's final score
print(f"You got {score} out of {len(quiz_questions)} questions correct!")
