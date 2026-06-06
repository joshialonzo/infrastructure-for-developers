from pathlib import Path
import importlib.util

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
        pass

    def print_results(self):
        pass

    def save_results(self):
        pass


if __name__ == "__main__":
    qm = QuizManager("quizzes")
    qm.list_quizzes()
