from creatures import *
from moves import *
from typechart import *
import random

def attack(attacker, victim, move):
    if move.power>0:
        typeMultiplier = 1
        if victim.type in superEffective.get(move.type, []):
            typeMultiplier = 2
        elif victim.type in notVeryEffective.get(move.type, []):
            typeMultiplier = 0.5
        randomFactor = random.uniform(0.85,1)
        if move.type == attacker.type:
            stab = 1.25
        else: stab = 1
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
    else:
        if random.randint(1,100) <= move.accuracy:
            if move.effect is not None:
                if random.randint(1, 100) <= move.effectChance:
                    move.effect(attacker if move.affected == 'user' else victim, move.effectX, move.effectY, move.effectZ, 0)


def playRound(creature1, move1, creature2):
    tempMove = botChooseMove(creature2, creature1)
    if move1.priority > tempMove.priority:
        first = creature1
        second = creature2
        move = move1
        move2 = tempMove
    elif move1.priority < tempMove.priority:
        first = creature2
        second = creature1
        move = tempMove
        move2 = move1
    elif move1.priority == tempMove.priority:
        if creature1.speed * creature1.tempSpeed > creature2.speed * creature2.tempSpeed:
            first = creature1
            second = creature2
            move = move1
            move2 = tempMove
        elif creature1.speed * creature1.tempSpeed < creature2.speed * creature2.tempSpeed:
            first = creature2
            second = creature1
            move = tempMove
            move2 = move1
        else:
            if random.randint(0,1) == 0:
                first = creature1
                second = creature2
                move = move1
                move2 = tempMove
            else:
                first = creature2
                second = creature1
                move = tempMove
                move2 = move1
    attack(first, second, move)
    if second.isAlive():
        attack(second, first, move2)

def botChooseMove(user, target):
    bestMove = user.moves[0]
    bestDamage = 0
    for move in user.moves:
        typeMultiplier = 1
        if target.type in superEffective.get(move.type, []):
            typeMultiplier = 2
        elif target.type in notVeryEffective.get(move.type, []):
            typeMultiplier = 0.5
        randomFactor = 1
        if move.type == user.type:
            stab = 1.25
        else: stab = 1
        base   = (move.power * (user.attack*user.tempAttack) / (target.defense*target.tempDefense)) / 5 + 2
        damage = base * typeMultiplier * randomFactor * stab * (move.accuracy/100)
        statusEffectScore = 0
        if move.effect not in(None, staticScrambleEffect, healEffect):
            effectX = move.effectX if move.effectX is not None else 0
            effectY = move.effectY if move.effectY is not None else 0
            effectZ = move.effectZ if move.effectZ is not None else 0
            if move.affected == 'user':
                statusEffectScore = (effectX + effectY + effectZ) * 15 * move.effectChance/100
            elif move.affected == 'victim':
                statusEffectScore = abs(effectX + effectY + effectZ) * 12 * move.effectChance/100
        elif move.effect is staticScrambleEffect:
            statusEffectScore = 10
        elif move.effect is healEffect:
            healAmount = round(damage * 0.75)
            c = min(user.currenthp + healAmount, user.maxhp)
            statusEffectScore = (c - user.currenthp) * 1.5
        if target.attackBuff < 0:
            statusEffectScore *=0.75
        if target.defenseBuff < 0:
            statusEffectScore *=0.75
        if target.speed * target.tempSpeed > user.speed * user.tempSpeed and move.priority > 0:
            statusEffectScore += 2 / (user.currenthp/user.maxhp)
        if damage >= target.currenthp:
            statusEffectScore += 60
            damage = target.currenthp
        damage += statusEffectScore
        damage *= random.uniform(0.75,1)
        if damage > bestDamage:
            bestDamage = damage
            bestMove = move
    return bestMove