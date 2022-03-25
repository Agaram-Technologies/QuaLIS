from tkinter import *

from tkinter import messagebox

from TestCoverage import TestCoverageUnit
from Utility import BrowserOperation

top = Tk()
top.geometry("500x500")



def launchLIMS():


   driver=BrowserOperation.launchLIMS()

def unitAdd():
   driver = BrowserOperation.launchLIMS()
   TestCoverageUnit.unitAdd(driver, "d","des","Yes" )


B1 = Button(top, text = "Launch LIMS", command = launchLIMS)
B1.place(x = 35,y = 50)

B1 = Button(top, text = "Unit Add", command = unitAdd())
B1.place(x = 35,y = 100)

B1 = Button(top, text = "Unit Edit", command = launchLIMS)
B1.place(x = 35,y = 200)

top.mainloop()