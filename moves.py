from models import Move
from effects import *

#Fire
flameFury = Move('fire',60,100,'Flame Fury', None)
flameCharge = Move('fire',100,90,'Flame Charge', selfBuffingEffect, -1, 0, 0, 100, affected='user')
fireDance = Move('fire',0,100,'Fire Dance', selfBuffingEffect, 1, 1, 1, 100, affected='user')
#Water
pressureWash = Move('water',60,100,'Pressure Wash', None)
hydroPump = Move('water',90,80,'Hydro Pump', None)
aquaRing = Move('water',30,100,'Aqua Ring', healEffect, effectChance=100, affected='user')
#Grass
mossyMash = Move('grass',60,100,'Mossy Mash', None)
overgrowth = Move('grass',30,100,'Overgrowth', selfBuffingEffect, 1, 1, 1, 60, affected='user')
leechLife = Move('grass',20,100,'Leech Life', healEffect, effectChance=100, affected='user')
#Normal
cookItUp = Move('normal',80,100,'Cook It Up', selfBuffingEffect, 1, 1, 1, 20, affected='user')
quickAttack = Move('normal',40,100,'Quick Attack', None, priority=1)
thrash = Move('normal',90,100,'Thrash', selfBuffingEffect, 0, -1, -1, 100, affected='user')
lunge = Move('normal', 50, 100, 'Lunge', None)
#Electric
staticScramble = Move('electric',70,90,'Static Scramble', staticScrambleEffect, effectChance=30, affected='user')
powerSavingMode = Move('electric',0,100,'Power Saving Mode', selfBuffingEffect, -1, -1, -1, 100, affected='victim')
thunderShock = Move('electric',50,100,'Thunder Shock', None)
#Rock
rockSlide = Move('rock',40,90,'Rock Slide', selfBuffingEffect, 0, 0, -1, 30, affected='victim')
rockOn = Move('rock',0,100,'Rock On', selfBuffingEffect, 1, 1, 1, 100, affected='user')
rockThrow = Move('rock',60,100,'Rock Throw', None)
#Flying
skyDive = Move('flying',80,95,'Sky Dive', None)
dartThrow = Move('flying',60,100,'Dart Throw', selfBuffingEffect, 0, 0, 1, 30, affected='user')
rapidWing = Move('flying',40,100,'Rapid Wing', selfBuffingEffect, 0, 0, 1, 100, affected='user')
