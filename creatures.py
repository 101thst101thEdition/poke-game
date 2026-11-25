from models import Creature
from moves import *

creatureData = {
    #Fire Creatures
    'Flamup':{
        'type':'fire','hp':70,'attack':70,'defense':45,'speed':65,
        'moves': [flameFury, quickAttack, fireDance]
    },
    #Water Creatures
    'Tidalotl':{
        'type':'water','hp':85,'attack':50,'defense':70,'speed':45,
        'moves': [pressureWash, aquaRing, waterJet]
    },
    #Grass Creatures
    'Mossbeetle':{
        'type':'grass','hp':75,'attack':60,'defense':65,'speed':50,
        'moves': [mossyMash, leechLife, overgrowth]
    },
    #Normal Creatures
    'Mausef':{
        'type':'normal','hp':75,'attack':70,'defense':65,'speed':60,
        'moves':[cookItUp, thrash, quickAttack]
    },
    'Rostirre':{
        'type':'normal','hp':50,'attack':65,"defense":50,'speed':75,
        'moves': [lunge, pressureCook, quickAttack]
    },
    'Purven':{
        'type':'normal','hp':70,'attack':40,"defense":85,'speed':40,
        'moves': [thrash, pressureCook, quickAttack]
    }
}

def buildCreature(name, moves=None):
    data = creatureData[name]
    moveNames = moves if moves is not None else data['moves']
    moveObjects = [allMoves[m] for m in moveNames]
    return Creature(data['type'], data['hp'], data['attack'], data['defense'],
                    data['speed'], moveObjects[0], name, *moveObjects[1:3])

#Fire Creature
flamup = buildCreature('Flamup')
#Water Creature
tidalotl = buildCreature("Tidalotl")
#Grass Creature
mossbeetle = buildCreature('Mossbeetle')
#Normal Creature
mausef = buildCreature('Mausef')
rostirre = buildCreature('Rostirre')
purven = buildCreature('Purven')
#Electric Creature
voltile = Creature('electric',65,75,40,70,staticScramble,'Voltile', move2=fireDance, move3=leechLife)
boltolt = Creature('electric',40, 80, 30, 80,fissionBolt,'Boltolt')
#Rock Creature
rockjaw = Creature('rock',90,45,80,20,rockSlide,'Rockjaw')
#Flying Creature
dartlix = Creature('flying',70,65,50,80,dartThrow,'Dartlix')