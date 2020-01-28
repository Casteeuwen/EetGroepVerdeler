from tkinter import *
from tkinter import ttk

import tkinter

class GUIHandler:

    def __init__(self):
        self.root = Tk()
        self.root.wm_title("Eetgroep Verdeler")

    def getroot(self):
        return self.root


    def initialize(self, leden, button, huizen):
        ####Create Leden Labels and checkboxes #################
        self.ledenPresenceTuples = []
        rowcounter = 0
        for lid in leden:
            naam = lid.getName()
            eetmee = lid.getEetMee()
            mijnvar = tkinter.BooleanVar()
            Label(self.root, text=naam, width = 15).grid(row = rowcounter)
            c = Checkbutton(self.root, variable=mijnvar)
            if(eetmee):
                c.select()
            c.grid(row=rowcounter, column=1)
            rowcounter = rowcounter +1
            tuple = [lid, mijnvar]
            self.ledenPresenceTuples.append(tuple)
        #########################################################

        ######Create button#############
        button.grid(row=rowcounter)
        ################################

        ####Create Huizen Labels and checkboxes ##################
        self.huisUsageTuples = []
        rowcounter = 0
        for huis in huizen:
            naam = huis.getName()
            mijnvar = tkinter.BooleanVar()
            Label(self.root, text=naam, width=15).grid(row=rowcounter, column = 2)
            c = Checkbutton(self.root, variable=mijnvar)
            c.grid(row=rowcounter, column=3)
            rowcounter = rowcounter + 1
            tuple = [huis, mijnvar]
            self.huisUsageTuples.append(tuple)

        mainloop()




    def getGUIHuizen(self):
        availableHuizen = []
        for tuple in self.huisUsageTuples:

            if tuple[1].get() == 1:
                #tuple[1] = True
                # print(tuple[0].getName())
                availableHuizen.append(tuple[0])
                # print('True')

            #elif tuple[1].get() == 0:
                #tuple[1] = False


        return availableHuizen

    def getGUIEters(self):
        eters = []
        for tuple in self.ledenPresenceTuples:

            if tuple[1].get() == 1:
                #tuple[1] = True
                #print(tuple[0].getName())
                eters.append(tuple[0])
                #print('True')

            #elif tuple[1].get() ==0:
                #tuple[1] = False


        return eters

    def popupmsg(self,msg):
        popup = tkinter.Tk()
        popup.wm_title("!")
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(popup, text="Okay", command=popup.destroy)
        B1.pack()
        popup.mainloop()