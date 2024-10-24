import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.go_up, "Up")

cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    for car in cars.all_car:
        if car.distance(player) < 30:
            game_is_on = False
            score.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        cars.level_up()
        score.increase_level()

screen.exitonclick()