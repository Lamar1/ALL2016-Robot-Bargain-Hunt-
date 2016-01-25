__author__ = 'Callum'
from tkinter import *
#Function to get robot to move left in response to left arrow key press by taking coordinates and
#moving the robot 5 pixels to left (-20 pixels)
def leftKey(event):
    print ("Left key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1-20,y1,x2-20,y2)
#Function to get robot to move right in response to left arrow key press by taking coordinates
#and moving the robot 5 pixels to right (+20 pixels)
def rightKey(event):
    print ("Right key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1+20,y1,x2+20,y2)
def upKey(event):
    print ("Up key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1-20,x2,y2-20)
def downKey(event):
    print ("Down key pressed")
    x1,y1,x2,y2=canvas.coords(id1)
    canvas.coords(id1,x1,y1+20,x2,y2+20)
main = Tk()
canvas = Canvas(main, width=300, height=300)
canvas.pack()
id1=canvas.create_rectangle(120,120,100, 100, width=2)
canvas.bind('<Left>', leftKey)
canvas.bind('<Right>', rightKey)
canvas.bind('<Up>', upKey)
canvas.bind('<Down>', downKey)
canvas.focus_set()
main.mainloop()
