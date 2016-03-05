from tkinter import Tk, Button,ttk
from tkinter import *
import sqlite3 as sql
import tkinter as tk


class ExpandedBasket:

    def __init__(self, root):
        '''Basic window setup'''
        self.root = root
       
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.wm_title("Python ALL Project")
        self.root.config(background = "#FFFFFF")
        self.root.geometry("1125x800")
        self.tree = ttk.Treeview(self.root)
        

        def frames(self):
            '''Create and place frames'''
            self.topFrame = Frame(self.root, width=1125, height = 50, background="royalblue")
            self.topFrame.place(anchor="c",relx=0.5, rely=0.03)



        def buttons(self):
            '''Create and place buttons'''
            self.button1 = Button(self.topFrame, text="v", background="white", fg="black", command = lambda: sortID())
            self.button1.place(anchor="c", relx=0.18, rely=0.5)

            self.button2 = Button(self.topFrame, text="v", background="white", fg="black", command = lambda: sortName())
            self.button2.place(anchor="c", relx=0.385, rely=0.5)

            self.button3 = Button(self.topFrame, text="v", background="white", fg="black", command = lambda: sortPrice())
            self.button3.place(anchor="c", relx=0.585, rely=0.5)

            self.button4 = Button(self.topFrame, text="v", background="white", fg="black", command = lambda: sortQuantity())
            self.button4.place(anchor="c", relx=0.785, rely=0.5)

            self.button5 = Button(self.topFrame, text="v", background="white", fg="black", command = lambda: sortCategory())
            self.button5.place(anchor="c", relx=0.985, rely=0.5)


        def labels(self):
            '''Create and place labels'''
            self.idLabel = Label(self.topFrame, text="ID", background="royalblue", fg="white", font=(12))
            self.idLabel.place(anchor="c", relx=0.10, rely=0.5)

            self.productLabel = Label(self.topFrame, text="Product Name", background="royalblue", fg="white", font=(12))
            self.productLabel.place(anchor="c", relx=0.305, rely=0.5)

            self.priceLabel = Label(self.topFrame, text="Price", background="royalblue", fg="white", font=(12))
            self.priceLabel.place(anchor="c", relx=0.505, rely=0.5)

            self.quantityLabel = Label(self.topFrame, text="Quantity", background="royalblue", fg="white", font=(12))
            self.quantityLabel.place(anchor="c", relx=0.705, rely=0.5)

            self.categoryLabel = Label(self.topFrame, text="Category", background="royalblue", fg="white", font=(12))
            self.categoryLabel.place(anchor="c", relx=0.905, rely=0.5)

        def table(self):
            self.tree["columns"]=("Price","Quantity","Category")
            self.tree.column("Price", width=305 )
            self.tree.column("Quantity", width=305)
            self.tree.column("Category", width=310)
            self.tree.heading("Price", text=" Price")
            self.tree.heading("Quantity", text=" Quantity")
            self.tree.heading("Category", text=" Category")

            _List4Table =['Grapes','Salmon','Bacon','Wine','Celery','Duck']

            def TreeviewItemTable():
                for prodname in _List4Table:
                    try:
                        ItemList1= []
                        con= sql.connect('ITEM DATABASE.sqlite')
                        cur = con.cursor()
                        
                        cur.execute('''SELECT Price,Quantity,"Category " FROM items
                                       WHERE Product = ?;''', (prodname,))
                        for row in cur:
                            ItemList1.append(row)
                            print(row)

                            global _ItemList
                            _ItemList = [val for sublist in ItemList1 for val in sublist]
                            self.tree.insert("" , "end", text= prodname, values=(_ItemList[0],_ItemList[1],_ItemList[2]))
                    finally:
                        con.close()
            self.tree.place(relx=0.001, rely=0.06)
            


        def sortID():
            '''TODO: Sorting code'''
            sys.stdout.write("ID sort pressed \n")
            
            if self.button1["text"]=="v":
                self.button1["text"] = "^"
                #Sort descending

            if self.button1["text"]=="^":
                self.button1["text"]=="v"
                #Sort ascending
                

        def sortName():
            '''TODO: Sorting code'''
            sys.stdout.write("Name sort pressed \n")

            if self.button2["text"]=="v":
                self.button2["text"] = "^"
                #Sort descending

            if self.button2["text"]=="^":
                self.button2["text"]=="v"
                #Sort ascending

        def sortPrice():
            '''TODO: Sorting code'''
            sys.stdout.write("Price sort pressed \n")

            if self.button3["text"]=="v":
                self.button3["text"] = "^"
                #Sort descending

            if self.button3["text"]=="^":
                self.button3["text"]=="v"
                #Sort ascending


        def sortQuantity():
            '''TODO: Sorting code'''
            sys.stdout.write("Quantity sort pressed \n")

            if self.button4["text"]=="v":
                self.button4["text"] = "^"
                #Sort descending

            if self.button4["text"]=="^":
                self.button4["text"]=="v"
                #Sort ascending

        def sortCategory():
            '''TODO: Sorting code'''
            sys.stdout.write("Category sort pressed \n")

            if self.button5["text"]=="v":
                self.button5["text"] = "^"
                #Sort descending

            if self.button5["text"]=="^":
                self.button5["text"]=="v"
                #Sort ascending

        frames(self)
        buttons(self)
        labels(self)
        table(self)
        self.root.mainloop()


def main():
    root = Tk()
    expandedBasket = ExpandedBasket(root)
    root.mainloop()

if __name__ == '__main__':
        sys.exit(main())

        
