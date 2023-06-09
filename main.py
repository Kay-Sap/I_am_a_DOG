from tkinter import *
import random

class App(Tk):
    def __init__(self):
        super().__init__()
        
        self.page()
        
    
    def page(self):
        self.geometry('300x300+500+150')
        self.title('Question ')
        self.lbl = Label(self,text = 'Are you a DOG?' , font='itallic 24 bold')
        self.lbl.pack()
        
        self.yes_btn = Button(self , text='Yes' , font='comicsansms 10 bold' , padx = 10 , command = self.yes)
        self.yes_btn.place(x = 50 , y=150)

        self.No_btn = Button(self , text='No' , font='comicsansms 10 bold' , padx = 12 , command=self.play)
        self.No_btn.place(x = 200 , y=150)

    def play(self):
        
        x = random.randint(50,250)
        y = random.randint(50,250)
        self.No_btn.place(x = x , y = y)


    def yes(self):
        self.lbl.destroy()
        self.yes_btn.destroy()
        self.No_btn.destroy()

        self.title('I Know')
        know = Label(self,text = 'Yes I know.' , font='itallic 24 bold')
        know.place(x = 50 , y = 100)



if __name__ == '__main__':
    app = App()
    app.mainloop()

