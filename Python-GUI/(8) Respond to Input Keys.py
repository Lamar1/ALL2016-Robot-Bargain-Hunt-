from Tkinter import *
main = Tk()
#Function to print “Left key pressed” if left arrow pressed
def leftKey(event):
    print ("Left key pressed")
#Function to print “Right key pressed” if right arrow pressed
def rightKey(event):
    print ("Right key pressed")
canvas = Canvas(main, width=100, height=100)
canvas.pack()
#Recognise keys in keyboard
canvas.bind('<Left>', leftKey)
canvas.bind('<Right>', rightKey)
# Create focus for keyboard
canvas.focus_set()
main.mainloop()
