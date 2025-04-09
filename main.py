print("Hello World")

import pygame as pg
import random

pg.init()
clock = pg.time.Clock()
screen = pg.display.set_mode((600, 600))
running = True

snake = [(280, 300), (290, 300), (300, 300)] #head

direction = "RIGHT"

food = (10*random.randint(0, 59), 10*random.randint(0, 59))

    



def move(direction, grow = False):
        if direction == "RIGHT":
            new_head = (snake[-1][0] + 10, snake[-1][1])
            
        elif direction == "LEFT":
            new_head = (snake[-1][0] - 10, snake[-1][1])
            

        elif direction == "UP":
            new_head = (snake[-1][0], snake[-1][1] - 10)
            
        
        elif direction == "DOWN":
            new_head = (snake[-1][0], snake[-1][1] + 10)
            
        
        snake.append(new_head)

        if not grow:
            snake.pop(0)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    screen.fill("white")

    for i in range(len(snake) - 1):
       pg.draw.rect(surface = screen, color="black", rect=(snake[i][0], snake[i][1], 10, 10))
       pg.draw.rect(surface = screen, color="red", rect=(snake[-1][0], snake[-1][1], 10, 10))
    
    pg.draw.rect(surface = screen, color="green", rect=(food[0], food[1], 10, 10))

    clock.tick(10)

    

    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pg.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pg.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pg.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
    
    grow = snake[-1] == food

    if grow:
        food = (10*random.randint(0, 59), 10*random.randint(0, 59))

    move(direction, grow=grow)


    
    if snake[-1][0] < -20 or snake[-1][0] > 610 or snake[-1][1] < -20 or snake[-1][1] > 610 or snake[-1] in snake[:-1]:
        running = False
        pg.time.delay(2000)
        print("Game Over")
        print("Score: " + str(len(snake) - 3))


    pg.display.flip()





    
pg.quit()