#!/usr/bin/env python

from itertools import combinations

BOSS = {
    'hit_points': 109,
    'damage': 8,
    'armor': 2,
}

INITIAL_HIT_POINTS = 100

ITEMS_WEAPON = {
    'Dagger': {
        'cost': 8, 'damage': 4, 'armor': 0
    },
    'Shortsword': {
        'cost': 10, 'damage': 5, 'armor': 0
    },
    'Warhammer': {
        'cost': 25, 'damage': 6, 'armor': 0
    },
    'Longsword': {
        'cost': 40, 'damage': 7, 'armor': 0
    },
    'Greataxe': {
        'cost': 74, 'damage': 8, 'armor': 0
    }
}

ITEMS_ARMOR = {
    'no_armor': { 
        'cost': 0, 'damage': 0, 'armor': 0
    },
    'Leather': { 
        'cost': 13, 'damage': 0, 'armor': 1
    },
    'Chainmail': { 
        'cost': 31, 'damage': 0, 'armor': 2
    },
    'Splintmail': { 
        'cost': 53, 'damage': 0, 'armor': 3
    },
    'Bandedmail': { 
        'cost': 75, 'damage': 0, 'armor': 4
    },
    'Platemail': { 
        'cost': 102, 'damage': 0, 'armor': 5
    }
}

ITEMS_RING = {
    'Damage +1': {
        'cost': 25, 'damage': 1, 'armor': 0
    },
    'Damage +2': {
        'cost': 50, 'damage': 2, 'armor': 0
    },
    'Damage +3': {
        'cost':100, 'damage': 3, 'armor': 0
    },
    'Defense +1': {
        'cost': 20, 'damage': 0, 'armor': 1
    },
    'Defense +2': {
        'cost': 40, 'damage': 0, 'armor': 2
    },
    'Defense +3': {
        'cost': 80, 'damage': 0, 'armor': 3
    }
}

def equipment():
    ring_combos = [()] + list(combinations(ITEMS_RING.keys(), 1)) + list(combinations(ITEMS_RING.keys(), 2))
    # at least one weapon
    for weapon, weapon_props in ITEMS_WEAPON.items():
        # zero or no armor, done by adding a 'zero' armor option above
        for armor, armor_props in ITEMS_ARMOR.items():
            # zero to two rings
            for rings in ring_combos:
                cost = 0
                damage = 0
                armor = 0
                for ring in rings:
                    cost += ITEMS_RING[ring]['cost']
                    damage += ITEMS_RING[ring]['damage']
                    armor += ITEMS_RING[ring]['armor']
                cost += weapon_props['cost']
                damage += weapon_props['damage']
                armor += weapon_props['armor']
                cost += armor_props['cost']
                damage += armor_props['damage']
                armor += armor_props['armor']
                yield (cost, damage, armor)

def fight(my_damage, my_armor):
    my_points = INITIAL_HIT_POINTS
    boss_points = BOSS['hit_points']
    boss_armor = BOSS['armor']
    boss_damage = BOSS['damage']
    my_turn = True
    while boss_points > 0 and my_points > 0:
        # It's only a scratch!
        if my_turn:
            boss_points += -max(1, my_damage - boss_armor)
        else:
            my_points += -max(1, boss_damage - my_armor)
        my_turn = not my_turn
    return my_points > 0


def cheapest_win():
    least_cost = 1000000
    for cost, damage, armor in equipment():
        if fight(damage, armor):
            least_cost = min(least_cost, cost)
    return least_cost

def expensive_loss():
    highest_cost = 0
    for cost, damage, armor in equipment():
        if not fight(damage, armor):
            highest_cost = max(highest_cost, cost)
    return highest_cost

print cheapest_win()
print expensive_loss()
