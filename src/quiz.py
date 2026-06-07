import datetime
import random
import sys


class Quiz:
    def __init__(self):
        self.name = ""
        self.description = ""
        self.questions = []
        self.score = 0
        self.correct_count = 0
        self.total_points = 0
        self.completion_time = 0

    def print_header(self):
        print("\n\n************************************")
        print(f"QUIZ NAME: {self.name}")
        print(f"DESCRIPTION: {self.description}")
        print(f"QUESTIONS: {len(self.questions)}")
        print(f"TOTAL POINTS: {self.total_points}")
        print("**************************************\n")

    def print_results(self, quiztaker, thefile=sys.stdout):
        print("\n\n************************************", file=thefile, flush=True)
        print(f"RESULTS for {quiztaker}", file=thefile, flush=True)
        print(f"Date: {datetime.datetime.today()}", file=thefile, flush=True)
        print(f"ELAPSED TIME: {self.completion_time}", file=thefile, flush=True)
        print(
            f"QUESTIONS: {self.correct_count} out of {len(self.questions)} correct",
            file=thefile, flush=True
        )
        print(
            f"SCORE: {self.score} points out of possible {self.total_points}",
            file=thefile, flush=True
        )
        print("**************************************\n", file=thefile, flush=True)

    def take_quiz(self):
        self.score = 0
        self.correct_count = 0
        self.completion_time = 0

        for q in self.questions:
            q.is_correct = False

        self.print_header()

        random.shuffle(self.questions)

        start_time = datetime.datetime.now()

        for q in self.questions:
            q.ask()
            if q.is_correct:
                self.correct_count += 1
                self.score += q.points
            print("------------------------------\n")

        end_time = datetime.datetime.now()

        if self.correct_count != len(self.questions):
            response = input(
                "\nIt looks like you missed some questions. Re-do the wrong ones? (y/n) "
            ).lower()
            if response[0] == "y":
                wrong_questions = [q for q in self.questions if not q.is_correct]
                for q in wrong_questions:
                    q.ask()
                    if q.is_correct:
                        self.correct_count += 1
                        self.score += q.points
                    print("------------------------------\n")
                end_time = datetime.datetime.now()

        self.completion_time = datetime.timedelta(
            seconds=round(
                (end_time - start_time).total_seconds()
            )
        )

        print("**************************************\n")

        return (self.score, self.correct_count, self.total_points)
