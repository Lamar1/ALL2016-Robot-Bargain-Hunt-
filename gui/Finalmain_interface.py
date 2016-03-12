
from tkinter import *
import tkinter as tk
from tkinter import Tk, Button,ttk
import time
from expanded_basket import ExpandedBasket
from sortingclass import SortAlgorithms
from random import randint
import random
import sqlite3 as sql
from collections import defaultdict, deque
from sys import argv


global _List4Table, _ProdPrice
_ProdPrice=[]
_List4Table=[]
global algorithm
global tree
global list1
list1= []
algorithm = 0

'''
[NOTES]
Must include the resource file 'arrows.gif' and expanded_basket.py in the same directory to run correctly.
'''

class MainInterface:
    
    def __init__(self, root):
        '''Basic window setup'''
        self.root = root
        self.top = Toplevel()
        self.top.title("Collected items")
        #Prevents window from being resized
        self.root.resizable(width=FALSE, height=FALSE)
        #Sets window title
        self.root.wm_title("Python ALL Project")
        #Sets window background to white
        self.root.config(background = "#FFFFFF")
        #Sets the window size
        self.root.geometry("1025x800")
        self.time_str = StringVar()
        #self.tree = ttk.Treeview(self.top)
        self.SC = SortAlgorithms()
        tree = ttk.Treeview(self.top)

        '''Setting up the Invidual Frames and Windows''''''RYAN'''
        def frames(self):
            '''Create and place frames'''
            #Frame to hold right menu 
            self.frameMenu = Frame(self.root, width=225, height = 600, background="royalblue")
            self.frameMenu.grid(row=0, column=1, padx=0, pady=0, sticky="nes")
            
            #Frame that holds sorting options
            self.framePlaceholder = Frame(self.root, width=200, height = 200, background="white")
            self.framePlaceholder.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.46)
            
            #Frame in which the game is displayed
            self.frameGame = Frame(self.root, width=900, height = 800, background="white")
            self.frameGame.grid(row=0, column=0, padx=0, pady=0, sticky="wnes" )
            
            #Frame to hold timer
            self.frameTimer = Frame(self.root, width=200, height = 100, background="white")
            self.frameTimer.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.25)
            
            #Frame that holds the radio buttons that allow the user to choose which sorting algorithm to use
            self.frameSelect = Frame(self.root, width=200, height=200, background="white")
            self.frameSelect.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.730)
            
            #Futher frames are used for decorational purposes only
            self.lineframe2 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe2.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.371)

            self.lineframe3 = Frame(self.root, width=200, height = 1, background="lightgrey")
            self.lineframe3.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.222)

            self.lineframe4 = Frame(self.root, width=200, height=1, background="lightgrey")
            self.lineframe4.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.64)

        '''Setting up of the Main Buttons in the gui''''''RYAN'''#and also includes sel def
        def buttons(self):
            '''Create and place buttons'''
            self.distributeButton = Button(self.frameMenu, text="Distribute items", command = lambda: distributeItems(), background="royalblue", fg="white")
            self.distributeButton.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.100)

            self.basketButton = Button(self.frameMenu, text="Basket View", command = lambda: distributeItems(), background="royalblue", fg="white")
            self.basketButton.place(in_=self.frameMenu, anchor="c", relx=0.5, rely=0.135)
            
            #Button that allows user to sort by name
            self.button1 = Button(self.framePlaceholder, text="v", background="white", fg="black", command = lambda: sortName())
            self.button1.place(anchor="c", relx=0.585, rely=0.3)

            #Button that allows user to sort by price
            self.button2 = Button(self.framePlaceholder, text="v", background="white", fg="black", command = lambda: sortPrice())
            self.button2.place(anchor="c", relx=0.585, rely=0.5)

            #Button that allows user to sort by quantity
            self.button3 = Button(self.framePlaceholder, text="v", background="white", fg="black", command = lambda: sortQuantity())
            self.button3.place(anchor="c", relx=0.585, rely=0.7)

            #Creates the related timer buttons & adds them to 'frameTimer',_Button1-3 is the duration selected in seconds
            self._button1 = Button(self.frameTimer, text='1 minute', command= lambda a=60: timerHandler(a))
            self._button2 = Button(self.frameTimer, text='2 minutes', command= lambda b=120: timerHandler(b))
            self._button3 = Button(self.frameTimer, text='4 minutes', command= lambda c=240: timerHandler(c))
            self._button1.place(anchor="c", relx=0.15, rely=0.87)
            self._button2.place(anchor="c", relx=0.50, rely=0.87)
            self._button3.place(anchor="c", relx=0.85, rely=0.87)

            def sel():
                #Called to modify the global variable 'algorithm'
                print("You selected the option " + str(var.get()))
                algorithm = str(var.get())
                algo(algorithm)

            var = IntVar()
            #A series of radio buttons that allow the user to select different sorting algoirthms
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

        def algo(algo):
            '''Used to modify the global variable 'algorithm''''
            print (algo)
            global algorithm
            algorithm = algo


        '''Setting up of the Main Labels and also includes the search box'''
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

            '''Search Box'''
            search_input = argv

            """FUNCTIONS"""

            """Function to look for items in list"""
            def find_items (_list4table):
                for i in _list4table: #Needs to be amended to the correct list box
                    searchresults.insert(END, search_input)

            """SCREENS"""

            """Screen for the search bar, to be later implemented into the expanded basket view"""
            root = Tk()
            root.title("Item Searcher")
            root.geometry('200x200')
            root.resizable(width=FALSE, height=FALSE)

            """FRAMES"""

            """Frame to hold: Search box, search button and quit button"""
            controlFrame = ttk.Frame(root, height=100, width=200)
            controlFrame.pack()

            """Frame to show search results of find"""
            resultsframe = ttk.Frame(root, height=00, width=200)
            resultsframe.pack()

            """BUTTONS AND BOXES"""

            """Search Box"""
            entry = Entry(controlFrame, width=30)
            entry.pack()

            """Listbox for listing all results of the find"""
            searchresults = Listbox(resultsframe, height=100, width=200)
            searchresults.pack(fill=BOTH, expand=YES)

            """Search button to intiate find_items"""
            searchbutton = ttk.Button(controlFrame, text="Search",command = lambda: linearSearch(self))
            searchbutton.pack()


            """Quit button to exit the application"""
            quitButton = ttk.Button(controlFrame, text="Quit")
            quitButton.pack()
            quitButton.bind ('<ButtonPress>', lambda e: exit())

            '''Search Algorithm'''
            def __init__(self):
                self.foundItem = False
                self.pos = 0

            def linearSearch(self):
                for i in range(0,len(myItem, _List4Table)):
                    if _List4Table[i] == myItem:
                        self.foundItem = True
                        self.pos = self.pos + 1
                        return ("Item Found")
                else:
                    return ("Item Not Found")

            def reset(self):
                self.foundItem = False
                self.pos = 0

        '''A function to retrieve SQL database information and convert to a list removing any tuples''''''LAMAR'''
        def randomitem():
            try:
                #connects to the item database
                con = sql.connect('ITEM DATABASE.sqlite')
                cur = con.cursor()
                #selects 9 random products from items table in database
                cur.execute(''' SELECT product,Price FROM items ORDER BY
                                RANDOM() LIMIT 22;''')
                ItemList = []
                #Creates a list of these items and prints the items selected to screen
                for row in cur:
                    ItemList.append(row)
                #Creates global _list1 to create another list from ItemList (to remove the tuple)
                global _list1
                #_list1 = [val for sublist in ItemList for val in sublist]
                _list1 = []
                _list1 = ItemList
            #closes database connection in any circumstance
            finally:
                    con.close()

        '''Calls function and prints converted list''''''LAMAR'''
        def RandomItemToTable():
            #Creates _List4Table (contains product names that will be added to treeview basket) _ProdPrice adds price to treeview
            #Creates ConversionList with a random entry from _list1
            ConversionList= random.choice(_list1)
            #Creates a list with just the product name through slicing
            _ConversionList1 = str(ConversionList[0])
            #Creates a list with just the product price through slicing
            _ConversionList2 = str(ConversionList[1])
            print(ConversionList)
            #Adds the product name to _List4Table
            _List4Table.append(_ConversionList1)
            #Adds the product price to _ProdPrice
            _ProdPrice.append(_ConversionList2)
            #Deletes the ConversionList,_ConversionList1
            del ConversionList,_ConversionList1,_ConversionList2
            #Prints the contents of _List4Table to IDLE
            print(_List4Table)

        '''Creates map, creates obstacles, sets up controls for user input''''''CALLUM'''
        def map(self):
            self.canvas = Canvas(self.frameGame,width = 800, height = 800, bg = 'black')
            self.canvas.pack(expand = YES, fill = BOTH)
            self.map = PhotoImage(file = 'map.png')
            self.canvas.create_image(0, 0, image = self.map, anchor = NW)

            '''Below sets out the item locations areas and the walls to the maze'''
            ###ITEM HOLDER BOXES
            itemHolder = self.canvas.create_rectangle(735, 0, 768, 161, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(639, 32, 736, 65, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 192, 673, 257, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 352, 705, 417, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 352, 705, 417, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(575, 480, 705, 545, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(639, 640, 705, 737, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(511, 640, 577, 737, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(95, 96, 193, 193, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(95, 256, 193, 353, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(95, 416, 193, 513, fill='', width=0)
            itemHolder = self.canvas.create_rectangle(127, 640, 225, 737, fill='', width=0)

            #EXTERIOR WALLS
            walls = self.canvas.create_rectangle(0, 0, 33, 801, fill='', width=0)
            walls = self.canvas.create_rectangle(0, 0, 801, 33, fill='', width=0)
            walls = self.canvas.create_rectangle(0, 768, 353, 801, fill='', width=0)
            walls = self.canvas.create_rectangle(416, 768, 801, 801, fill='', width=0)
            walls = self.canvas.create_rectangle(767, 0, 801, 801, fill='', width=0)

            #INTERIOR WALLS
            walls = self.canvas.create_rectangle(32, 576, 353, 609, fill='', width=0)
            walls = self.canvas.create_rectangle(415, 576, 768, 609, fill='', width=0)
            walls = self.canvas.create_rectangle(416, 704, 449, 769, fill='', width=0)
            walls = self.canvas.create_rectangle(320, 704, 353, 769, fill='', width=0)
            walls = self.canvas.create_rectangle(415, 608, 449, 641, fill='', width=0)
            walls = self.canvas.create_rectangle(319, 608, 353, 641, fill='', width=0)
            walls = self.canvas.create_rectangle(512, 288, 768, 321, fill='', width=0)
            walls = self.canvas.create_rectangle(479, 32, 513, 129, fill='', width=0)
            walls = self.canvas.create_rectangle(479, 192, 513, 417, fill='', width=0)
            walls = self.canvas.create_rectangle(479, 480, 513, 577, fill='', width=0)
            walls = self.canvas.create_rectangle(255, 96, 289, 577, fill='', width=0)

            #Create user controlled robot
            player=self.canvas.create_rectangle(364,727,404,767,fill = 'green',width=2)

            #Robot Location Setter
            x1,y1,x2,y2=self.canvas.coords(player)

            '''Below code is used for controlling the robot, temporary code that will be wiped when pathfinding algorithm has been implemented'''
            #Move robot left
            def leftKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1-5,y1,x2-5,y2)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))

                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                    RandomItemToTable()
                    TreeviewItemTable()
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')


            #Move robot right
            def rightKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1+5,y1,x2+5,y2)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))
                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                    RandomItemToTable()
                    TreeviewItemTable()
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')

            #Move robot up
            def upKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1,y1-5,x2,y2-5)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))
                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                    RandomItemToTable()
                    TreeviewItemTable()
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')


            #Move robot down
            def downKey(event):
                x1,y1,x2,y2=self.canvas.coords(player)
                self.canvas.coords(player,x1,y1+5,x2,y2+5)
                currentLocation = self.canvas.coords(player)
                objectsTouching = (self.canvas.find_overlapping(currentLocation[0],currentLocation[1],currentLocation[2],currentLocation[3]))
                if 2<= (objectsTouching[-2]) <= 13:
                    print('You have hit the items!!!')
                    RandomItemToTable()
                    TreeviewItemTable()
                if 14<= (objectsTouching[-2]) <= 29:
                    print('You have hit the wall!!!')

            #move robot using keys
            self.canvas.bind('<Left>', leftKey)
            self.canvas.bind('<Right>', rightKey)
            self.canvas.bind('<Up>', upKey)
            self.canvas.bind('<Down>', downKey)
            self.canvas.focus_set()

        ''' Code for pathfinding algorithm''''''CALLUM'''
        class Graph(object):
            def __init__(self):
                self.nodes = set()
                self.edges = defaultdict(list)
                self.distances = {}

            def add_node(self, value):
                self.nodes.add(value)

            def add_edge(self, from_node, to_node, distance):
                self.edges[from_node].append(to_node)
                self.edges[to_node].append(from_node)
                self.distances[(from_node, to_node)] = distance

            def onObjectClick(event):
                ('Got object click', event.x, event.y)
                (event.widget.find_closest(event.x, event.y))

            def pathFinding(graph, initial):
                visited = {initial: 0}
                path = {}

                nodes = set(graph.nodes)

                while nodes:
                    min_node = None
                    for node in nodes:
                        if node in visited:
                            if min_node is None:
                                min_node = node
                            elif visited[node] < visited[min_node]:
                                min_node = node
                    if min_node is None:
                        break

                    nodes.remove(min_node)
                    current_weight = visited[min_node]

                    for edge in graph.edges[min_node]:
                        try:
                            weight = current_weight + graph.distances[(min_node, edge)]
                        except:
                            continue
                        if edge not in visited or weight < visited[edge]:
                            visited[edge] = weight
                            path[edge] = min_node

                return visited, path

            def shortest_path(graph, origin, destination):
                visited, paths = pathFinding(graph, origin)
                full_path = deque()
                _destination = paths[destination]

                while _destination != origin:
                    full_path.appendleft(_destination)
                    _destination = paths[_destination]

                full_path.appendleft(origin)
                full_path.append(destination)

                return visited[destination], list(full_path)

            #Depth first search
            def DFS(graph, start):
                path = []
                queue = [start]
                while queue:
                    v = queue.pop(0)
                    if v not in path:
                        path = path + [v]
                        queue = graph[v] + queue
                return path

            #Breadth first search
            def BFS(graph, start):
                path = []
                queue = [start]
                while queue:
                    v = queue.pop(0)
                    if v not in path:
                        path = path + [v]
                        queue = queue + graph[v]
                return path
            def graph():
                graph = (

                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #1
                        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1], #2
                        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1], #3
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1], #4
                        [1,0,0,1,1,1,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,1], #5
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], #6
                        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1], #7
                        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,0,0,0,1], #8
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], #9
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1], #10
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], #11
                        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1], #12
                        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1], #13
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], #14
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1], #15
                        [1,0,0,1,1,1,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1], #16
                        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,1,1,1,1,0,0,1], #17
                        [1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1], #18
                        [1,1,1,1,1,1,1,1,1,1,1,0,0,1,1,1,1,1,1,1,1,1,1,1,1], #19
                        [1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1], #20
                        [1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1], #21
                        [1,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,1,1,0,0,1,1,0,0,1], #22
                        [1,0,0,0,1,1,1,0,0,0,1,0,0,1,0,0,1,1,0,0,1,1,0,0,1], #23
                        [1,0,0,0,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,1], #24
                        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]  #25

                        )

        '''Timer Related Code''''''LAMAR'''
        def timerHandler(duration):
            self.duration = duration
            self.timerActiveLabel['text'] = duration // 60, "Minutes"

        '''  
        
        INDIVIDUAL FEATURE - Ryan -----------------------------------------------------------------------------------------------------
        
        '''
        '''Code to distribute items across the map''''''RYAN'''
        def distributeItems():
            sys.stdout.write("Distribute pressed \n")

            #Sets item variable as a PhotoImage variable and alocates it the 'item.png' resource file
            self.item = PhotoImage(file = 'item.png')
            #A tuple that holds 100 different coordinates of possible item locations
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

            #An array to track which coordinates have already been added to the map
            track = []
            #For loop to randomly position 20 different items on the map
            for x in range (20):
                #Random number generated using python random module (range 0-99)
                rnd = randint(0,99)
                #An if statement to check if the random number and therefore associated cooridnates have already been used
                if rnd in track:
                    #A while loop to generate random numbers until an un allocated coordinate is found
                    while rnd in track:
                        rnd = randint(0,99)
                    #Adds random number to track array
                    track.insert(x,rnd)
                    #Places image onto map in generated coordinates
                    self.canvas.create_image(tup[rnd], image = self.item)
                    
                else:
                    track.insert(x,rnd)
                    self.canvas.create_image(tup[rnd], image = self.item)
            randomitem()
        global tree
        
        '''
        -------------------------------------------------------------------------------------------------------------------------------
        '''
        


        def bubbleSort():
            #Function to sort a list into alphabetical/numerical order using Bubble Sort algorithm
            #Removes all entries from tree view
            tree.delete(*tree.get_children())
            for i in range(len(_List4Table) - 1):
                for j in range(len(_List4Table) - 1):
                    if (_List4Table[j])[0] > (_List4Table[j+1])[0]:
                        _List4Table[j], _List4Table[j+1] = _List4Table[j+1], _List4Table[j]
            return _List4Table,TreeviewItemTable()
            print(_List4Table())

        def bubbleSortReverse():
        #Function to sort a list into reverse alphabetical/numerical order using Bubble Sort algorithm
            tree.delete(*tree.get_children())
            for i in range(len(_List4Table) - 1):
                for j in range(len(_List4Table) - 1):
                    if (_List4Table[j])[0] < (_List4Table[j+1])[0]:
                        _List4Table[j], _List4Table[j+1] = _List4Table[j+1], _List4Table[j]
            return _List4Table,TreeviewItemTable()
            print(_List4Table())

        def insertionSort():
            #Used to sort by price
        #Function to sort a list into alphabetical/numerical order using Insertion Sort algorithm
            tree.delete(*tree.get_children())
            for i in range(len(_ProdPrice)):
                comparisonValue = _ProdPrice[i]
                while (i > 0) and (_ProdPrice[i-1] > comparisonValue):
                    _ProdPrice[i] = _ProdPrice[i-1]
                    i -= 1
                _ProdPrice[i] = comparisonValue
            return _ProdPrice,TreeviewSortByPrice()

        def insertionSortReverse():
            #Used to sort by price
        #Function to sort a list into reverse alphabetical/numerical order using Insertion Sort algorithm
            tree.delete(*tree.get_children())
            for i in range(len(_ProdPrice)):
                comparisonValue = _ProdPrice[i]
                while (i > 0) and (_ProdPrice[i-1] < comparisonValue):
                    _ProdPrice[i] = _ProdPrice[i-1]
                    i -= 1
                _ProdPrice[i] = comparisonValue
            return _ProdPrice,TreeviewSortByPrice()

        def quickSort():
        #Function to sort a list into alphabetical/numerical order using Quick Sort algorithm
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
                return quickSort(lessThan) + equalTo + quickSort(greaterThan)
            else:
                return _List4Table,TreeviewItemTable()

        def quickSortReverse():
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
                return _List4Table,TreeviewItemTable()


        '''Code to Sort by product name''''''NICK'''
        def sortName():
            sys.stdout.write("Name sort pressed \n")

            if self.button1["text"]=="v":
                self.button1["text"] = "^"
                #Sort descending

                if algorithm == "1":
                    print ("Quick sort (descending)")
                    bubbleSortReverse()

                elif algorithm == "2":
                    print ("Bubble sort (descending)")
                    bubbleSortReverse()

                elif algorithm == "3":
                    print ("Insertion sort (descending)")
                    insertionSortReverse()

            elif self.button1["text"]=="^":
                self.button1["text"]="v"
                #Sort ascending

                if algorithm == "1":
                    print ("Quick sort (ascending)")
                    quickSort()

                elif algorithm == "2":
                    print ("Bubble sort (ascending)")
                    bubbleSort()

                elif algorithm == "3":
                    print ("Insertion sort (ascending)")
                    insertionSort()

                if algorithm == "1":
                    print ("Quick sort (ascending)")
                    quickSort()

                elif algorithm == "2":
                    print ("Bubble sort (ascending)")
                    bubbleSort()

                elif algorithm == "3":
                    print ("Insertion sort (ascending)")
                    insertionSort()

            elif self.button1["text"]=="^":
                self.button1["text"]="v"
                #Sort ascending

        '''Code to Sort by price''''''NICK'''
        def sortPrice():
        
            sys.stdout.write("Price sort pressed \n")

            if self.button2["text"]=="v":
                self.button2["text"] = "^"
                #Sort descending

                if algorithm == "1":
                    print ("Quick sort (descending)")
                    quickSortReverse()

                elif algorithm == "2":
                    print ("Bubble sort (descending)")
                    bubbleSortReverse()

                elif algorithm == "3":
                    print ("Insertion sort (descending)")
                    insertionSortReverse()

            elif self.button2["text"]=="^":
                self.button2["text"]="v"
                #Sort ascending

                if algorithm == "1":
                    print ("Quick sort (ascending)")
                    quickSort()

                elif algorithm == "2":
                    print ("Bubble sort (ascending)")
                    bubbleSort()

                elif algorithm == "3":
                    print ("Insertion sort (ascending)")
                    insertionSort()

        '''Code to Sort by quantity''''''NICK'''
        def sortQuantity():
            sys.stdout.write("Quantity sort pressed \n")

            if self.button3["text"]=="v":
                self.button3["text"] = "^"
                #Sort descending
                if algorithm == "1":
                    print ("Quick sort (descending)")
                    quickSortReverse()

                elif algorithm == "2":
                    print ("Bubble sort (descending)")
                    bubbleSortReverse()

                elif algorithm == "3":
                    print ("Insertion sort (descending)")
                    insertionSortReverse()

            elif self.button3["text"]=="^":
                self.button3["text"]="v"
                #Sort ascending
                if algorithm == "1":
                    print ("Quick sort (ascending)")
                    quickSort()

                elif algorithm == "2":
                    print ("Bubble sort (ascending)")
                    bubbleSort()

                elif algorithm == "3":
                    print ("Insertion sort (ascending)")
                    insertionSort()

        '''Item Collection Code'''
        def itemCollection():
            EB = ExpandedBasket.TreeviewItemTable()
            EB.TreeviewItemTable()

        '''Sets up tje expanded basket table'''
        def table():
            tree["columns"]=("Price","Quantity","Category")
            tree.column("Price", width=200 )
            tree.column("Quantity", width=200)
            tree.column("Category", width=200)
            tree.heading("Price", text=" Price")
            tree.heading("Quantity", text=" Quantity")
            tree.heading("Category", text=" Category")


            global _List4Table

        '''Sets up treeview table'''
        def TreeviewItemTable():
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
                        tree.insert("" , "end", text= prodname, values=(_ItemList[0],_ItemList[1],_ItemList[2]))
                finally:
                    #Closes database connection in any circumstance
                    con.close()

        def TreeviewSortByPrice():
        #for loop iterates over all items contained in _ProdPrice
        #_ProdPrice contains item prices collected in game
            for price in _ProdPrice:
                try:
                #Connects to the item database
                    ItemList1= []
                    con= sql.connect('ITEM DATABASE.sqlite')
                    cur = con.cursor()
                    #finds the relevant information for product in _ProdPrice
                    cur.execute('''SELECT Product,Quantity,"Category " FROM items
                                   WHERE Price = ?;''', (price,))
                    #Appends Product, Quantity & Category to ItemList1
                    for row in cur:
                        ItemList1.append(row)
                        print(row)
                        #creates _ProdTable from ItemList1 (removing any tuples)
                        global _ProdTable
                        _ProdTable = [val for sublist in ItemList1 for val in sublist]
                        #Appends at the end of the tree with Name, Quantity, Price & Category in the relevant column
                        tree.insert("" , "end", text= _ProdTable[0], values=(price,_ProdTable[1],_ProdTable[2]))
                finally:
                    #Closes database connection in any circumstance
                    con.close()

        '''Calls all necessary functions'''
        frames(self)
        buttons(self)
        labels(self)
        map(self)
        table()
        tree.pack()

class listbox():

   #Initialises the actual listbox screens attributes
    def __init__(self):
        _listbox = Listbox(self)
        #MainProductList is the list with every item
        for product in MainProductList:
            _listbox.insert(-1,product)
        #Binds an event to Double Click on Left mouse button
        #Event is doubleclick function
        _listbox.bind("<Double-Button-1>", self.DoubleClick)
        #packs the listbox window
        _listbox.pack(side="top", fill="both", expand=True)
        #retrieves the cursors selection after a double click
    #The function that adds selected item to product in game

    def DoubleClick(self):
        #Selection is what handles a double-click
        selection=widget.curselection()
        #value is = to the item last clicked by user
        value = widget.get(selection[0])
        #Stores value into _list1
        #_list1 is all items retrievable by robot
        _list1 = []
        _list1.append(value)
        #Confirms what item was added to the game
        print(value,"was added to search items")

def main():
    root = Tk()
    mainInterface = MainInterface(root)
    root.mainloop()



if __name__ == '__main__':
    sys.exit(main())
