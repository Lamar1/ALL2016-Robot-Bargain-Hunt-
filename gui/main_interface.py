from tkinter import *
import tkinter as tk
import time
from expanded_basket import ExpandedBasket

'''
[TODO]
*Implement timer
*Fill framePlaceholder
[NOTES]
Must include the resource file 'arrows.gif' and expanded_basket.py in the same directory to run correctly
'''

class MainInterface:
    
    def __init__(self, root):
        '''Basic window setup'''
        self.root = root
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.wm_title("Python ALL Project")
        self.root.config(background = "#FFFFFF")
        self.root.geometry("1125x800")
        self.time_str = StringVar()
        


        def frames(self):
            '''Create and place frames'''
            self.frameMenu = Frame(self.root, width=225, height = 600, background="royalblue")
            self.frameMenu.grid(row=0, column=1, padx=0, pady=0, sticky="nes")

            self.frameBasket = Frame(self.root, width=200, height = 300, background="white")
            self.frameBasket.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.795)

            self.framePlaceholder = Frame(self.root, width=200, height = 200, background="white")
            self.framePlaceholder.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.46)

            self.frameGame = Frame(self.root, width=900, height = 800, background="white")
            self.frameGame.grid(row=0, column=0, padx=0, pady=0, sticky="wnes" )

            self.frameTimer = Frame(self.root, width=200, height = 100, background="white")
            self.frameTimer.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.25)

            self.lineframe1 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe1.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.65)

            self.lineframe2 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe2.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.371)

            self.lineframe3 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe3.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.222)
      

        def buttons(self):
            '''Create and place buttons'''
            self.distributeButton = Button(self.frameMenu, text="Distribute items", command = lambda: distributeItems(), background="royalblue", fg="white")
            self.distributeButton.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.100)

            self.image = tk.PhotoImage(file="arrows.gif")
            self.expandButton = Button(self.frameBasket, image=self.image, background="white", command = lambda: expandedBasket())
            self.expandButton.place(anchor="c", relx=0.9, rely=0.06)
            
            #Creates the related timer buttons & adds them to 'frameTimer',_Button1-3 is the duration selected in seconds
            self._button1 = Button(self.frameTimer, text='1 minute', command= lambda a=60: timerHandler(a))
            self._button2 = Button(self.frameTimer, text='2 minutes', command= lambda b=120: timerHandler(b))
            self._button3 = Button(self.frameTimer, text='4 minutes', command= lambda c=240: timerHandler(c))
            
            self._button1.place(anchor="c", relx=0.15, rely=0.87)
            self._button2.place(anchor="c", relx=0.50, rely=0.87)
            self._button3.place(anchor="c", relx=0.85, rely=0.87)
             

        def labels(self):
            '''Create and place labels'''
            basketLabel = Label(self.frameBasket, text="Basket", background="white", fg="mediumblue")
            basketLabel.place(anchor="c", relx=0.5, rely=0.06)

            phLabel = Label(self.framePlaceholder, text="PLACEHOLDER", background="white", fg="mediumblue")
            phLabel.place(anchor="c", relx=0.5, rely=0.08)

            timerLabel = Label(self.frameTimer, text="Timer", background="white", fg="mediumblue")
            timerLabel.place(anchor="c", relx=0.5, rely=0.14)

            self.timerActiveLabel = Label(self.frameTimer, text="UPDATE", background="white", fg="mediumblue")
            self.timerActiveLabel.place(anchor="c", relx=0.5, rely=0.40)

        def timerHandler(duration):
            self.duration = duration
            
                
        def distributeItems():
            '''TODO: Randomly places items within map & start timer'''
            sys.stdout.write("Distribute pressed \n")
            

        def expandedBasket():
            '''Launches expanded basket'''
            sys.stdout.write("Expand pressed \n")
            self.frameMenu.destroy()
            self.frameGame.destroy()
            EB = ExpandedBasket(root)
            
        frames(self)
        buttons(self)
        labels(self)


def main():
    root = Tk()
    mainInterface = MainInterface(root)
    root.mainloop()

if __name__ == '__main__':
        sys.exit(main())
