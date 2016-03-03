from tkinter import *
import tkinter as tk

class ExpandedBasket:

    def __init__(self, root):
        '''Basic window setup'''
        self.root = root
        self.root.resizable(width=FALSE, height=FALSE)
        self.root.wm_title("Python ALL Project")
        self.root.config(background = "#FFFFFF")
        self.root.geometry("1125x800")
        

        def frames(self):
            '''Create and place frames'''
            self.topFrame = Frame(self.root, width=1125, height = 50, background="royalblue")
            self.topFrame.grid(row=0, column=1, padx=0, pady=0, sticky="nes")
            
            #Frame to TreeView Basket
            self.tableFrame = Frame(self.root, width=1125, height = 800, background="white")
            self.tableFrame.grid(row=2, column=1, padx=0, pady=0, sticky="w")

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
        self.root.mainloop()


def main():
    root = Tk()
    expandedBasket = ExpandedBasket(root)
    root.mainloop()

if __name__ == '__main__':
        sys.exit(main())

        

