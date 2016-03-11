
from tkinter import *
import tkinter as tk
from tkinter import Tk, Button,ttk
import time
from expanded_basket import ExpandedBasket
from sortingclass import SortAlgorithms
from random import randint
import random
import sqlite3 as sql
global tree
global algorithm
algorithm = 0
#DELETE TABLE EXAMPLE '_List4Table BEFORE FINAL IMPLEMENTATION
#CALL TreeviewItemTable() AFTER ITEM COLLECTION



'''
[TODO]
*Implement timer
*Fill framePlaceholder
[NOTES]
Must include the resource file 'arrows.gif' and expanded_basket.py in the same directory to run correctly.


'''

class MainInterface:
    
    def __init__(self, root):
        '''Basic window setup'''
        self.root = root
        self.top = Toplevel()
        self.top.title("Collected items")
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.wm_title("Python ALL Project")
        self.root.config(background = "#FFFFFF")
        self.root.geometry("1025x800")
        self.time_str = StringVar()
        
        self.tree = ttk.Treeview(self.top)

        self.SC = SortAlgorithms()
    

        def frames(self):
            '''Create and place frames'''
            self.frameMenu = Frame(self.root, width=225, height = 600, background="royalblue")
            self.frameMenu.grid(row=0, column=1, padx=0, pady=0, sticky="nes")

            self.framePlaceholder = Frame(self.root, width=200, height = 200, background="white")
            self.framePlaceholder.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.46)

            self.frameGame = Frame(self.root, width=900, height = 800, background="white")
            self.frameGame.grid(row=0, column=0, padx=0, pady=0, sticky="wnes" )

            self.frameTimer = Frame(self.root, width=200, height = 100, background="white")
            self.frameTimer.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.25)

            self.frameSelect = Frame(self.root, width=200, height=200, background="white")
            self.frameSelect.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.730)

            self.lineframe2 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe2.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.371)

            self.lineframe3 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe3.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.222)

            self.lineframe4 = Frame(self.root, width=200, height=1, background="lightgrey")
            self.lineframe4.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.64)


        def buttons(self):
            '''Create and place buttons'''
            self.distributeButton = Button(self.frameMenu, text="Distribute items", command = lambda: distributeItems(), background="royalblue", fg="white")
            self.distributeButton.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.100)

            self.button1 = Button(self.framePlaceholder, text="v", background="white", fg="black", command = lambda: sortName())
            self.button1.place(anchor="c", relx=0.585, rely=0.3)

            self.button2 = Button(self.framePlaceholder, text="v", background="white", fg="black", command = lambda: sortPrice())
            self.button2.place(anchor="c", relx=0.585, rely=0.5)

            self.button3 = Button(self.framePlaceholder, text="v", background="white", fg="black", command = lambda: sortQuantity())
            self.button3.place(anchor="c", relx=0.585, rely=0.7)


            def sel():
               print("You selected the option " + str(var.get()))
               algorithm = str(var.get())
               algo(algorithm)

            var = IntVar()
            R1 = Radiobutton(self.frameSelect, text="Quick sort", variable=var, value=1,
                  command=sel, background="white")
            R1.place(anchor="c", relx=0.220, rely=0.35)

            R1.invoke()

            R2 = Radiobutton(self.frameSelect, text="Bubble sort", variable=var, value=2,
                  command=sel, background="white")
            R2.place(anchor="c", relx=0.23, rely=0.55)

            R3 = Radiobutton(self.frameSelect, text="Insertion sort", variable=var, value=3,
                  command=sel, background="white")
            R3.place(anchor="c", relx=0.25, rely=0.75)

            
            #Creates the related timer buttons & adds them to 'frameTimer',_Button1-3 is the duration selected in seconds
            self._button1 = Button(self.frameTimer, text='1 minute', command= lambda a=60: timerHandler(a))
            self._button2 = Button(self.frameTimer, text='2 minutes', command= lambda b=120: timerHandler(b))
            self._button3 = Button(self.frameTimer, text='4 minutes', command= lambda c=240: timerHandler(c))
            
            self._button1.place(anchor="c", relx=0.15, rely=0.87)
            self._button2.place(anchor="c", relx=0.50, rely=0.87)
            self._button3.place(anchor="c", relx=0.85, rely=0.87)


        def algo(algo):
            print (algo)
            global algorithm
            algorithm = algo
            

        def labels(self):
            '''Create and place labels'''

            phLabel = Label(self.framePlaceholder, text="Sorting options", background="white", fg="mediumblue")
            phLabel.place(anchor="c", relx=0.5, rely=0.08)

            timerLabel = Label(self.frameTimer, text="Timer", background="white", fg="mediumblue")
            timerLabel.place(anchor="c", relx=0.5, rely=0.14)

            self.timerActiveLabel = Label(self.frameTimer, text="Select time", background="white", fg="mediumblue")
            self.timerActiveLabel.place(anchor="c", relx=0.5, rely=0.40)

            self.productLabel = Label(self.framePlaceholder, text="Product Name", background="white", fg="mediumblue")
            self.productLabel.place(anchor="c", relx=0.230, rely=0.3)

            self.priceLabel = Label(self.framePlaceholder, text="Price", background="white", fg="mediumblue")
            self.priceLabel.place(anchor="c", relx=0.100, rely=0.5)

            self.quantityLabel = Label(self.framePlaceholder, text="Quantity", background="white", fg="mediumblue")
            self.quantityLabel.place(anchor="c", relx=0.150, rely=0.7)

            self.sortingLabel = Label(self.frameSelect, text="Sorting algorithms", background="white", fg="mediumblue")
            self.sortingLabel.place(anchor="c", relx=0.475, rely=0.07)

            
        def map(self):
            self.canvas = Canvas(self.frameGame,width = 800, height = 800, bg = 'black')
            self.canvas.pack(expand = YES, fill = BOTH)
            self.map = PhotoImage(file = 'map.png')
            self.canvas.create_image(0, 0, image = self.map, anchor = NW)
            

        def timerHandler(duration):
            self.duration = duration
            self.timerActiveLabel['text'] = duration // 60, "Minutes"
            
                
        def distributeItems():
            '''TODO: Randomly places items within map & start timer'''
            sys.stdout.write("Distribute pressed \n")

            self.item = PhotoImage(file = 'item.png')
            tup = ((105,105),(105,130),(105, 155),(105, 180),(130, 105),(155, 105),(180, 105),(180, 130),(180, 155)
                   ,(180, 180),(155, 180),(130, 180),(105, 265),(105, 290),(105, 315),(105, 340),(130, 340)
                   ,(155, 340),(180, 340),(180, 290),(180, 265),(180, 315),(155, 265),(130, 265),(105, 425)
                   ,(105, 450),(105, 475),(105, 500),(130, 425),(155, 425),(180, 425),(180, 450),(180, 475)
                   ,(180, 500),(155, 500),(130, 500),(135, 650),(135, 675),(135, 700),(135, 725),(160, 650)
                   ,(185, 650),(210, 650),(210, 675),(210, 700),(210, 725),(185, 725),(160, 725),(650, 50)
                   ,(675, 50),(700, 50),(725, 50),(750, 75),(750, 100),(750, 125),(750, 150),(586, 200)
                   ,(611, 200),(636, 200),(661, 200),(586, 246),(611, 246),(636, 246),(661, 246),(586, 360)
                   ,(611, 360),(636,360),(661,360),(686,360),(586, 406),(611, 406),(636, 406),(661, 406)
                   ,(686, 406),(586, 490),(611, 490),(636, 490),(661, 490),(686, 490),(586, 536),(611, 536)
                   ,(636, 536),(661, 536),(686, 536),(520, 650),(520, 675),(520, 700),(520, 725),(565, 650)
                   ,(565, 675),(565, 700),(565, 725),(650, 650),(650, 675),(650, 700),(650, 725),(695, 650)
                   ,(695, 675),(695, 700),(695, 725))

            track = []
            for x in range (20):
                rnd = randint(0,99)
                if rnd in track:
                    while rnd in track:
                        rnd = randint(0,99)
                    track.insert(x,rnd)
                    self.canvas.create_image(tup[rnd], image = self.item)
                    
                else:
                    track.insert(x,rnd)
                    self.canvas.create_image(tup[rnd], image = self.item)

            randomitem()
            

        def sortName():
            '''TODO: Sorting code'''
            sys.stdout.write("Name sort pressed \n")

            if self.button1["text"]=="v":
                self.button1["text"] = "^"
                #Sort descending

                if algorithm == "1":
                    print ("Quick sort (descending)")
                    #self.SC.quickSortReverse()


                    #Function to sort a list into  reverse alphabetical/numerical order using Quick Sort algorithm
                    tree.delete(*tree.get_children())
                    lessThan = []
                    equalTo = []
                    greaterThan = []
                    if len(_List4Table) > 1:
                        pivot = _List4Table[0]
                        for i in range(len(_List4Table)):
                            if _List4Table[i] < pivot:
                                lessThan.append(_List4Table[i])
                            elif _List4Table[i] > pivot:
                                greaterThan.append(_List4Table[i])
                            else:
                                equalTo.append(_List4Table[i])
                        return quickSortReverse(greaterThan) + equalTo + quickSortReverse(lessThan)
                    else:
                        return _List4Table


                    

                elif algorithm == "2":
                    print ("Bubble sort (descending)")

                elif algorithm == "3":
                    print ("Insertion sort (descending)")
                
            elif self.button1["text"]=="^":
                self.button1["text"]="v"
                #Sort ascending

                if algorithm == "1":
                    print ("Quick sort (ascending)")

                elif algorithm == "2":
                    print ("Bubble sort (ascending)")

                elif algorithm == "3":
                    print ("Insertion sort (ascending)")
                    

        def sortPrice():
            '''TODO: Sorting code'''
            sys.stdout.write("Price sort pressed \n")

            if self.button2["text"]=="v":
                self.button2["text"] = "^"
                #Sort descending

                if algorithm == "1":
                    print ("Quick sort (descending)")

                elif algorithm == "2":
                    print ("Bubble sort (descending)")

                elif algorithm == "3":
                    print ("Insertion sort (descending)")

                
            elif self.button2["text"]=="^":
                self.button2["text"]="v"
                #Sort ascending

                if algorithm == "1":
                    print ("Quick sort (ascending)")

                elif algorithm == "2":
                    print ("Bubble sort (ascending)")

                elif algorithm == "3":
                    print ("Insertion sort (ascending)")
                

        def sortQuantity():
            '''TODO: Sorting code'''
            sys.stdout.write("Quantity sort pressed \n")

            if self.button3["text"]=="v":
                self.button3["text"] = "^"
                #Sort descending

                if algorithm == "1":
                    print ("Quick sort (descending)")

                elif algorithm == "2":
                    print ("Bubble sort (descending)")

                elif algorithm == "3":
                    print ("Insertion sort (descending)")

                
            elif self.button3["text"]=="^":
                self.button3["text"]="v"
                #Sort ascending

                if algorithm == "1":
                    print ("Quick sort (ascending)")

                elif algorithm == "2":
                    print ("Bubble sort (ascending)")

                elif algorithm == "3":
                    print ("Insertion sort (ascending)")
                
            
        def itemCollection():
            EB = ExpandedBasket.TreeviewItemTable()
            EB.TreeviewItemTable()

        def randomitem():
            try:
                #connects to the item database
                con = sql.connect('ITEM DATABASE.sqlite')
                cur = con.cursor()
                #selects 9 random products from items table in database
                cur.execute(''' SELECT product FROM items ORDER BY
                                RANDOM() LIMIT 9;''')
                ItemList = []
                #Creates a list of these items and prints the items selected to screen 
                for row in cur:
                    ItemList.append(row)
                    print(row)
                #Creates global _list1 to create another list from ItemList (to remove the tuple)    
                global _list1
                _list1 = [val for sublist in ItemList for val in sublist]
                #closes database connection in any circumstance
            finally:
                    con.close()
                #calls function and prints converted list


        def table(self):
            self.tree["columns"]=("Price","Quantity","Category")
            self.tree.column("Price", width=200 )
            self.tree.column("Quantity", width=200)
            self.tree.column("Category", width=200)
            self.tree.heading("Price", text=" Price")
            self.tree.heading("Quantity", text=" Quantity")
            self.tree.heading("Category", text=" Category")

            global _List4Table
            

        def TreeviewItemTable():

        #Example table
            _List4Table =['Grapes','Salmon','Bacon','Wine','Celery','Duck']
                
        #for loop iterates over all items contained in _List4Table 
        #_List4Table contains items collected in game 
            for prodname in _List4Table:
                try:
                #Connects to the item database 
                    ItemList1= []
                    con= sql.connect('ITEM DATABASE.sqlite')
                    cur = con.cursor()
                    #finds the relevant information for product in _List4Table
                    cur.execute('''SELECT Price,Quantity,"Category " FROM items
                                   WHERE Product = ?;''', (prodname,))
                    #Appends Price, Quantity & Category to ItemList1              
                    for row in cur:
                        ItemList1.append(row)
                        print(row)
                        #creates _ItemList from ItemList1 (removing any tuples)
                        global _ItemList
                        _ItemList = [val for sublist in ItemList1 for val in sublist]
                        #Appends at the end of the tree with Price, Quantity & Category in the relevant column
                        self.tree.insert("" , "end", text= prodname, values=(_ItemList[0],_ItemList[1],_ItemList[2]))
                finally:
                    #Closes database connection in any circumstance
                    con.close()
            
        frames(self)
        buttons(self)
        labels(self)
        map(self)
        table(self)
        self.tree.pack()
        
        
def main():
    root = Tk()
    mainInterface = MainInterface(root)
    root.mainloop()

if __name__ == '__main__':
        sys.exit(main())
