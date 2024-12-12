questions = {
    "What is the capital of France?": "paris",
    "What is 5 + 3?": "8",
    "What color is the sky on a clear day?": "blue"
}
score = 0

print("Welcome to the Quiz Game!")
for question, answer in questions.items():
    user_answer = input(f"{question} ").lower()
    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}.")

print(f"Game over! Your final score is {score}/{len(questions)}.")
