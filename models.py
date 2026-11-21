class Move:
    def __init__(self, mtype, power, accuracy, shownName, effect, effectX=None, effectY=None, effectZ=None, effectChance=None, affected=None, priority=0):
        self.type = mtype
        self.power = power
        self.accuracy = accuracy
        self.name = shownName
        self.effect = effect
        self.priority = priority
        if self.effect is not None:
            self.effectX = effectX
            self.effectY = effectY
            self.effectZ = effectZ
            self.effectChance = effectChance
            self.affected = affected
    def __str__(self):
        return f"{self.name} ({self.type}) - P: {self.power}, Acc: {self.accuracy}%"

class Creature:
    def __init__(self, ctype, maxhp, attack, defense, speed, startingMove, shownName, move2 = None, move3 = None):
        self.type = ctype
        self.maxhp = maxhp
        self.currenthp = maxhp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = [startingMove]
        if move2 is not None:
            self.moves.append(move2)
        if move3 is not None:
            self.moves.append(move3)
        self.name = shownName
        self.tempAttack = 1
        self.tempDefense = 1
        self.tempSpeed = 1
        self.attackBuff = 0
        self.defenseBuff = 0
        self.speedBuff = 0
    def __str__(self):
        return f"{self.name} ({self.type}) - HP: {self.currenthp}/{self.maxhp}, Attack: {self.attack}, Defense: {self.defense}, Speed: {self.speed}, Moves: {[move.name for move in self.moves]}"
    def isAlive(self):
        return self.currenthp > 0
