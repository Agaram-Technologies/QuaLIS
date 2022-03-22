from tkinter import *

from tkinter import messagebox

from Utility import BrowserOperation

top = Tk()
top.geometry("500x500")



def launchLIMS():
   BrowserOperation.launchLIMS()

B1 = Button(top, text = "Launch LIMS", command = launchLIMS)
B1.place(x = 35,y = 50)

B1 = Button(top, text = "Master", command = launchLIMS)
B1.place(x = 35,y = 100)

B1 = Button(top, text = "Transaction", command = launchLIMS)
B1.place(x = 35,y = 200)

top.mainloop()