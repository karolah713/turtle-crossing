from turtle import Screen
import time
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(player.player_move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()


    #detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()

    #detect colision with top wall
    if player.ycor() > 280:
        player.reset_position()
        car_manager.level_up()
        scoreboard.update_level()








screen.exitonclick()