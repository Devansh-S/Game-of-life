
# coding: utf-8

# In[1]:


import numpy as np
import random
import turtle


class draw_game():
    def __init__(self, size):
        self.size = size
 
        scr=turtle.Screen()
        turtle.setup(1000,1000)
        turtle.title("Game of Life")
        turtle.hideturtle()
        turtle.speed(0)
        turtle.tracer(0,0)

        lifeturtle = turtle.Turtle()
        lifeturtle.up()
        lifeturtle.hideturtle()
        lifeturtle.speed(0)
        lifeturtle.color('black')

    def draw_line(x1,y1,x2,y2):
        turtle.up()
        turtle.goto(x1,y1)
        turtle.down()
        turtle.goto(x2,y2)
        
    def draw_grid(size): 
        turtle.pencolor('gray')
        turtle.pensize(3)
        x = -400
        for i in range(self.size+1):
            draw_line(x,-400,x,400)
            x += 800/self.size
        y = -400
        for i in range(self.size+1):
            draw_line(-400,y,400,y)
            y += 800/size

    def square(x,y,size_block):
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
        global board
        for i in range(self.size):
            for j in range(self.size):
                if board[i][j] == 1:
                    lx = 800/self.size*i - 400
                    ly = 800/self.size*j - 400
                    square(lx+1,ly+1,800/self.size-2)
                    
    def draw_board(x_size, y_size):
        board = np.zeros((x_size, y_size))
        for x in range(x_size):
            for y in range(y_size):
                board[x][y] = int(random.randrange(2));
        return board

           
    def update_life(size): 
        global board 
        neighbors = 0
        board1 = draw_board(self.size,self.size)
        for x in range(0,self.size):
            for y in range(0,self.size):
                neighbors = 0
                neighbors = int((board[x, (y-1)%self.size] +
                             board[x, (y+1)%self.size] + 
                             board[(x-1)%self.size, y] +
                             board[(x+1)%self.size, y] + 
                             board[(x-1)%self.size, (y-1)%self.size] +
                             board[(x-1)%self.size, (y+1)%self.size] + 
                             board[(x+1)%self.size, (y-1)%self.size] +
                             board[(x+1)%self.size, (y+1)%self.size]))
                
                if ((board[x][y] == 1) and (neighbors <  2)):
                    board1[x][y] = 0
                elif ((board[x][y] == 1) and (neighbors >  3)):
                    board1[x][y] = 0           
                elif ((board[x][y] == 0) and (neighbors == 3)):
                    board1[x][y] = 1
                else:
                    board1[x][y] = board[x][y]

        board[:] = board1[:]
        lifeturtle.clear()
        draw_species(self.size)
        scr.update() 
        scr.ontimer(update_life(self.size),200) 


    def game(size):
        init()
        global board   
        board = draw_board(self.size,self.size)
        while(True):
            draw_grid(self.size)
            update_life(self.size)

