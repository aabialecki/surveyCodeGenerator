# surveyCodeGenerator
This program will generate the code for a simple python survey based on a list of questions and options. Currently there is no system for inputting survey details so it must be done seperatly, the format for questions is layed out below.


#Usage
* in codegen.main() you can put your questions into the list questions = []
* each question in the list must follow the format layed out in question_format below
* Running the program will generate code in a seperate code.py file
* once generated it will run the program and save user responses in a seperate file


#Question_format

question = {  "question_text":question_text,  - the question to ask the user
              "choices":choices"}             - specify restrictions on user input and responses to that input, set to None if not in use

each value in the choices dictionary is an array, new questions and responses are based on user response. For example, if the user responded with the option in index 2 of the options list, it would ask a new question or send a response based on index 2 of the questions and responses list. if you do not want a response or new question for a certain user input, specify that index as None
choices = {   "questions":[questions],        - new questions to ask user
              "responses":[responses],        - responses to user answers
              "options":[options]}            - the options the user is allowed to answer with
