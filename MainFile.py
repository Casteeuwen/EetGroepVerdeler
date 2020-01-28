from Lid import Lid
from Huis import Huis
from ErrorFile import MoreHousesThanPeopleError
import random
from GUIHandler import GUIHandler
from tkinter import *
import datetime

HUIZEN = []
LEDEN = []
EETHUIZEN = []
ROOT = None
GUI = None

#INITIALIZES HUIZEN AND LEDEN ARRAY AND OBJECTS
def initializeHouses():
    del HUIZEN[:]
    del LEDEN[:]
    del EETHUIZEN[:]

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




def distributeEaters(eters, eethuizen):

    amtEating = len(eters)
    amtHouses = len(eethuizen)
    avgEaters = float(amtEating)/ float(amtHouses)
    print('Amount of people eating: ', amtEating,'. \nNumber of houses: ',amtHouses, ' \nAvg eaters per house: ',avgEaters)

    if amtEating<amtHouses:
        raise MoreHousesThanPeopleError(amtEating,amtHouses)

    unAssignedEaters = eters.copy()

    ### Set Present Tenants of a House############
    for huis in eethuizen:
        huisname = huis.getName()
        for lid in LEDEN:
            homename = lid.getHome()
            if (homename == huisname and lid.getEetMee()):
                huis.addTenant(lid)
    #######################################

    ###First select a tenant to stay at the house##################
    for huis in eethuizen:
        tenants = huis.getTenants()
        amtTenants = len(tenants)

        if(amtTenants > 0):
            randomTenant = random.choice(tenants)
            unAssignedEaters.remove(randomTenant)
            huis.addEater(randomTenant)
            print(amtTenants ," tenants at ",huis.getName(), ". tenant that stays: ", huis.getEaters()[0])
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
    for huis in eethuizen:
        randomCook = random.choice(possibleCookList)
        unAssignedEaters.remove(randomCook)
        possibleCookList.remove(randomCook)
        huis.setCook(randomCook)
        huis.addEater(randomCook)
    #############################################################


    ####Distibute the rest of the eaters#########################
    intavgeaters = int(avgEaters)
    for huis in eethuizen:
        amtEatersAlreadyAssignedToHouse = len(huis.getEaters())
        for i in range(intavgeaters - amtEatersAlreadyAssignedToHouse):
            randomEater = random.choice(unAssignedEaters)
            unAssignedEaters.remove(randomEater)
            huis.addEater(randomEater)

    for huis in eethuizen:
        if(len(unAssignedEaters)>0):
            randomEater = random.choice(unAssignedEaters)
            unAssignedEaters.remove(randomEater)
            huis.addEater(randomEater)
    #############################################################














######################################
# def seeTenants():
#     for huis in HUIZEN:
#         print(' ')
#         print(huis.getName(), ":")
#         tenants = huis.getTenants()
#         for tenant in tenants:
#             print(tenant.getName())
######################################


######################################
def seeEaters():
    for huis in EETHUIZEN:
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
    #print(" amt of eethuizen: ",len(EETHUIZEN))
    for huis in EETHUIZEN:
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
    eters = GUI.getGUIEters()
    for lid in LEDEN:
        lid.setEetMee(False)
    for eter in eters:
        eter.setEetMee(True)


    del EETHUIZEN[:]
    guiEeth = GUI.getGUIHuizen()
    for huis in HUIZEN:
        huis.eaters = []
        huis.tenants = []
        huis.setAvailable(False)
    for eethuis in guiEeth:
        EETHUIZEN.append(eethuis)
        eethuis.setAvailable(True)

    newhouses = GUI.getPossibleHouses()
    for newhouse in newhouses:
        EETHUIZEN.append(newhouse)
        newhouse.setAvailable(True)


    try:
        distributeEaters(eters,EETHUIZEN)
        #seeEaters()
        createTheFile()
    except MoreHousesThanPeopleError:
        GUI.popupmsg("AYO FAKKA MAN JE HEBT GWN TE VEEL HUIZEN G")



if __name__ == '__main__':

    GUI = GUIHandler()
    ROOT = GUI.getroot()
    b = Button(ROOT, text="OK", command = clicked)
    initializeHouses()

    GUI.initialize(LEDEN,b, HUIZEN)

