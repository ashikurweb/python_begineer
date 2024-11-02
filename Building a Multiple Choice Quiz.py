from Question import  Question

question_prompts = [
    "What is your name?\n(a) Ashik\n(b) Rasel\n(c) Mehedi\n\n",
    "What is your age?\n(a) 20\n(b) 21\n(c) 22\n\n",
    "What is your gender?\n(a) Male\n(b) Female\n(c) Other\n\n"

]

questions = [
    Question(question_prompts[0], 'a'),
    Question(question_prompts[1], 'b'),
    Question(question_prompts[2], 'a')
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + '/' + str(len(questions)) + 'Correct')


run_test(questions)
