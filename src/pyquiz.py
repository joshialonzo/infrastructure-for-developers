from questions import QuestionMC
from questions import QuestionTF
from quiz import Quiz
from answer import Answer


class QuizApp:
    def __init__(self):
        self.username = ""

    def startup(self):
        # print the greeting at startup
        self.greeting()
        self.username = input("What is your name? ")
        print(f"Welcome, {self.username}!")
        print()

    def greeting(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print("-~-~-~-~-~ Welcome to PyQuiz! -~-~-~-~-~")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print()

    def menu_header(self):
        print("----------------------------------------")
        print("Please make a selection: ")
        print("(M): Repeat this menu")
        print("(L): List quizzes")
        print("(T): Take a quiz")
        print("(E): Exit program")

    def menu_error(self):
        print("That's not a valid selection. Please try again.")

    def goodbye(self):
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")
        print(f"Thanks for using PyQuiz, {self.username}!")
        print("-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~")

    def menu(self):
        self.menu_header()
        selection = ""
        while True:
            selection = input("Selection? ")
            if len(selection) == 0:
                self.menu_error()
                continue
            selection = selection.capitalize()

            if selection[0] == "E":
                self.goodbye()
                break
            elif selection[0] == "M":
                self.menu_header()
                continue
            elif selection[0] == "L":
                print("\nAvailable quizzes are: ")
                print("------------------------\n")
                continue
            elif selection[0] == "T":
                try:
                    quiz_number = int(input("Quiz number: "))
                    print(f"You have selected quiz {quiz_number}.")
                    # TODO: Start the quiz
                except ValueError:
                    self.menu_error()
                    continue
            else:
                self.menu_error()

    # this is the entrypoint to the program
    def run(self):
        # Execute the startup routine - ask for name, print greeting, etc
        self.startup()
        # Start the main program menu and run until the user exits
        self.menu()


if __name__ == "__main__":
    qz = Quiz()
    qz.name = "Sample Quiz"
    qz.description = "This is a sample quiz!"

    q1 = QuestionTF()
    q1.text = "Broccoli is good for you?"
    q1.points = 5
    q1.correct_answer = "t"
    qz.questions.append(q1)

    q2 = QuestionMC()
    q2.text = "What is 2 + 2?"
    q2.points = 10
    q2.correct_answer = "b"
    ans = Answer()
    ans.name = "a"
    ans.text = "3"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "b"
    ans.text = "4"
    q2.answers.append(ans)
    ans = Answer()
    ans.name = "c"
    ans.text = "5"
    q2.answers.append(ans)
    qz.questions.append(q2)

    qz.total_points = q1.points + q2.points
    result = qz.take_quiz()
    print(result)
