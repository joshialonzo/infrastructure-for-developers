# Quiz App

## Requirements

* Extensible quiz definitions
    - New quizzes can be added wihtout changing code
* Quiz results are tracked and presented to the user
    - Score, number of correct questions, etc.
* Results can be saved in a file

## Application Architecture

* Quiz App (front-end)
    - Presents the app
    - Handles the menu selections
    - Instantiates the Quiz Manager

* Quiz Manager (back-end)
    - Maintains the list of quizzes
    - Coordinates the quiz presentation
    - Displays and saves the results

* Quiz Parser
    - Parses quiz from XML
        * Creates a quiz from XML

* Quiz
    - Question
    - Answer