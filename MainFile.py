from Lid import Lid
from Huis import Huis
import random
from GUIHandler import GUIHandler
from tkinter import *
import datetime

HUIZEN = []
LEDEN = []
ROOT = None
GUI = None

#INITIALIZES HUIZEN AND LEDEN ARRAY AND OBJECTS
def initializeHouses():
    del HUIZEN[:]
    del LEDEN[:]

    #### Instantiate 'leden' and 'eters' array #########
    ledendoc = open("Leden.txt", "r")
    for x in ledendoc:
        if not x.strip():
            continue
        lidInfoArray = x.split()

        lidInfoArray[2] = int(lidInfoArray[2])
        lidInfoArray[4] = int(lidInfoArray[4])

        if (lidInfoArray[3] == 'Nee'):
            lidInfoArray[3] = False
        else:
            lidInfoArray[3] = True


        lidobj = Lid(lidInfoArray[0],lidInfoArray[1],lidInfoArray[2],lidInfoArray[3],lidInfoArray[4])
        LEDEN.append(lidobj)
    ledendoc.close()
    ########################################

    #### Instantiate 'huizen' array #######
    huizendoc = open("Huizen.txt", "r")
    for huisnaam in huizendoc:
        if not huisnaam.strip():
            continue
        huisnaam = huisnaam.rstrip()
        newHuis = Huis(huisnaam)
        HUIZEN.append(newHuis)
    huizendoc.close()
    #######################################



    #seeTenants()




def distributeEaters(eters):

    amtEating = len(eters)
    amtHouses = len(HUIZEN)
    avgEaters = float(amtEating)/ float(amtHouses)
    print('Amount of people eating: ', amtEating,'. \nNumber of houses: ',amtHouses, ' \nAvg eaters per house: ',avgEaters)

    unAssignedEaters = eters.copy()

    ### Set Present Tenants of a House############
    for huis in HUIZEN:
        huisname = huis.getName()
        for lid in LEDEN:
            homename = lid.getHome()
            if (homename == huisname and lid.getEetMee()):
                huis.addTenant(lid)
    #######################################

    ###First select a tenant to stay at the house##################
    for huis in HUIZEN:
        tenants = huis.getTenants()
        amtTenants = len(tenants)

        if(amtTenants > 0):
            randomTenant = random.choice(tenants)
            unAssignedEaters.remove(randomTenant)
            huis.addEater(randomTenant)
            print(huis.getName(), " tenant that stays: ", huis.getEaters()[0])
    ################################################################



    ###Assign lowest anci first as cook##########################
    unAssignedEaters.sort( key=lambda eater: eater.anci, reverse= True)
    maxAnciOfCooks = unAssignedEaters[amtHouses-1].anci
    possibleCookList = []
    #Create a list of possible cooks
    for eater in unAssignedEaters:
        if(eater.anci >= maxAnciOfCooks):
            possibleCookList.append(eater)

    #Choose a random cook from the list of possible cooks
    for huis in HUIZEN:
        randomCook = random.choice(possibleCookList)
        unAssignedEaters.remove(randomCook)
        possibleCookList.remove(randomCook)
        huis.setCook(randomCook)
        huis.addEater(randomCook)
    #############################################################


    ####Distibute the rest of the eaters#########################
    intavgeaters = int(avgEaters)
    for huis in HUIZEN:
        amtEatersAlreadyAssignedToHouse = len(huis.getEaters())
        for i in range(intavgeaters - amtEatersAlreadyAssignedToHouse):
            randomEater = random.choice(unAssignedEaters)
            unAssignedEaters.remove(randomEater)
            huis.addEater(randomEater)

    for huis in HUIZEN:
        if(len(unAssignedEaters)>0):
            randomEater = random.choice(unAssignedEaters)
            unAssignedEaters.remove(randomEater)
            huis.addEater(randomEater)
    #############################################################














######################################
def seeTenants():
    for huis in HUIZEN:
        print(' ')
        print(huis.getName(), ":")
        tenants = huis.getTenants()
        for tenant in tenants:
            print(tenant.getName())
######################################


######################################
def seeEaters():
    for huis in HUIZEN:
        print(' ')
        print(huis.getName(), ':')
        eaters = huis.getEaters()
        for eater in eaters:
            if eater == huis.getCook():
                print(eater.getName()," Nummer: ",eater.phoneNumber)
            else:
                print(eater.getName())

######################################

######################################
def createTheFile():
    f = open("Verdeling.txt", "w+")
    for huis in HUIZEN:
        f.write("\n")
        f.write("\n%s:" % huis.getName())
        eaters = huis.getEaters()
        for eater in eaters:
            if eater == huis.getCook():
                f.write("\n%s - %s" % (eater.getName(),eater.phoneNumber))
            else:
                f.write("\n%s" % eater.getName())
######################################

######################################
def clicked():
    guieters = GUI.getGUIEters()
    ETERS = guieters
    for lid in LEDEN:
        lid.setEetMee(False)

    #print('new  eterslist:' )
    for eter in ETERS:
        eter.setEetMee(True)
        #print(eter.getName())
    #print('after mod:')
    #for eter in ETERS:
    #    print(eter.getName())
    distributeEaters(ETERS)
    seeEaters()
    createTheFile()


if __name__ == '__main__':

    GUI = GUIHandler()
    ROOT = GUI.getroot()
    b = Button(ROOT, text="OK", command = clicked)
    initializeHouses()

    GUI.initialize(LEDEN,b)

