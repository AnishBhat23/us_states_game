import turtle
import pandas
from scores import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

scores = Scoreboard()


states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

while scores.score < 50:
    answer_state = screen.textinput(title=f"{scores.score}/50 States guessed", prompt="What's another state's name?\n").title()
    if answer_state == "Exit":
        all_states_data = pandas.DataFrame(all_states)
        all_states_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        # print(states_data[states_data.state == str(answer_state)].x)
        all_states.remove(answer_state)
        scores.display_score(int(states_data[all_states == str(answer_state)].x.iloc[0]), int(states_data[all_states == str(answer_state)].y.iloc[0]), answer_state)
        scores.increase_score()
        screen.update()
