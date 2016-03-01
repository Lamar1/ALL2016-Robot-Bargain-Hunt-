from tkinter import *
from random import randint

'''
[NOTES]
Must include the resource file 'item.png' and 'map.png in the same directory to run correctly' 
'''

class Game:

    '''This class will randomly distribute 20* items in a possible 100 locations and display on map'''

    def __init__(self, root, canvas):
        self.root = root
        self.canvas = Canvas(width = 800, height = 800, bg = 'black')
        self.canvas.pack(expand = YES, fill = BOTH)
        self.map = PhotoImage(file = 'map.png')
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.wm_title("Map Demo")


        self.canvas.create_image(0, 0, image = self.map, anchor = NW)
      

        def itemDistAll():
            '''Exactly 100 possible item locations'''

            #Left 1
            self.item = PhotoImage(file = 'item.png')
            self.canvas.create_image(105, 105, image = self.item)
            self.canvas.create_image(105, 130, image = self.item)
            self.canvas.create_image(105, 155, image = self.item)
            self.canvas.create_image(105, 180, image = self.item)
            self.canvas.create_image(130, 105, image = self.item)
            self.canvas.create_image(155, 105, image = self.item)
            self.canvas.create_image(180, 105, image = self.item)
            self.canvas.create_image(180, 130, image = self.item)
            self.canvas.create_image(180, 155, image = self.item)
            self.canvas.create_image(180, 180, image = self.item)
            self.canvas.create_image(155, 180, image = self.item)
            self.canvas.create_image(130, 180, image = self.item)

            #Left 2
            self.canvas.create_image(105, 265, image = self.item)
            self.canvas.create_image(105, 290, image = self.item)
            self.canvas.create_image(105, 315, image = self.item)
            self.canvas.create_image(105, 340, image = self.item)
            self.canvas.create_image(130, 340, image = self.item)
            self.canvas.create_image(155, 340, image = self.item)
            self.canvas.create_image(180, 340, image = self.item)
            self.canvas.create_image(180, 290, image = self.item)
            self.canvas.create_image(180, 265, image = self.item)
            self.canvas.create_image(180, 315, image = self.item)
            self.canvas.create_image(155, 265, image = self.item)
            self.canvas.create_image(130, 265, image = self.item)

            #Left 3
            self.canvas.create_image(105, 425, image = self.item)
            self.canvas.create_image(105, 450, image = self.item)
            self.canvas.create_image(105, 475, image = self.item)
            self.canvas.create_image(105, 500, image = self.item)
            self.canvas.create_image(130, 425, image = self.item)
            self.canvas.create_image(155, 425, image = self.item)
            self.canvas.create_image(180, 425, image = self.item)
            self.canvas.create_image(180, 450, image = self.item)
            self.canvas.create_image(180, 475, image = self.item)
            self.canvas.create_image(180, 500, image = self.item)
            self.canvas.create_image(155, 500, image = self.item)
            self.canvas.create_image(130, 500, image = self.item)

            #Left 4
            self.canvas.create_image(135, 650, image = self.item)
            self.canvas.create_image(135, 675, image = self.item)
            self.canvas.create_image(135, 700, image = self.item)
            self.canvas.create_image(135, 725, image = self.item)
            self.canvas.create_image(160, 650, image = self.item)
            self.canvas.create_image(185, 650, image = self.item)
            self.canvas.create_image(210, 650, image = self.item)
            self.canvas.create_image(210, 675, image = self.item)
            self.canvas.create_image(210, 700, image = self.item)
            self.canvas.create_image(210, 725, image = self.item)
            self.canvas.create_image(185, 725, image = self.item)
            self.canvas.create_image(160, 725, image = self.item)

            #Right 1
            self.canvas.create_image(650, 50, image = self.item)
            self.canvas.create_image(675, 50, image = self.item)
            self.canvas.create_image(700, 50, image = self.item)
            self.canvas.create_image(725, 50, image = self.item)
            self.canvas.create_image(750, 75, image = self.item)
            self.canvas.create_image(750, 100, image = self.item)
            self.canvas.create_image(750, 125, image = self.item)
            self.canvas.create_image(750, 150, image = self.item)

            #Right 2

            self.canvas.create_image(586, 200, image = self.item)
            self.canvas.create_image(611, 200, image = self.item)
            self.canvas.create_image(636, 200, image = self.item)
            self.canvas.create_image(661, 200, image = self.item)
            self.canvas.create_image(586, 246, image = self.item)
            self.canvas.create_image(611, 246, image = self.item)
            self.canvas.create_image(636, 246, image = self.item)
            self.canvas.create_image(661, 246, image = self.item)

            #Right 3
            self.canvas.create_image(586, 360, image = self.item)
            self.canvas.create_image(611, 360, image = self.item)
            self.canvas.create_image(636, 360, image = self.item)
            self.canvas.create_image(661, 360, image = self.item)
            self.canvas.create_image(686, 360, image = self.item)
            self.canvas.create_image(586, 406, image = self.item)
            self.canvas.create_image(611, 406, image = self.item)
            self.canvas.create_image(636, 406, image = self.item)
            self.canvas.create_image(661, 406, image = self.item)
            self.canvas.create_image(686, 406, image = self.item)

            #Right 4
            self.canvas.create_image(586, 490, image = self.item)
            self.canvas.create_image(611, 490, image = self.item)
            self.canvas.create_image(636, 490, image = self.item)
            self.canvas.create_image(661, 490, image = self.item)
            self.canvas.create_image(686, 490, image = self.item)
            self.canvas.create_image(586, 536, image = self.item)
            self.canvas.create_image(611, 536, image = self.item)
            self.canvas.create_image(636, 536, image = self.item)
            self.canvas.create_image(661, 536, image = self.item)
            self.canvas.create_image(686, 536, image = self.item)

            #Right 5
            self.canvas.create_image(520, 650, image = self.item)
            self.canvas.create_image(520, 675, image = self.item)
            self.canvas.create_image(520, 700, image = self.item)
            self.canvas.create_image(520, 725, image = self.item)
            self.canvas.create_image(565, 650, image = self.item)
            self.canvas.create_image(565, 675, image = self.item)
            self.canvas.create_image(565, 700, image = self.item)
            self.canvas.create_image(565, 725, image = self.item)

            #Right 6
            self.canvas.create_image(650, 650, image = self.item)
            self.canvas.create_image(650, 675, image = self.item)
            self.canvas.create_image(650, 700, image = self.item)
            self.canvas.create_image(650, 725, image = self.item)
            self.canvas.create_image(695, 650, image = self.item)
            self.canvas.create_image(695, 675, image = self.item)
            self.canvas.create_image(695, 700, image = self.item)
            self.canvas.create_image(695, 725, image = self.item)

        def itemDistRandom():
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

            for x in range (20):
                rnd = randint(0,99)
                self.canvas.create_image(tup[rnd], image = self.item)

                
        #itemDistAll()
        itemDistRandom()
        

root = Tk()
canvas = Canvas(width = 800, height = 800, bg = 'black')
game = Game(root,canvas)
