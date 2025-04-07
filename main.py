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

game_is_on = True
states_data = pandas.read_csv("50_states.csv")

while game_is_on:
    answer_state = screen.textinput(title=f"{scores.score}/50 States guessed", prompt="What's another state's name?\n").title()
    if states_data.isin([answer_state]).any().any():
        # print(states_data[states_data.state == str(answer_state)].x)
        scores.display_score(int(states_data[states_data.state == str(answer_state)].x.iloc[0]), int(states_data[states_data.state == str(answer_state)].y.iloc[0]), answer_state)
        scores.increase_score()
        screen.update()

screen.mainloop()