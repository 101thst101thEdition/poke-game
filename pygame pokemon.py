import random

class Move:
    def __init__(self, mtype, power, accuracy, shownName, effect):
        self.type = mtype
        self.power = power
        self.accuracy = accuracy
        self.name = shownName
        self.effect = effect

class Creature:
    def __init__(self, ctype, maxhp, attack, defense, speed, startingMove, shownName):
        self.type = ctype
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = [startingMove]
        self.name = shownName

def attack(attacker, victim, move):
    typeMultiplier = 1
    randomFactor = random.uniform(0.85,1)
    base   = (move.power * attacker.attack / victim.defense) / 5 + 2
    damage = base * typeMultiplier * randomFactor
    damage = round(damage)
    print(f"Damage: {damage}")
    if random.randint(0,99) <= move.accuracy:
        victim.currenthp -= damage
        print(victim.currenthp)
    else: print('Miss!')

flameFury = Move('fire',60,95,'Flame Fury', None)
pressureWash = Move('water',60,95,'Pressure Wash', None)


flamup = Creature('fire',70,65,45,70,flameFury,'Flamup')
tidalotl = Creature('water',85,50,70,45,pressureWash,'Tidalotl')

print(flamup.moves)
attack(flamup,tidalotl,flameFury)


