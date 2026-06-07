import datetime
import importlib.util
import os
from pathlib import Path

# Load parser.py explicitly from the same directory as this script
_parser_path = Path(__file__).resolve().parent / "parser.py"
spec = importlib.util.spec_from_file_location("parser", str(_parser_path))
parser = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parser)
QuizParser = parser.QuizParser


class QuizManager:
    def __init__(self, quizfolder):
        # resolve quiz folder (accepts absolute, cwd-relative, or relative to this file)
        folder = Path(quizfolder)

        if not folder.exists():
            folder = Path(__file__).resolve().parent / quizfolder

        if not folder.exists():
            raise FileNotFoundError(f"Quiz folder does not seem to exist: {quizfolder}")

        self.quizfolder = folder
        self.the_quiz = None
        self.quizzes = dict()
        self.results = None
        self.quiztaker = ""

        self._build_quiz_list()

    def _build_quiz_list(self):
        dircontents = self.quizfolder.iterdir()
        for i, f in enumerate(dircontents):
            if f.is_file():
                _parser = QuizParser()
                self.quizzes[i+1] = _parser.parse_quiz(f)

    def list_quizzes(self):
        for k, v in self.quizzes.items():
            print(f"({k}): {v.name}")

    def take_quiz(self, quizid, username):
        self.quiztaker = username
        self.the_quiz = self.quizzes[quizid]
        self.results = self.the_quiz.take_quiz()

    def print_results(self):
        self.the_quiz.print_results(self.quiztaker)

    def save_results(self):
        today = datetime.datetime.now()
        filename = f"QuizResults_{today.year}_{today.month}_{today.day}.txt"

        n = 1
        while os.path.exists(filename):
            filename = f"QuizResults_{today.year}_{today.month}_{today.day}_{n}.txt"
            n += 1

        with open(filename, "w") as f:
            self.the_quiz.print_results(self.quiztaker, f)

if __name__ == "__main__":
    qm = QuizManager("quizzes")
    qm.list_quizzes()
