import pandas
import turtle
from states import States
data = pandas.read_csv('50_states.csv')

screen = turtle.Screen()
screen.title('U.S States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
state = States()
turtle.shape(image)

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(
        title=f' {state.score}/50 Guess a state', prompt='Guess one of the states').title()
    if answer_state != 'Exit':
        state.check_answer(answer_state)
    else:
        state.create_csv()
        game_is_on = False
    if len(state.states_guessed) == 50:
        print('you win')
        game_is_on = False
        state.create_csv()
        screen.title('YOU WIN!')
