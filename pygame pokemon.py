import random
import pygame

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
        return f"{self.name} ({self.type}) - Power: {self.power}, Accuracy: {self.accuracy}%"

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
def staticScrambleEffect(attacker, a, b, c, damage):
    x = random.choice([-1, 2])
    y = random.choice([-1, 2])
    z = random.choice([-1, 2])
    selfBuffingEffect(attacker, x, y, z, damage)

def attack(attacker, victim, move):
    typeMultiplier = 1
    if victim.type in superEffective.get(move.type, []):
        typeMultiplier = 2
    elif victim.type in notVeryEffective.get(move.type, []):
        typeMultiplier = 0.5
    randomFactor = random.uniform(0.85,1)
    if move.type == attacker.type:
        stab = 1.25
    base   = (move.power * (attacker.attack*attacker.tempAttack) / (victim.defense*victim.tempDefense)) / 5 + 2
    damage = base * typeMultiplier * randomFactor * stab
    if random.randint(1,100) <= move.accuracy:
        if random.randint(1,12) == 1:
            damage *= 1.5
            print("The attack seems to be strong...")
        damage = round(damage)
        if damage < 1:
            damage = 1
        if damage > victim.currenthp:
            damage = victim.currenthp
        victim.currenthp -= damage
        print(f"Damage: {damage}")
        if typeMultiplier == 2:
            print("It's super effective!")
        elif typeMultiplier == 0.5:
            print("It's not very effective...")
        print(f"{victim.name}'s HP: {victim.currenthp}/{victim.maxhp}")
        if move.effect is not None:
            if random.randint(1, 100) <= move.effectChance:
                move.effect(attacker if move.affected == 'user' else victim, move.effectX, move.effectY, move.effectZ, damage)
    else: print('Miss!')

def selfBuffingEffect(creature, attackBuff, defenseBuff, speedBuff, damage):
    for buff, stat, buffAttr in [(attackBuff, 'tempAttack', 'attackBuff'), (defenseBuff, 'tempDefense', 'defenseBuff'), (speedBuff, 'tempSpeed', 'speedBuff')]:
        setattr(creature, buffAttr, getattr(creature, buffAttr) + buff)
        if getattr(creature, buffAttr) > 6:
            setattr(creature, buffAttr, 6)
        elif getattr(creature, buffAttr) < -6:
            setattr(creature, buffAttr, -6)
        if getattr(creature, buffAttr) >= 0:
            setattr(creature, stat, (2+(getattr(creature, buffAttr))) * 0.5)
        elif getattr(creature, buffAttr) < 0:
            setattr(creature, stat, 2/(2 - getattr(creature, buffAttr)))
    print(f"{creature.name}'s stats have been modified: Attack: {creature.attackBuff}, Defense: {creature.defenseBuff}, Speed: {creature.speedBuff}")

def healEffect(creature, attackBuff, defenseBuff, speedBuff, damage):
    healAmount = round(damage * 0.75)
    creature.currenthp = min(creature.currenthp + healAmount, creature.maxhp)
    print(f"{creature.name} was healed for {healAmount} HP.")

#Type effectiveness dictionaries 'Attacker Type': ['Victim Type', 'Victim Type', ...]
superEffective = {
    'fire': ['grass'],
    'water': ['fire','rock'],
    'grass': ['water', 'rock','electric'],
    'electric': ['water', 'flying'],
    'rock': ['fire', 'flying'],
    'flying': ['grass'],
}
notVeryEffective = {
    'fire': ['water', 'fire', 'rock'],
    'water': ['grass', 'water'],
    'grass': ['fire', 'grass', 'flying'],
    'electric': ['grass', 'electric', 'rock'],
    'rock': ['grass'],
    'flying': ['electric', 'rock'],
    'normal': ['rock']
}

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

#Fire Creature
flamup = Creature('fire',70,70,45,65,flameFury,'Flamup')
#Water Creature
tidalotl = Creature('water',85,50,70,45,pressureWash,'Tidalotl')
#Grass Creature
mossbeetle = Creature('grass',75,60,65,50,mossyMash,'Mossbeetle')
#Normal Creature
mausef = Creature('normal',75,70,65,60,cookItUp,'Mausef')
rostirre = Creature('normal',50, 65, 50, 75, lunge, 'Rostirre')
#Electric Creature
voltile = Creature('electric',65,75,40,70,staticScramble,'Voltile')
#Rock Creature
rockjaw = Creature('rock',90,45,80,20,rockSlide,'Rockjaw')
#Flying Creature
dartlix = Creature('flying',70,65,50,80,dartThrow,'Dartlix')
knightwing = Creature('flying',80,70,60,90,rapidWing,'Knightwing')

pygame.init()
screenLength = 800
screenWidth = 600
screen = pygame.display.set_mode((screenLength, screenWidth))
maxBarLength = 300
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

def drawHpBar(creature, x, y):
    currenthp = creature.currenthp
    maxhp = creature.maxhp
    ratio = currenthp/maxhp
    hpBarLength = round((ratio)*maxBarLength)
    if ratio <= 0.2:
        hpColor = (255,0,0)
    elif ratio <= 0.5:
        hpColor = (255,255,0)
    else:
        hpColor = (0,255,0)
        
    pygame.draw.rect(screen, (0,0,0), (x, y, maxBarLength, 100))
    pygame.draw.rect(screen, hpColor, (x, y, hpBarLength, 100))
    
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if flamup.isAlive():
                    attack(voltile, flamup, thunderShock)
    screen.fill((30,30,30))

    drawHpBar(flamup, 0, 0)
    drawHpBar(voltile, 500, 500)
    creature1text = font.render(f"{flamup.name}: {flamup.currenthp}/{flamup.maxhp}", True, (255,255,255))
    creature2text = font.render(f"{voltile.name}: {voltile.currenthp}/{voltile.maxhp}", True, (255,255,255))
    screen.blit(creature1text, (0,100))
    screen.blit(creature2text,(630,470))
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()
