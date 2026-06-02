
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
    app = QuizApp()
    app.run()
