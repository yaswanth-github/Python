import random

def generate_question():
    # generate two random numbers between 1 and 10
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # generate a random operator
    operator = random.choice(["+", "-", "*"])
    
    # create the question string
    question = f"What is {num1} {operator} {num2}?"
    
    # calculate the correct answer
    if operator == "+":
        answer = num1 + num2
    elif operator == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2
    
    return question, answer

def quiz():
    num_questions = 5
    num_correct = 0
    
    print("Welcome to the math quiz!")
    print(f"You will be asked {num_questions} questions.")
    
    for i in range(num_questions):
        # generate a question
        question, answer = generate_question()
        
        # ask the question and get the user's answer
        user_answer = input(question)
        
        # check if the user's answer is correct
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue
        
        if user_answer == answer:
            print("Correct!")
            num_correct += 1
        else:
            print(f"Incorrect. The correct answer is {answer}.")
    
    # print the user's score
    print(f"You got {num_correct} out of {num_questions} questions correct.")
    
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        quiz()
    else:
        print("Thanks for playing!")

quiz()