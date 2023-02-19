# This program simulates two space bar games
# Game 1 is hit spacebar until you get 100 and calculates time
# game 2 is hit spacebar as much as you can in 5 seconds

# import things from Pythons API
# Time function to time things and give it variable name as time
import time as time
# The Python Turtle Graphics
import turtle

# Hide the turtle
turtle.hideturtle()
# Brings the turtle up so that it does not draw on the page
turtle.up()
# Go to the specified (x, y) coordinate
turtle.goto(-150, 0)

# used to keep track of the user's time, ending time - start time = total time
start = 0
# used tp keep track of the amount of times user clicks space bar
spacePress = 0
turtle.write("Press Left for Space Game 1, Right for Space Game 2")

# Create and initialize booleans but set all initally to false
game1Playing = False
game1End = False

game2Playing = False
game2End = False
timerActive = False

# Function for if Left arrow key is pressed aka game 1

def left():
  # global keyword used so that you can access the variable created earlier, 
  # bring it into this function and modify it
  global game1Playing
  global start
  game1Playing = True
  # Set start as the time function
  start = time.time()
  # Clear the text, press left for space...
  turtle.clear()
  turtle.goto(-100, 0)
  turtle.write("Click Space as Much as Possible")

# Function for if Right arrow key is pressed aka game 2
def right():
  global game2Playing
  game2Playing = True
  turtle.clear()
  turtle.goto(-100,0)
  turtle.write("Click Space as Much as Possible")

# Activate timer for game 2

def TimerActivate():
  global game2End
  # User has 5 seconds to press space bar as fast as they can
  timeVal = 5

  # For loop runs 5 times
  for i in range(timeVal):
    turtle.clear()
    turtle.goto(-100, 0)
    # str function to convert an integer to string so it can be written
    turtle.write("Seconds Remaining: " + str(timeVal - i))
    # Wait 1 second before running the loop again
    time.sleep(1)

  game2End = True

# The space bar part, also checks which game is being played, 1 or 2
# code runs when you click the space bar

def space():
  global game1Playing
  global spacePress
  global timerActive
  global game2Playing
  # this is for game 1 as user has to press space 100 times
  # in shortest amount of time
  spacePressAmt = 100

  # this is set to true so it continues running, no for loop needed
  if (game1Playing):
    spacePress += 1
    turtle.clear()
    end = time.time()
    turtle.goto(-50,0)
    turtle.write(str(spacePress) + "/" + str(spacePressAmt) + " presses")

    if (spacePress >= spacePressAmt):
      end = time.time()
      turtle.clear()
      turtle.goto(-50,0)
      # round function is round to two decimal places
      turtle.write("Time is " + str(round(end-start,2)) + " seconds!")
      game1Playing = False
   
  elif (game2Playing):
    spacePress += 1
    if (timerActive == False):
      timerActive = True
      TimerActivate()

      if (game2End):
        turtle.clear()
        turtle.goto(-15,0)
        turtle.write(str(spacePress) + " Presses!")
        game2Playing = False

# onkey means call the function space, left or right if the key pressed
# is left, right or space

turtle.onkey(left, "Left")
turtle.onkey(right, "Right")
turtle.onkey(space, "space")

# allows the turtle to wait in user command until doing something
turtle.listen()