import random

def staticScrambleEffect(attacker, a, b, c, damage):
    x = random.choice([-1, 2])
    y = random.choice([-1, 2])
    z = random.choice([-1, 2])
    selfBuffingEffect(attacker, x, y, z, 0)

def selfBuffingEffect(creature, attackBuff, defenseBuff, speedBuff, _):
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

def healEffect(creature, ___, _, __, damage):
    healAmount = round(damage * 0.75)
    creature.currenthp = min(creature.currenthp + healAmount, creature.maxhp)
    print(f"{creature.name} was healed for {healAmount} HP.")
