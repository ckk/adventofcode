#!/usr/bin/env python27

from itertools import product
from copy import deepcopy, copy

BOSS = {
    'hit_points': 55,
    'damage': 8 
}

INITIAL_HIT_POINTS = 50
INITIAL_MANA = 500

ITEMS_SPELL = {
    'C. Magic Missile': {
        'cost': 53,
        'damage': 4,
        'turns': 0,
    },
    'E. Drain': {
        'cost': 73,
        'damage': 2,
        'healing': 2,
        'turns': 0,
    },
    'D. Shield': {
        'cost': 113,
        'turns': 6,
        'armor': 7,
    },
    'A. Recharge': {
        'cost': 229,
        'turns': 5,
        'mana_recharge': 101,
    },
    'B. Poison': {
        'cost': 173,
        'turns': 6,
        'damage': 3,
    },
}

# recursively test all combinations, ending if anyone wins or if spent mana > currently least value
# for spent mana for player win
# this should be refactored, code for player winning all over the place now after debugging several
# times and carefully re-reading the instructions. :)
def fight(hard, my_points, mana_left, mana_spent, boss_points, boss_damage, active_spells, spell_key=None):
    global least_mana
    if spell_key is not None:
        my_armor = 0
        if hard:
            my_points -= 1
        if my_points <= 0:
            return
        for aspell in active_spells.keys():
                if 'damage' in active_spells[aspell]:
                    boss_points -= active_spells[aspell]['damage']
                    if boss_points <= 0:
                        #print "Player won! mana_spent", mana_spent
                        least_mana = min(least_mana, mana_spent)
                if 'mana_recharge' in active_spells[aspell]:
                    mana_left += active_spells[aspell]['mana_recharge']
                if active_spells[aspell]['turns'] == 1:
                    del active_spells[aspell]
                else:
                    active_spells[aspell]['turns'] -= 1
        spell = ITEMS_SPELL[spell_key]
        mana_left -= spell['cost']
        if mana_left < 0:
            return
        mana_spent += spell['cost']
        if spell['turns'] == 0: # immediate spell
            if 'damage' in spell:
                boss_points -= spell['damage']
                if boss_points <= 0:
                    #print "Player won! mana_spent", mana_spent
                    least_mana = min(least_mana, mana_spent)
                    return
            if 'healing' in spell:
                my_points += spell['healing']
        else:
            active_spells[spell_key] = spell.copy()
        # boss turn
        for aspell in active_spells.keys():
                if 'armor' in active_spells[aspell]:
                    my_armor = active_spells[aspell]['armor']
                if 'damage' in active_spells[aspell]:
                    boss_points -= active_spells[aspell]['damage']
                    if boss_points <= 0:
                        #print "Player won! mana_spent", mana_spent
                        least_mana = min(least_mana, mana_spent)
                        return
                if 'mana_recharge' in active_spells[aspell]:
                    mana_left += active_spells[aspell]['mana_recharge']
                if active_spells[aspell]['turns'] == 1:
                    del active_spells[aspell]
                else:
                    active_spells[aspell]['turns'] -= 1
        my_points -= max(1, boss_damage - my_armor)
        if my_points <= 0:
            return
        #print "mana_left: %d, mana_spent: %d, my_points: %d, boss_points: %d" % (mana_left, mana_spent, my_points, boss_points)
    if mana_spent > least_mana:
        return
    for next_spell in sorted(ITEMS_SPELL.keys()): # sorting according to hinted order makes part one much faster
        # note the importance of also allowing a spell if next turn is the last turn it's active...
        if next_spell not in active_spells or active_spells[next_spell]['turns'] == 1:
            if spell_key is None: # show progress
                print next_spell
            fight(hard, my_points, mana_left, mana_spent, boss_points, boss_damage, deepcopy(active_spells), next_spell)

# global is an easy but ugly solution
least_mana = 1000000
fight(False, INITIAL_HIT_POINTS, INITIAL_MANA, 0, BOSS['hit_points'], BOSS['damage'], {})
print least_mana
least_mana = 1000000
fight(True, INITIAL_HIT_POINTS, INITIAL_MANA, 0, BOSS['hit_points'], BOSS['damage'], {})
print least_mana
