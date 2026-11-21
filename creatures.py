from models import Creature
from moves import *

#Fire Creature
flamup = Creature('fire',70,70,45,65,flameFury,'Flamup', move2=quickAttack, move3=fireDance)
#Water Creature
tidalotl = Creature('water',85,50,70,45,pressureWash,'Tidalotl')
#Grass Creature
mossbeetle = Creature('grass',75,60,65,50,mossyMash,'Mossbeetle')
#Normal Creature
mausef = Creature('normal',75,70,65,60,cookItUp,'Mausef')
rostirre = Creature('normal',50, 65, 50, 75, lunge, 'Rostirre')
#Electric Creature
voltile = Creature('electric',65,75,40,70,staticScramble,'Voltile', move2=fireDance, move3=leechLife)
#Rock Creature
rockjaw = Creature('rock',90,45,80,20,rockSlide,'Rockjaw')
#Flying Creature
dartlix = Creature('flying',70,65,50,80,dartThrow,'Dartlix')