# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:11:10 2015

@author: Just the Nib
"""
#--------------------------------------------------------------------------------------------------- PROJECT FEAT START


import math
from random import randrange as rr

#------------------------------------------------------------------------------------------------------------------ UNIT INITIALIZATION FUNCTIONS START

def findSideAdvantage(cDirection, tDirection):
    #hit from behind
    if cDirection == tDirection:
        x = [10,1]
        return x
    #hit from front
    elif cDirection + tDirection == 5:
        x = [-5,-1]
        return x
    #hit from side
    else:
        x = [5,0]
        return x

#------------------------------------------------------------------------------------------------------------------ UNIT INITIALIZATION FUNCTIONS END

#------------------------------------------------------------------------------------------------------------------ BASE UNIT ENTITY START

class Actor:
    faction = -1                                                #-1=none, 0=player, 1=enemy, 2=neutral/friendly
    name = "null"
    stats = [
             rr(1,10),                                          #str  0
             rr(1,10),                                          #int  1
             rr(1,10),                                          #dex  2
             rr(1,10),                                          #agl  3
             rr(1,10),                                          #vit  4
             rr(1,10),                                          #end  5
             rr(1,10),                                          #wis  6
             rr(1,10)                                           #lck  7
             ]
    direction =             rr(4)+1
    sideAdvantage =         findSideAdvantage(direction)        #hit , dmg
    triangleAdvantage =     0
    weaponMastery =         [0,0]
    terrainModifier =       0
    health =                [stats(4)*7,stats(4)*7]             #current hp, max hp
#------------------------------------------------------------------------------------------------------------------ BASE UNIT ENTITY END
    
#------------------------------------------------------------------------------------------------------------------ COMBAT FORECAST FUNCTIONS START
    
def physicalDmg(cStr, cW, cWM, cSA, tEnd, tArmor, tTM):
    x = int(round(((( (cStr + cW) * cWM) - (tEnd + tArmor) ) * math.sqrt(cStr/tEnd) ) + (cSA - tTM)))
    if x > 0:
        return x
    else:
        return 0

def multiHit(cAgl,cWM,tAgl):
    x = int(math.floor((cAgl*cWM-tAgl)/4))
    if x > 1:
        return x
    else:
        return 1

def critPercent(cDex,cWM,tLck):
    advantage = cDex*cWM*3.0-tLck*2.95
    if advantage > 0:
        return int(round(200.0*(math.exp(advantage/33.075)/(1 + math.exp(advantage/33.075)))-100))
    else:
        return 0

def hitPercent(cDex, cLck, cWM, cSA, cTri, tAgl, tLck, tTM):
    x = ((((cDex * cWM) + cTri)/tLck) - (tAgl/cLck)) - (cSA + tTM)
    if x >= 0:
        y = int(round(60.0*(math.exp(x/12.0)/(1 + math.exp(x/12.0)))+40))
        return y
    elif x < 0:
        y = int(round(140.0*(math.exp(x/30.0)/(1 + math.exp(x/30.0)))))
        return y
    else:
        print("goat tho")

#------------------------------------------------------------------------------------------------------------------ COMBAT FORECAST FUNCTIONS END

#------------------------------------------------------------------------------------------------------------------ COMBAT EXECUTE FUNCTIONS START

def rng():
    return rr(100)

def attack(rng, crit, hit, dmg):
    if crit > rng:
        return dmg*3
    elif hit > rng:
        return dmg
    else:
        return 0
    

#------------------------------------------------------------------------------------------------------------------ COMBAT EXECUTE FUNCTIONS START






