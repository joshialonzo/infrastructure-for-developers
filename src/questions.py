class Question:
    def __init__(self):
        self.points = 0
        self.correct_answer = ""
        self.text = ""
        self.is_correct = False


class QuestionTF(Question):
    def __init__(self):
        super().__init__()

    def ask(self):
        while True:
            print(f"(T)rue or (F)alse: {self.text}")
            response = input("? ")

            if len(response) == 0:
                print("Sorry, that's not a valid response. Please try again.")
                continue

            response = response.lower()
            if response[0] != "t" and response[0] != "f":
                print("Sorry, that's not a valid response. Please try again.")
                continue

            if response[0] == self.correct_answer:
                self.is_correct = True
            
            break


class QuestionMC(Question):
    def __init__(self):
        super().__init__()
        self.answers = []

    def ask(self):
        while True:
            print(self.text)
            for a in self.answers:
                print(f"({a.name}) {a.text}")
            response = input("? ")

            if len(response) == 0:
                print("Sorry, that's not a valid response. Please try again.")
                continue

            response = response.lower()
            if response[0] == self.correct_answer:
                self.is_correct = True

            break
