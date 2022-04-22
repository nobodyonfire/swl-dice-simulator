import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from termcolor import colored

import os 

csv_path = "././polls/csv/"
mainDf = pd.read_csv(os.path.join(csv_path,"swlcsv.csv"), sep=";")

def function_resize_for_bins(List):
    returnList = []
    for i in List:
        if (i<5):
            returnList.append(0.1)
        elif (i<10):
            returnList.append(0.3)
        elif (i<15):
            returnList.append(0.7)
        elif (i<20):
            returnList.append(0.9)
        else :
            returnList.append(1)
    return returnList
        
#Function For calculation Dice probability
def calculate_y_proba_dice(player='b',attOrDef='att',colorDice='r',round=None):
    
    df = mainDf.copy()

    #Blue Player 
    if player:
        df = df[df["player"]==player]
    
    if colorDice :
        df= df[df["couleur"]==colorDice]
        
    if attOrDef:
        df = df[df["att/def"]==attOrDef]
    
    if round :
        df = df[df["round"]==round]
        
    sumdf = df.sum()
    
    if (attOrDef =='att'):
        
        if(len(df)!=0):
            return [sumdf["critique"]/len(df),sumdf["touche"]/len(df),sumdf["adrenaline"]/len(df),sumdf["miss"]/len(df)],len(df)
        else : 
            return [0,0,0,0],0
        
    elif (attOrDef =='def'):
        
        if(len(df)!=0):
            return [sumdf["block"]/len(df),sumdf["adrenaline"]/len(df),sumdf["miss"]/len(df)],len(df)
        else : 
            return [0,0,0],len(df)
    
    
def count_number_dice(player='b',attOrDef='att',colorDice='r',round=None):
    
    df = mainDf.copy()
    
    #Blue Player 
    if player:
        df = df[df["player"]==player]
    
    if colorDice :
        df= df[df["couleur"]==colorDice]
        
    if attOrDef:
        df = df[df["att/def"]==attOrDef]
    
    if round :
        df = df[df["round"]==round]
        
    
        
    return len(df)

def count_number_dice_with_df(df,player='b',attOrDef='att',colorDice='r',round=None):
    
    #Blue Player 
    if player:
        df = df[df["player"]==player]
    
    if colorDice :
        df= df[df["couleur"]==colorDice]
        
    if attOrDef:
        df = df[df["att/def"]==attOrDef]
    
    if round :
        df = df[df["round"]==round]
        
    df = df.reset_index()


    index = df.index.tolist()

    df['statValue'] = df['statValue'].astype(float)
    StatsList = df["statValue"].tolist()
    
    
    indexRound = []
    serieGroupBy =df.groupby(['round']).size()

    for i in range (len(serieGroupBy)):
        somme=0
        for j in range(i+1):
            somme = somme + serieGroupBy[j+1]
        indexRound.append(somme)

            
        
        
    return index,StatsList,indexRound


def number_tir_def_per_unit(df,color):

    df = df[df["player"]==color]
    listUnits = df["unité"].unique()
    listUnits = listUnits[listUnits != 'supress']
    


    mainUnitsListTir = []
    mainUnitsListDef = []

    for unit in listUnits :

            listActualUnitTir=[]
            listActualUnitDef=[]

            dfUnits = df[df["unité"]==unit]

            dfUnitsTir = dfUnits[dfUnits["att/def"]=="att"]

            nombreDeTir = len(dfUnitsTir)
            listActualUnitTir.append(len(dfUnitsTir[dfUnitsTir["round"]==1]))
            listActualUnitTir.append(len(dfUnitsTir[dfUnitsTir["round"]==2]))
            listActualUnitTir.append(len(dfUnitsTir[dfUnitsTir["round"]==3]))
            listActualUnitTir.append(len(dfUnitsTir[dfUnitsTir["round"]==4]))
            listActualUnitTir.append(len(dfUnitsTir[dfUnitsTir["round"]==5]))
            listActualUnitTir.append(len(dfUnitsTir[dfUnitsTir["round"]==6]))

            dfUnitsDef = dfUnits[dfUnits["att/def"]=="def"]

            nombreDeDef = len(dfUnitsDef)
            listActualUnitDef.append(len(dfUnitsDef[dfUnitsDef["round"]==1]))
            listActualUnitDef.append(len(dfUnitsDef[dfUnitsDef["round"]==2]))
            listActualUnitDef.append(len(dfUnitsDef[dfUnitsDef["round"]==3]))
            listActualUnitDef.append(len(dfUnitsDef[dfUnitsDef["round"]==4]))
            listActualUnitDef.append(len(dfUnitsDef[dfUnitsDef["round"]==5]))
            listActualUnitDef.append(len(dfUnitsDef[dfUnitsDef["round"]==6]))

            mainUnitsListTir.append(listActualUnitTir)
            mainUnitsListDef.append(listActualUnitDef)

    return listUnits,mainUnitsListTir,mainUnitsListDef


def count_luck_per_round(df,player='b',attOrDef=None,round=None):
    
    #Blue Player 
    if player:
        df = df[df["player"]==player]
    
    if attOrDef:
        df = df[df["att/def"]==attOrDef]
    
    if round :
        df = df[df["round"]==round]
    
    if len(df) !=0 :
        value = df['statValue'].mean()
        return value
    else : 
        return 0

        
    