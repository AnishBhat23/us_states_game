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
guessed_states = []

while scores.score < 50:
    answer_state = screen.textinput(title=f"{scores.score}/50 States guessed", prompt="What's another state's name?\n").title()
    if answer_state == "Exit":
        #states_to_learn = pandas.DataFrame(~(states_data.isin([guessed_states])))
        #states_to_learn.to_csv("states_to_learn.csv")
        break
    if states_data.isin([answer_state]).any().any():
        # print(states_data[states_data.state == str(answer_state)].x)
        guessed_states.append(answer_state)
        scores.display_score(int(states_data[states_data.state == str(answer_state)].x.iloc[0]), int(states_data[states_data.state == str(answer_state)].y.iloc[0]), answer_state)
        scores.increase_score()
        screen.update()
