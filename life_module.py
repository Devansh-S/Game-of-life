
# coding: utf-8

# In[1]:


import numpy as np
import random
import turtle
import argparse

class gol:
    def __init__(self):
        self.size = 40
        
    def draw_grid(self, size):

        turtle.pencolor('grey')
        turtle.pensize(3)
        x = -400
        for i in range(self.size+1):
            turtle.up()
            turtle.goto(x,-400)
            turtle.down()
            turtle.goto(x,400)
            x += 800/self.size
        y = -400
        for i in range(self.size+1):
            turtle.up()
            turtle.goto(-400,y)
            turtle.down()
            turtle.goto(400,y)
            y += 800/self.size

    def square(self, x, y, size_block):
        self.lifeturtle.up()
        self.lifeturtle.goto(x,y)
        self.lifeturtle.down()
        self.lifeturtle.seth(0)
        self.lifeturtle.begin_fill()
        for i in range(4):
            self.lifeturtle.fd(size_block)
            self.lifeturtle.left(90)
        self.lifeturtle.end_fill()

    def draw_species(self,size):
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    lx = 800/self.size*i - 400
                    ly = 800/self.size*j - 400
                    self.square(lx+1,ly+1,800/self.size-2)

           
    def update_life(self,size): 
        neighbors = 0
        for x in range(0,size):
            for y in range(0,size):
                neighbors = 0
                neighbors = int((self.board[x, (y-1)%self.size] +
                             self.board[x, (y+1)%self.size] + 
                             self.board[(x-1)%self.size, y] +
                             self.board[(x+1)%self.size, y] + 
                             self.board[(x-1)%self.size, (y-1)%self.size] +
                             self.board[(x-1)%self.size, (y+1)%self.size] + 
                             self.board[(x+1)%self.size, (y-1)%self.size] +
                             self.board[(x+1)%self.size, (y+1)%self.size]))
                
                if ((self.board[x][y] == 1) and (neighbors <  2)):
                    self.temp_board[x][y] = 0
                elif ((self.board[x][y] == 1) and (neighbors >  3)):
                    self.temp_board[x][y] = 0           
                elif ((self.board[x][y] == 0) and (neighbors == 3)):
                    self.temp_board[x][y] = 1
                else:
                    self.temp_board[x][y] = self.board[x][y]

        self.board[:] = self.temp_board[:]

    def game(self, refresh_rate=200, size=40):

        self.size = size
        self.board = np.random.randint(2, size=(self.size,self.size))
        self.temp_board = np.random.randint(2, size=(self.size,self.size))
        
        self.scr=turtle.Screen()
        turtle.setup(1000,1000)
        turtle.title("Game of Life")
        turtle.hideturtle()
        turtle.speed(0)
        turtle.tracer(0,0)

        self.lifeturtle = turtle.Turtle()
        self.lifeturtle.up()
        self.lifeturtle.hideturtle()
        self.lifeturtle.speed(0)
        self.lifeturtle.color('black')

        while(True):
            self.draw_grid(self.size)
            self.update_life(self.size)
            self.lifeturtle.clear()
            self.draw_species(self.size)
            self.scr.update() 
            self.scr.ontimer(self.update_life(self.size),refresh_rate) 


