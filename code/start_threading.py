import random
import time
from tkinter import *
from code.mainwindow import window
from threading import *

class START(Thread):
    def run(self):
        root=Tk()
        window(root)
        root.mainloop()