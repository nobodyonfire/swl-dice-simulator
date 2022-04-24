import random as rd
import statistics
import numpy as np


#Proba Attack Dice
AttName = ['crit' , 'touche' , 'adre' , 'miss']
AttWhite = [1,1,1,5]
AttBlack = [1,3,1,3]
AttRed = [1,5,1,1]
#Proba Defence Dice
AttName = ['def' , 'adre' , 'miss']
DefWhite = [1,1,4]
DefRed = [3,1,2]

#Precalculation for easier code 

NumberHitsAttRed = 5
NumberHitsAttBlack = 3
NumberHitsAttWhite = 1

NumberHitsDefRed = 3
NumberHitsDefWhite = 1

# 1 = CRIT 
# 2 = ADRE
# 3-x = TOUCHE

# ListThrow [crits,hits,Miss]


# 1 = ADRE
# 2 - x = TOUCHE

# ListThrow [Def,Miss]

# ListMiss [MissWhite, MissBlack, MissRed]



def oneThrow(ListThrow,NumberHits,AdreCrit,NumberCritical,NumberSurge,Adre):
    tmp=0
    random = rd.randint(1,8)

    #CRITS
    if random == 1:
        ListThrow[0]+=1
        return 1 ,NumberCritical,NumberSurge,ListThrow
    
    #HITS
    elif 3<= random <3+NumberHits:
        ListThrow[1]+=1
        return 1,NumberCritical,NumberSurge,ListThrow
    
    #ADRE
    elif random ==2:
        if AdreCrit:
            ListThrow[0]+=1
            return 1,NumberCritical,NumberSurge,ListThrow
        elif NumberCritical >0:
            ListThrow[0]+=1
            NumberCritical-=1
            return 1,NumberCritical,NumberSurge,ListThrow
        elif NumberSurge >0:
            ListThrow[0]+=1
            NumberSurge-=1
            return 1,NumberCritical,NumberSurge,ListThrow
        elif Adre:
            ListThrow[1]+=1
            return 1,NumberCritical, NumberSurge,ListThrow
        else:
            ListThrow[2]+=1
            return 0,NumberCritical,NumberSurge,ListThrow

    #MISS
    else :
        ListThrow[2]+=1
        return 0,NumberCritical,NumberSurge,ListThrow
    


    
