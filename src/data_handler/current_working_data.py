from data_handler.data_reader import get_data
from random import choice, shuffle

index = count_correct = count_wrong = 0

file, topic, working_file_path = get_data()

shuffle(file)

question = file[index][0]
answer = file[index][1]
wrong_answer = choice(file[index][2:])
answer_options = [answer, wrong_answer]
shuffle(answer_options)

def update_question(is_correct: bool) -> None:
    global answer, question, wrong_answer, index, count_correct, count_wrong, answer_options
    if index < len(file) - 1:
        index += 1
    else:
        index = 0
        shuffle(file)

    count_wrong += not is_correct
    count_correct += is_correct
    
    question = file[index][0]
    answer = file[index][1]
    wrong_answer = choice(file[index][2:])

    answer_options = [answer, wrong_answer]
    shuffle(answer_options)