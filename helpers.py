def verify_input(question, options):
    while True:
        userInput = input("\n\nOptions: " + str(options) + "\n" + question + ": ")
        for o in options:
            if userInput == o:
                return userInput
        print("your answer was not one of the options provided, try again.\n")

def save_input(userInput, question):
    file = open("responses.txt", "a")
    file.write("Input: " + userInput + "\t\t\tQuestion: " + question)
    file.close()

def save_code(CODE):
    file = open("code.py","w")
    file.write(CODE)
    file.close()
    