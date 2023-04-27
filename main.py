# import turtle
#
# #create screen objact
# screen=turtle.Screen()
#
# screen.title("Game States of U.S.A")
# image="blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# #check coordination of each state on screen
# def get_mouse_coordinate(x,y):
#     print(x,y)
#
# #bind fun to a mouse-click event on canvas
# turtle.onscreenclick(get_mouse_coordinate)
#
# #keep screen open
# turtle.mainloop()
#
# #get info from csv file
# user_answer=screen.textinput(title="Guess the state", prompt="enter the state name")
# print(user_answer)

import turtle
import pandas


screen=turtle.Screen()
screen.title("U.S State")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_state_list=data["state"].to_list()
guess_states=[]


while len(guess_states) < 50:
     answer = screen.textinput(title=f"{len(guess_states)}/50 State correct", prompt="name of the State: ").title()

     if answer=="Exit":
          missing_states=[]
          for state in all_state_list:
               if state not in guess_states:
                    missing_states.append(state)
          # state to learn csv file
          new_data=pandas.DataFrame(missing_states)
          new_data.to_csv("state_to_learn.csv")
          break

     if answer in all_state_list:
          guess_states.append(answer)
          t=turtle.Turtle()
          t.hideturtle() #hide the turtle shape
          t.penup() #for not drawing things on screen
          state_data= data[data.state==answer] #pullup the row of the state
          t.goto(int(state_data.x), int(state_data.y)) #get the x value and the y value of the state
          t.write(answer)


