import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)} /50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        non_guessed_states = [state for state in all_states if state not in guessed_states]
        missed_states = pd.DataFrame({"States": non_guessed_states})
        missed_states.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # the line below is a variable created to find the specific row inside the state column (answer of the player)
        # and let us access to the info of that specific row
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # the line below asks the turtle to write the state name by tapping into the states column and writing jut the
        # name
        t.write(answer_state)

