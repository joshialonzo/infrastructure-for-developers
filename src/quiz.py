class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0

    def print_header(self):
        print("\n\n************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("**************************************\n")

    def print_results(self):
        print("\n\n************************************")
        print("**************************************\n")

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0

        for q in self.questions:
            q.is_correct = False
        
        self.print_header()
        
        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points
        
        print("**************************************\n")

        return (self.score, self.correct_count, self.total_points)
