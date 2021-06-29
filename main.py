from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)  # 400 es la meta  (+250)
user_bet = screen.textinput(title="Make your bet", prompt="Which "
"turtle will win the race? Enter a color: ")
colors = ['red', 'orange', 'black', 'green', 'blue', 'purple']
y_positions = [-90, -40, 10, 60, 110, 160]
all_champs = []

for index in range(0, 6):
    champ = Turtle(shape='turtle')
    champ.shapesize(2)
    champ.color(colors[index])
    champ.penup()
    champ.goto(x=-230, y=y_positions[index])
    all_champs.append(champ)

if user_bet:
    is_race_on = True

while is_race_on:
    for champ in all_champs:
        if champ.xcor() > 230:
            is_race_on = False
            winning_color = champ.pencolor()
            if winning_color == user_bet:
                print(f'You won! The {winning_color} turtle is the winner!')
            else:
                print(f'You lost! The {winning_color} turtle is the winner!')
        random_distance = random.randint(0, 10)
        champ.forward(random_distance)

screen.listen()
screen.exitonclick()
