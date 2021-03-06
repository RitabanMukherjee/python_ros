from multiple_choice_quiz import Question

question_prompts = [
    "What color are apples?\na)Red/Green \nb)Purple \nc)Orange",
    "What color are bananas?\na)Teal \nb)Magenta \nc)Yellow",
    "What color are strawberries?\na)Yellow \nb)Red \nc)Blue"
]

questions = [
    Question(question_prompts(0), "a"),
    Question(question_prompts(1), "c"),
    Question(question_prompts(2), "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " questions right!")

run_test(questions)