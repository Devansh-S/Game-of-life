
# coding: utf-8

# In[1]:


import numpy as np
import random
import turtle
import argparse


scr=turtle.Screen()
turtle.setup(500,500)
turtle.title("Game of Life")
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(0,0)

lifeturtle = turtle.Turtle()
lifeturtle.up()
lifeturtle.hideturtle()
lifeturtle.speed(0)
lifeturtle.color('black')
    
def draw_grid(size):
    turtle.pencolor('grey')
    turtle.pensize(2)
    x = -200
    for i in range(size+1):
        turtle.up()
        turtle.goto(x,-200)
        turtle.down()
        turtle.goto(x,200)
        x += 400/size
    y = -200
    for i in range(size+1):
        turtle.up()
        turtle.goto(-200,y)
        turtle.down()
        turtle.goto(200,y)
        y += 400/size

def square(x, y, size_block):
    lifeturtle.up()
    lifeturtle.goto(x,y)
    lifeturtle.down()
    lifeturtle.seth(0)
    lifeturtle.begin_fill()
    for i in range(4):
        lifeturtle.fd(size_block)
        lifeturtle.left(90)
    lifeturtle.end_fill()

def draw_species(size):
    for i in range(size):
        for j in range(size):
            if board[i][j] == 1:
                px = 400/size*i - 200
                py = 400/size*j - 200
                square(px+1,py+1,400/size-2)

           
def update_life(size):

    neighbors = 0
    for x in range(0,size):
        for y in range(0,size):
            neighbors = 0
            neighbors = int((board[x, (y-1)%size] +
                         board[x, (y+1)%size] + 
                         board[(x-1)%size, y] +
                         board[(x+1)%size, y] + 
                         board[(x-1)%size, (y-1)%size] +
                         board[(x-1)%size, (y+1)%size] + 
                         board[(x+1)%size, (y-1)%size] +
                         board[(x+1)%size, (y+1)%size]))
                
            if ((board[x][y] == 1) and (neighbors <  2)):
                temp_board[x][y] = 0
            elif ((board[x][y] == 1) and (neighbors >  3)):
                temp_board[x][y] = 0           
            elif ((board[x][y] == 0) and (neighbors == 3)):
                temp_board[x][y] = 1
            else:
                temp_board[x][y] = board[x][y]

    board[:] = temp_board[:]

def main(refresh_rate=200, size=40):

    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.") 
  
    parser.add_argument('--board_size', dest='size', required=False) 
    parser.add_argument('--refresh_rate', dest='refresh_rate', required=False) 

    args = parser.parse_args() 
      
    size = 50
    if args.size and int(args.size) > 8: 
        size = int(args.size)

    global board
    global temp_board

    temp_board = np.random.randint(2, size=(size,size))
    board = np.random.randint(2, size=(size,size))
      
    refresh_rate = 200
    if args.refresh_rate: 
        refresh_rate = int(args.refresh_rate)  

    while(True):
        draw_grid(size)
        update_life(size)
        lifeturtle.clear()
        draw_species(size)
        scr.update() 
        scr.ontimer(update_life(size),refresh_rate) 


if __name__ == '__main__': 
    main()
