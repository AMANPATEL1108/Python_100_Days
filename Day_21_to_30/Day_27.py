questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A) New Delhi", "B) Mumbai", "C) Kolkata", "D) Chennai"],
        "answer": "A"
    },
    {
        "question": "Who is the Prime Minister of India?",
        "options": ["A) Narendra Modi", "B) Rahul Gandhi", "C) Amit Shah", "D) Arvind Kejriwal"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) J.K. Rowling", "D) Mark Twain"],
        "answer": "B"
    }
]

prizes = [1000, 5000, 10000, 50000, 100000]

score = 0
total_amount = 0

def ask_question(q_num):
    global total_amount
    question = questions[q_num]
    print(f"\nQuestion {q_num + 1}: {question['question']}")
    for option in question['options']:
        print(option)
    user_answer = input("Please enter the option (A/B/C/D): ").upper()

    if user_answer == question['answer']:
        print("Correct!")
        total_amount += prizes[q_num]
    else:
        print(f"Wrong! The correct answer was {question['answer']}")
        return False
    return True

def play_game():
    print("Welcome to Kaun Banega Crorepati!")
    for i in range(len(questions)):
        if not ask_question(i):
            break
    print(f"\nYou are taking home ₹{total_amount}!")

play_game()
