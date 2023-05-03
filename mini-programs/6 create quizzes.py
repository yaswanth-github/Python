class Quiz:
    def __init__(self, name):
        self.name = name
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def generate_quiz(self):
        total_score = 0
        print(f"Quiz: {self.name}\n")
        for i, question in enumerate(self.questions):
            print(f"{i+1}. {question.text}")
            user_answer = input("Your answer: ")
            if user_answer == question.answer:
                total_score += question.points
                print(f"Correct! {question.points} points earned.\n")
            else:
                print(f"Incorrect. The correct answer was {question.answer}.\n")
        print(f"Your total score is: {total_score}\n")

class Question:
    def __init__(self, text, answer, points):
        self.text = text
        self.answer = answer
        self.points = points

def create_question():
    text = input("Enter the question text: ")
    answer = input("Enter the correct answer: ")
    points = int(input("Enter the point value for this question: "))
    return Question(text, answer, points)

def create_quiz():
    name = input("Enter the quiz name: ")
    quiz = Quiz(name)

    while True:
        print("Menu:")
        print("1. Add a question")
        print("2. Generate the quiz")
        print("3. Cancel and exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            question = create_question()
            quiz.add_question(question)
        elif choice == "2":
            quiz.generate_quiz()
            break
        elif choice == "3":
            break
        else:
            print("Invalid choice! Please enter a valid choice.")
    
    print("Quiz creation cancelled.")

def main():
    while True:
        print("Menu:")
        print("1. Create a quiz")
        print("2. Quit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            create_quiz()
        elif choice == "2":
            break
        else:
            print("Invalid choice! Please enter a valid choice.")
    
    print("Goodbye!")

if __name__ == "__main__":
    main()
