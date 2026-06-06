import xml.sax
from pathlib import Path
from quiz import *
from enum import Enum, unique

from answer import Answer
from questions import QuestionMC
from questions import QuestionTF


@unique
class QuizParserState(Enum):
    IDLE = 0
    PARSE_QUIZ = 1
    PARSE_DESCRIPTION = 2
    PARSE_QUESTION = 3
    PARSE_QUEST_TEXT = 4
    PARSE_ANSWER = 5


class QuizParser(xml.sax.ContentHandler):
    """
    The QuizParser class loads a particular quiz file, parses it, and returns a
    a fully-built Quiz object that can be presented to the user.
    """

    def __init__(self):
        self.new_quiz = Quiz()
        self._parse_state = QuizParserState.IDLE
        self._current_question = None
        self._current_answer = None

    def parse_quiz(self, quizpath):
        quizfile = Path(quizpath)
        if not quizfile.exists():
            quizfile = Path(__file__).resolve().parent / quizpath

        if not quizfile.exists():
            raise FileNotFoundError(f"Quiz file not found: {quizpath}")

        quiztext = quizfile.read_text()
        xml.sax.parseString(quiztext, self)
        return self.new_quiz

    def startElement(self, tagname, attrs):
        if tagname == "QuizML":
            self._parse_state = QuizParserState.PARSE_QUIZ
            self.new_quiz.name = attrs["name"]
        elif tagname == "Description":
            self._parse_state = QuizParserState.PARSE_DESCRIPTION
        elif tagname == "Question":
            self._parse_state = QuizParserState.PARSE_QUESTION
            if attrs["type"] == "multichoice":
                self._current_question = QuestionMC()
            elif attrs["type"] == "tf":
                self._current_question = QuestionTF()
            self._current_question.points = int(attrs["points"])
            self.new_quiz.total_points += self._current_question.points
        elif tagname == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUEST_TEXT
            self._current_question.correct_answer = attrs["answer"]
        elif tagname == "Answer":
            self._current_answer = Answer()
            self._current_answer.name = attrs["name"]
            self._parse_state = QuizParserState.PARSE_ANSWER

    def endElement(self, tagname):
        if tagname == "QuizML":
            self._parse_state = QuizParserState.IDLE
        elif tagname == "Description":
            self._parse_state = QuizParserState.PARSE_QUIZ
        elif tagname == "Question":
            self.new_quiz.questions.append(self._current_question)
            self._parse_state = QuizParserState.PARSE_QUIZ
        elif tagname == "QuestionText":
            self._parse_state = QuizParserState.PARSE_QUESTION
        elif tagname == "Answer":
            self._current_question.answers.append(self._current_answer)
            self._parse_state = QuizParserState.PARSE_QUESTION

    def characters(self, chars):
        if self._parse_state == QuizParserState.PARSE_DESCRIPTION:
            self.new_quiz.description += chars
        elif self._parse_state == QuizParserState.PARSE_QUEST_TEXT:
            self._current_question.text += chars
        elif self._parse_state == QuizParserState.PARSE_ANSWER:
            self._current_answer.text += chars


if __name__ == "__main__":
    app = QuizParser()
    qz = app.parse_quiz("quizzes/MyQuiz.xml")
    print(f"Quiz name: {qz.name}")
    print(f"Quiz description: {qz.description}")
    print(f"Number of questions: {len(qz.questions)}")
    print(f"Total points: {qz.total_points}")
    print("Questions:")
    for index, q in enumerate(qz.questions):
        print(f"{index + 1}. {q.text}")
