import helpers

# Choices:
# Contains information regarding reactions and restricitons on user input
# choices = {'questions':questions,     //new questions to ask user based on choice TYPE=ARRAY - Optional
#            'responses':responses,     //text responses to each option TYPE=ARRAY - Optional
#            'options':options}         //restict user input to these options TYPE=ARRAY - Must be included
class Code():

    #Code for this Question
    CODE = ""

    newQuestions = None
    options = None
    responses = None

    #Create Object
    #indent_level makes indented blocks depending on level
    def __init__(self, question_info,indent_level = 0):
        self.question_text = question_info["question_text"]
        self.choices = question_info["choices"]
        self.indent_level = indent_level

        #Checks question for additional options
        if self.choices != None:
            if self.choices["questions"] != None:
                self.newQuestions = self.choices["questions"]
            if self.choices["options"] != None:
                self.options = self.choices["options"]
            if self.choices["responses"] != None:
                self.responses = self.choices["responses"]

        #setting up needed variables
        self.indent_code("_question = \"{question}\"".format(question=self.question_text))
        self.indent_code("_options = {options}".format(options=self.options))
        self.indent_code("_responses = {responses}".format(responses=self.responses))
        self.indent_code("_newQuestions = {newQuestions}\n".format(newQuestions=self.newQuestions))

    def indent_code(self,codepiece):
        self.CODE += "\n"
        for i in range(self.indent_level):
            self.CODE += "\t"
        self.CODE += codepiece


    #Generate user input code
    def gen_userinput(self):
        if self.options != None: 
            self.indent_code("userInput = helpers.verify_input(\"{question}\", _options)".format(question=self.question_text))
        else:
            self.indent_code("userInput = input(\"{question}\"".format(question=self.question_text))
        self.indent_code("helpers.save_input(userInput,_question)\n")

    #Generate question response code
    def gen_response(self):
        self.indent_code("resp = _responses[_options.index(userInput)]\n")
        self.indent_code("if resp != None: ")
        self.indent_level+=1
        self.indent_code("print(resp)")

    def gen_newQuestions(self):
        for q in range(len(self.newQuestions)):
            self.indent_code("if {newq} != None and {index} == _options.index(userInput):".format(newq=self.newQuestions[q],index=q))
            nq = Code(self.newQuestions[q],self.indent_level+1)
            self.indent_code(nq.gencode())



    def gencode(self):
        self.gen_userinput()
        if self.responses != None:
            self.gen_response()
            self.indent_level -= 1
        if self.newQuestions != None:
            self.gen_newQuestions()

        return self.CODE


  
q1_info = {"question_text":"are you tall or short", #Main Question
            "choices":{"questions":[{"question_text":"taller then a giraffe?", #Secondary Question based on Option Selected
                                    "choices":{"questions":None,
                                               "responses":["Wow, you're Tall!",None], #Response to option selected for secondary question
                                               "options":["yes","no"]}}, #secondary question options
                                    {"question_text":"shorter then a mouse?", #Secondary Question based on Option Selected
                                    "choices":{"questions":None,
                                               "responses":["Wow, you're Short!",None], #Response to option selected for secondary question
                                               "options":["yes","no"]}}], #secondary question options
                        "responses":None,
                        "options":["tall","short"] #Main Question Options
                }}



def main():
    CODE = "import helpers\n\n"
    questions = [q1_info] #this array can be filld with any number of questions
    for q in questions:
        question = Code(q)
        CODE += question.gencode()
    print(CODE)
    helpers.save_code(CODE)
    exec(CODE)

main()    



       

