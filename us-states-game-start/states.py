from turtle import Turtle
import pandas

data = pandas.read_csv('50_states.csv')


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.states_guessed = []
        self.states_to_use = data.state.values

    def check_answer(self, answer):
        """Takes a string argument and compares it to data in csv to confirm if its a match"""

        if answer in self.states_to_use:
            if answer in self.states_guessed:
                print('already guessed')
            else:
                self.score += 1
                self.states_guessed.append(answer)
                self.place_on_map(answer)
                print('correct')
        else:
            print('wrong')

    def place_on_map(self, answer):
        answer_state = data[data['state'] == f'{answer}']
        x_cor = answer_state['x'].values[0]

        y_cor = answer_state['y'].values[0]
        cord = (x_cor, y_cor)
        new_state = Turtle()
        new_state.penup()
        new_state.hideturtle()

        new_state.goto(cord)
        new_state.write(f'{answer}')

    def create_csv(self):
        missed_states = []
        for i in self.states_to_use:
            if i not in self.states_guessed:
                missed_states.append(i)
        dict_send = {
            'states': [missed_states]
        }
        pandas.Series(dict_send).to_csv('missed_states.csv')