def throwDice(numberAttWhiteDice,numberAttBlackDice,numberAttRedDice,DefDiceUsed,fullArmor,adredef,AdreCrit=False ,\
     Adre=False,numberThrow=50000,attOrDef ='att',critiqueNumber=0,impactNumber=0,armorNumber=0,dodgeNumber=0,\
         couvertNumber=0,perforantNumber=0,dangersensNumber=0,coupdechanceNumber=0,surgeNumber=0,surgeDefNumber=0,\
         HauteVelocite=False,aimNumber=0,preciseNumber=0):
    
    print("numberAttWhiteDice : ",numberAttWhiteDice)
    print("numberAttBlackDice : ",numberAttBlackDice)
    print("numberAttRedDice   : ",numberAttRedDice)
    print("AdreCrit           : ",AdreCrit)
    print("Adre               : ",Adre)
    print("critiqueNumber     : ",critiqueNumber)

    listEsperance =[]
    listCrits = []
    listHits = []
    listMiss = []
    listWound = []
    
    if (attOrDef =='att'):
        
        #NUMBER OF THROW:
        for throw in range (numberThrow):
            
            NumberCritical = critiqueNumber
            NumberSurge = surgeNumber
            NumberSurgeDef = surgeDefNumber
            esperance=0
            ListThrow=[0,0,0]
            ListMissPerDice = [0,0,0]

            for i in range(numberAttWhiteDice):
                result, NumberCritical,NumberSurge,ListThrow = oneThrow(ListThrow,NumberHitsAttWhite,AdreCrit,NumberCritical,NumberSurge,Adre)
                esperance += result
                ListMissPerDice[0]+=1-result
            

            for i in range(numberAttBlackDice):
                result, NumberCritical,NumberSurge, ListThrow= oneThrow(ListThrow,NumberHitsAttBlack,AdreCrit,NumberCritical,NumberSurge,Adre)
                esperance += result   
                ListMissPerDice[1]+=1-result
            

            for i in range(numberAttRedDice):
                result, NumberCritical,NumberSurge, ListThrow= oneThrow(ListThrow,NumberHitsAttRed,AdreCrit,NumberCritical,NumberSurge,Adre)
                esperance += result
                ListMissPerDice[2]+=1-result 
        

            #AIM 
            for i in range(aimNumber):

                rerolled=2+preciseNumber

                #RED
                for i in range(ListMissPerDice[2]):
                    if (rerolled>0):
                        result, NumberCritical,NumberSurge,ListThrow = oneThrow(ListThrow,NumberHitsAttRed,AdreCrit,NumberCritical,NumberSurge,Adre)
                        esperance += result
                        ListMissPerDice[2]-=result
                        rerolled-=1

                #BLACK
                for i in range(ListMissPerDice[1]):
                    if (rerolled>0):
                        result, NumberCritical,NumberSurge,ListThrow = oneThrow(ListThrow,NumberHitsAttBlack,AdreCrit,NumberCritical,NumberSurge,Adre)
                        esperance += result
                        ListMissPerDice[1]-=result
                        rerolled-=1
                    
                #WHITE
                for i in range(ListMissPerDice[0]):
                    if (rerolled>0):
                        result, NumberCritical,NumberSurge,ListThrow = oneThrow(ListThrow,NumberHitsAttWhite,AdreCrit,NumberCritical,NumberSurge,Adre)
                        esperance += result
                        ListMissPerDice[0]-=result
                        rerolled-=1




            #IMPACT 
            if (fullArmor or armorNumber>0):
                for i in range(impactNumber):
                    if (ListThrow[1])>0:
                        ListThrow[1]-=1
                        ListThrow[0]+=1


            listEsperance.append(esperance)
            listCrits.append(ListThrow[0])
            listHits.append(ListThrow[1])
            listMiss.append(ListThrow[2])

            #################
            #DEFENCE 
            #################

            #Couvert
            if (couvertNumber>0):
                for i in range( min(couvertNumber,ListThrow[1])):
                    ListThrow[1]-=1

            #Dodge:
            if (dodgeNumber>0 and not(HauteVelocite)):
                for i in range( min(dodgeNumber,ListThrow[1])):
                    ListThrow[1]-=1

            #Tireur embusqué

            #Full Armor 
            if (fullArmor):
                ListThrow[1]=0

            #Armor Number 
            if (armorNumber>0):
                for i in range( min(armorNumber,ListThrow[1])):
                    ListThrow[1]-=1

            numberOfSave=ListThrow[0]+ListThrow[1]

            sumResult=0

            #Danger Sens 

            #Dice def 
            if (DefDiceUsed=="rdef"):
                for i in range(numberOfSave+dangersensNumber):
                    result, ListThrow,NumberSurgeDef=  oneThrowDef(ListThrow,NumberHitsDefRed,adredef,NumberSurgeDef)
                    sumResult+=result
                
                #Coup de chance 
                if (coupdechanceNumber>0):
                    for j in range(coupdechanceNumber):
                        if(sumResult<numberOfSave):
                            result, ListThrow,NumberSurgeDef=  oneThrowDef(ListThrow,NumberHitsDefRed,adredef,NumberSurgeDef)
                            sumResult+=result


            if (DefDiceUsed=="wdef"):
                for i in range(numberOfSave+dangersensNumber):
                    result, ListThrow,NumberSurgeDef =  oneThrowDef(ListThrow,NumberHitsDefWhite,adredef,NumberSurgeDef)
                    sumResult+=result

                #Coup de chance 
                if (coupdechanceNumber>0):
                    for j in range(coupdechanceNumber):
                        if(sumResult<numberOfSave):
                            result, ListThrow,NumberSurgeDef=  oneThrowDef(ListThrow,NumberHitsDefWhite,adredef,NumberSurgeDef)
                            sumResult+=result
                
            


            #Perforant
            if (perforantNumber>0):
                for i in range( min(perforantNumber,sumResult)):
                    sumResult-=1
                 
            
            #Wound Total 
            if(sumResult>numberOfSave):
                listWound.append(0)
            else:
                listWound.append(numberOfSave-sumResult)

            




            
    



        #MEAN
        listEsperance = 1000*np.array(listEsperance)

        listCrits = 1000*np.array(listCrits)
        listHits = 1000*np.array(listHits)
        listMiss = 1000*np.array(listMiss)

        listWound = 1000*np.array(listWound)

        return statistics.mean(listEsperance)/1000,\
        statistics.mean(listCrits)/1000,\
        statistics.mean(listHits)/1000,\
        statistics.mean(listMiss)/1000,\
        statistics.mean(listWound)/1000
    




def oneThrowDef(ListThrow,NumberHits,Adre,NumberSurgeDef):
    tmp=0
    random = rd.randint(1,6)

    if 2<= random <2+NumberHits:
        ListThrow[0]+=1
        return 1,ListThrow,NumberSurgeDef
    
    elif random ==1:
       
        if Adre:
            ListThrow[0]+=1
            return 1,ListThrow,NumberSurgeDef
        elif NumberSurgeDef>0:
            NumberSurgeDef-=1
            ListThrow[0]+=1
            return 1,ListThrow,NumberSurgeDef
        else:
            ListThrow[1]+=1
            return 0,ListThrow,NumberSurgeDef

    else :
        ListThrow[1]+=1
        return 0,ListThrow,NumberSurgeDef

    
