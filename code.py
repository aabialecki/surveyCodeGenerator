import helpers


_question = "are you tall or short"
_options = ['tall', 'short']
_responses = None
_newQuestions = [{'question_text': 'taller then a giraffe?', 'choices': {'questions': None, 'responses': ["Wow, you're Tall!", None], 'options': ['yes', 'no']}}, {'question_text': 'shorter then a mouse?', 'choices': {'questions': None, 'responses': ["Wow, you're Short!", None], 'options': ['yes', 'no']}}]

userInput = helpers.verify_input("are you tall or short", _options)
helpers.save_input(userInput,_question)

if {'question_text': 'taller then a giraffe?', 'choices': {'questions': None, 'responses': ["Wow, you're Tall!", None], 'options': ['yes', 'no']}} != None and 0 == _options.index(userInput):

	_question = "taller then a giraffe?"
	_options = ['yes', 'no']
	_responses = ["Wow, you're Tall!", None]
	_newQuestions = None

	userInput = helpers.verify_input("taller then a giraffe?", _options)
	helpers.save_input(userInput,_question)

	resp = _responses[_options.index(userInput)]

	if resp != None: 
		print(resp)
if {'question_text': 'shorter then a mouse?', 'choices': {'questions': None, 'responses': ["Wow, you're Short!", None], 'options': ['yes', 'no']}} != None and 1 == _options.index(userInput):

	_question = "shorter then a mouse?"
	_options = ['yes', 'no']
	_responses = ["Wow, you're Short!", None]
	_newQuestions = None

	userInput = helpers.verify_input("shorter then a mouse?", _options)
	helpers.save_input(userInput,_question)

	resp = _responses[_options.index(userInput)]

	if resp != None: 
		print(resp)