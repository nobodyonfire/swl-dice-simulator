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

def oneThrow(ListThrow,NumberHits,AdreCrit,NumberCritical,Adre):
    tmp=0
    random = rd.randint(1,8)
    if random == 1:
        ListThrow[0]+=1
        return 1 ,NumberCritical,ListThrow
    
    elif 3<= random <3+NumberHits:
        ListThrow[1]+=1
        return 1,NumberCritical,ListThrow
    
    elif random ==2:
        if AdreCrit:
            ListThrow[0]+=1
            return 1,NumberCritical,ListThrow
        elif NumberCritical >0:
            ListThrow[0]+=1
            NumberCritical-=1
            return 1,NumberCritical,ListThrow
        elif Adre:
            ListThrow[1]+=1
            return 1,NumberCritical,ListThrow
        else:
            ListThrow[2]+=1
            return 0,NumberCritical,ListThrow

    else :
        ListThrow[2]+=1
        return 0,NumberCritical,ListThrow
    


    
def throwDice(numberAttWhiteDice,numberAttBlackDice,numberAttRedDice,AdreCrit=False , Adre=False,numberThrow=50000,attOrDef ='att',critiqueNumber=0):
    
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
    
    if (attOrDef =='att'):
        
        #NUMBER OF THROW:
        for throw in range (numberThrow):
            
            NumberCritical = critiqueNumber
            esperance=0
            ListThrow=[0,0,0]
    
            for i in range(numberAttWhiteDice):
                result, NumberCritical,ListThrow = oneThrow(ListThrow,NumberHitsAttWhite,AdreCrit,NumberCritical,Adre)
                esperance += result
                
            for i in range(numberAttBlackDice):
                result, NumberCritical, ListThrow= oneThrow(ListThrow,NumberHitsAttBlack,AdreCrit,NumberCritical,Adre)
                esperance += result
                
            for i in range(numberAttRedDice):
                result, NumberCritical, ListThrow= oneThrow(ListThrow,NumberHitsAttRed,AdreCrit,NumberCritical,Adre)
                esperance += result
                

            listEsperance.append(esperance)
            listCrits.append(ListThrow[0])
            listHits.append(ListThrow[1])
            listMiss.append(ListThrow[2])
            
    
        listEsperance = 1000*np.array(listEsperance)

        listCrits = 1000*np.array(listCrits)
        listHits = 1000*np.array(listHits)
        listMiss = 1000*np.array(listMiss)

        return statistics.mean(listEsperance)/1000,\
        statistics.mean(listCrits)/1000,\
        statistics.mean(listHits)/1000,\
        statistics.mean(listMiss)/1000
    




def oneThrowDef(ListThrow,NumberHits,Adre):
    tmp=0
    random = rd.randint(1,6)

    if 2<= random <2+NumberHits:
        ListThrow[0]+=1
        return 1,ListThrow
    
    elif random ==1:
       
        if Adre:
            ListThrow[0]+=1
            return 1,ListThrow
        else:
            ListThrow[1]+=1
            return 0,ListThrow

    else :
        ListThrow[1]+=1
        return 0,ListThrow

  
def throwDiceDEF(numberDefWhiteDice,numberDefRedDice, Adre=False,numberThrow=50000,attOrDef ='def'):
    
    print("numberAttWhiteDice : ",numberDefWhiteDice)
    print("numberAttBlackDice : ",numberDefRedDice)
    print("Adre               : ",Adre)

    listEsperance =[]
    listDef = []
    listMiss = []
    
    if (attOrDef =='def'):
        
        #NUMBER OF THROW:
        for throw in range (numberThrow):
            
            esperance=0
            ListThrow=[0,0]
    
            for i in range(numberDefWhiteDice):
                result,ListThrow = oneThrowDef(ListThrow,NumberHitsDefWhite,Adre)
                esperance += result
                
            for i in range(numberDefRedDice):
                result, ListThrow=  oneThrowDef(ListThrow,NumberHitsDefRed,Adre)
                esperance += result
                
        

            listEsperance.append(esperance)
            listDef.append(ListThrow[0])
            listMiss.append(ListThrow[1])
            
    
        listEsperance = 1000*np.array(listEsperance)

        listDef = 1000*np.array(listDef)
        listMiss = 1000*np.array(listMiss)

        return statistics.mean(listEsperance)/1000,\
        statistics.mean(listDef)/1000,\
        statistics.mean(listMiss)/1000
    
