from models import Party
from creatures import *
import copy

gymLeaderMausef = copy.copy(mausef)
gymLeaderRostirre = copy.copy(rostirre)
gymLeaderPurven = copy.copy(purven)
gymLeaderParty = Party(gymLeaderRostirre,gymLeaderPurven,gymLeaderMausef)

