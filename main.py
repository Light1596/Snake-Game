from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("brown")
screen.title("SNAKE GAME")
# To avoid seeing each snake object, we use a screen method that turns off the animation
screen.tracer(0)


snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        food.new_food()
        score.score_increase()
        snake.extend()

    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() < -295 or snake.segments[0].ycor() > 295:
        score.check_game_over()
        game_is_on = False

    for every_segments in snake.segments:
        if every_segments == snake.segments[0]:
            continue
        if snake.segments[0].distance(every_segments) < 10:
            score.check_game_over()
            game_is_on = False


screen.exitonclick()
