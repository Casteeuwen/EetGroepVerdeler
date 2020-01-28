from tkinter import *
import tkinter

class GUIHandler:

    def __init__(self):
        self.root = Tk()

    def getroot(self):
        return self.root


    def initialize(self, leden, button):
        self.ledenPresenceTuples = []
        rowcounter = 0
        for lid in leden:
            naam = lid.getName()
            eetmee = lid.getEetMee()
            mijnvar = tkinter.BooleanVar()
            ############
            Label(self.root, text=naam).grid(row = rowcounter)
            c = Checkbutton(self.root, variable=mijnvar)
            if(eetmee):
                c.select()
            c.grid(row=rowcounter, column=1)
            rowcounter = rowcounter +1
            tuple = [lid, mijnvar]
            self.ledenPresenceTuples.append(tuple)

        button.grid(row = rowcounter)
        mainloop()

    def getGUIEters(self):
        eters = []
        for tuple in self.ledenPresenceTuples:

            if tuple[1].get() == 1:
                tuple[1] = True
                #print(tuple[0].getName())
                eters.append(tuple[0])
                #print('True')

            elif tuple[1].get() ==0:
                tuple[1] = False

            else:
                print('someting went wrong')
        return eters

