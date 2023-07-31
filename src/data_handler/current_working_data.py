from data_handler.data_reader import get_data
from random import choice, shuffle

class CurrentData():
    def __init__(self):
        self.file, self.topic, self.working_file_path = get_data()

        if self.file == None:
            return
        
        self.index = self.count_correct = self.count_wrong = 0
        shuffle(self.file)
        
        self.question = self.file[self.index][0]
        self.answer = self.file[self.index][1]
        self.wrong_answer = choice(self.file[self.index][2:])
        self.answer_options = [self.answer, self.wrong_answer]
        shuffle(self.answer_options)
    
    def update_question(self, is_previous_ans_correct):
        if self.index < len(self.file) - 1:
            self.index += 1
        else:
            self.index = 0
            shuffle(self.file)
        
        self.count_wrong += not is_previous_ans_correct
        self.count_correct += is_previous_ans_correct

        self.question = self.file[self.index][0]
        self.answer = self.file[self.index][1]
        self.wrong_answer = choice(self.file[self.index][2:])

        self.answer_options = [self.answer, self.wrong_answer]
        shuffle(self.answer_options)