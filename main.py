import math
from Entities import *
in_battle = False
def battle(player1, player2):
    print(player1.name + " has encountered "+ player2.name + ". \n Prepare to fight!")
    in_battle = True
    while (in_battle):
        choice = input("What would you like to do? ")
        if (choice.__contains__("attack")):
            player1.attack("ranged", player2)
            if (player2.health <= 0):
                print(player1.name + " has won the fight against " + player2.name)
                in_battle = False
                break

        player2.attack(player1)
        if (player1.health <= 0):
            print(player2.name + " has won the fight against " + player1.name)
            in_battle = False
            break
sword = weapon("Sword", "Main Hand", 5, 0,)
bow = weapon("Bow", "Off Hand", 5, 2)
gold_ring = ring("ring", "Ring", 5, True)
if __name__ == "__main__":
    attack = 10
    health = 20
    stam = 15
    magic = 10
    mana = 15
    puname = input("what is your name? ")
    suclass = input("what class do you want to be? Warrior or Mage?")
    Ethan = enemy("Ethan", 10, 2, "loser", 3, 100)
    suname = Player(puname,10, 1, 10, 10, 10, 10, suclass, 10)
    print("Name: " + suname.name)
    print("Class: " + suname.pclass)
    print("Attack: " +str(suname.attackp))
    print("Magic Power: " +str(suname.magicp))
    suname.WE_equip(sword)
    suname.WE_equip(bow)
    suname.WE_equip(gold_ring)




