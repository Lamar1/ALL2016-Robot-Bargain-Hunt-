from tkinter import *
import tkinter as tk
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


        def labels(self):
            '''Create and place labels'''
            basketLabel = Label(self.frameBasket, text="Basket", background="white", fg="mediumblue")
            basketLabel.place(anchor="c", relx=0.5, rely=0.06)

            phLabel = Label(self.framePlaceholder, text="PLACEHOLDER", background="white", fg="mediumblue")
            phLabel.place(anchor="c", relx=0.5, rely=0.08)

            timerLabel = Label(self.frameTimer, text="Timer", background="white", fg="mediumblue")
            timerLabel.place(anchor="c", relx=0.5, rely=0.14)
            
        global _duration 
        #global _duration allows the timer to recieve the timer information stored in clockInput.  1 minute is the placeholder value 
        def count_down(duration):
            if duration is None:
                _duration = 60
            for t in range(_duration, -1, -1):
        # formats duration as 2 digit integers 00:00
        # divmod() converts the seconds to minutes, seconds
            sf = "{:02d}:{:02d}".format(*divmod(t, 60))
            time_str.set(sf)
            root.update()
        #delays number changing for 1 second 
            time.sleep(1)
        
        #Creates the related timer buttons & adds them to 'frameTimer',_Button1-3 is the duration selected in seconds
        _button1 = Button(frameTimer, text='1 minute', command= lambda a=60: clockInput(a))
        _button2 = Button(frameTimer, text='2 minutes', command= lambda b=120: clockInput(b))
        _button3 = Button(frameTimer, text='4 minutes', command= lambda c=240: clockInput(c))
        _button4 = Button(frameTimer, text='Start', command = lambda: count_down(_duration))
            
        _button1.pack(side=LEFT,fill=BOTH,expand=True)
        _button2.pack(side=LEFT,fill=BOTH,expand=True)
        _button3.pack(side=LEFT,fill=BOTH,expand=True)
        _button4.pack(side=LEFT,fill=BOTH,expand=True)
       
        
        def clockInput(Length):
            '''Saves the duration selected by a timer button'''
                _duration = Length
                
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
