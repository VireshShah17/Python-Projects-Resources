import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
car = CarManager()
level= Scoreboard()
screen.onkey(key="Up",fun=player.up)
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    # Detecting player collision with car
    for cars in car.all_cars:
        if cars.distance(player) < 20 :
            level.game_over()
            game_is_on = False

    # Detecting if the player has reached the otherside or not
    if player.at_end():
        player.is_win()
        car.level_up()
        level.inc_level()


screen.exitonclick()
