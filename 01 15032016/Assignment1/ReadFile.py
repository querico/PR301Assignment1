__author__ = 'Rui Zheng'

from tkinter import *
from tkinter import filedialog


class OpenFile(object):
        root = Tk()
        root.fileName = filedialog.askopenfilename( filetypes=(("Target file", "txt"), ("All files", "*.*")))
        file = open(root.fileName, "r")




class ReadData(object):
    fileOpen = OpenFile()
    tehFile = fileOpen.file
    record = []
    personal = []
    for line in tehFile:
        record.append(line)

        x = line.split(" ")
        personal.append(x)
    fileOpen.file.close()





