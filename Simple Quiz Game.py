def quiz_game():
    questions = {
        "What is the capital of France?": "a",
        "What is 2 + 2?": "b",
        "What is the color of the sky?": "c"
    }
    options = {
        "What is the capital of France?": "a) Paris b) London c) Berlin",
        "What is 2 + 2?": "a) 3 b) 4 c) 5",
        "What is the color of the sky?": "a) Red b) Green c) Blue"
    }
    score = 0

    for question, correct_answer in questions.items():
        print(question)
        print(options[question])
        answer = input("Your answer: ").lower()

        if answer == correct_answer:
            score += 1

    print(f"Your final score is {score}/{len(questions)}")


quiz_game()
