import turtle
import pandas

TOTAL_ANSWERS = 50
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_turtle = turtle.Turtle()
state_turtle.penup()
state_turtle.hideturtle()

states_data = pandas.read_csv("50_states.csv")
states_list = states_data["state"].to_list()
guesses_states = []
missed_states = []

while len(guesses_states) < 50:
    answer_state = screen.textinput(title=f"| {len(guesses_states)}/{TOTAL_ANSWERS} | States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        break
    if answer_state in states_list:
        guesses_states.append(answer_state)
        x_cor = states_data[states_data["state"] == answer_state]["x"]
        y_cor = states_data[states_data["state"] == answer_state]["y"]
        state_turtle.goto(int(x_cor), int(y_cor))
        state_turtle.write(answer_state)


for state in states_list:
    if state not in guesses_states:
        missed_states.append(state)

dt = pandas.DataFrame(missed_states)
dt.to_csv("states_to_learn.csv")
