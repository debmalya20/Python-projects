questions = [
    "Q1. Who invented TESLA?",
    "Q2. What is the capital of WEST BENGAL?",
    "Q3. Which language is used in Python?"
]

options = [
    ["A. Elon Musk", "B. Narendra Modi", "C. Mamata Banerjee"],
    ["A. Kolkata", "B. Jharkhand", "C. Bhubaneswar", "D. Delhi"],
    ["A. English", "B. Bangla", "C. Telugu", "D. Urdu"]
]

answers = ["A", "A", "A"]

score = 0

for i in range(3):
    print("\n", questions[i])

    for opt in options[i]:
        print(opt)

    user = input("Enter your answer (A/B/C/D): ")

    if user.upper() == answers[i]:
        print("Correct")
        score = score + 1
    else:
        print("Wrong ")

print("\nYour score is:", score)