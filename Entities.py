
class Player(object):
    def __init__(self,name, health, level, stamina, mana, magic, attack, pclass, armor,):
        self.name = name
        self.weapons = {"Ring" : object, "Main Hand": object, "Off Hand" : object}
        self.equipment = {"Pants": object, "Shirt" : object, "Shield": object}
        self.armor = armor
        self.health = health
        self.level = level
        self.stamina = stamina
        self.mana = mana
        self.magicp = mana
        self.attackp = attack
        if pclass==  "MAGE":
            self.magicp = magic + 5
            self.attackp = attack - 3
        elif pclass== "WARRIOR":
            self.magicp = magic - 3
            self.attackp = attack + 5
        self.pclass = pclass
    def attack(self, type, target):
        if type == "ranged":
            target.health -= self.magicp + target.armor*.5
            print(self.name + " dealt " + str((self.magicp - (target.armor*.5))) + " to " + target.name)
        elif type == "melee":
            target.health -= self.attackp + (target.armor*.5)
            print(self.name + " dealt " + str((self.attackp - (target.armor*.5))) + " to " + target.name)
        else:
            print("You charge your weapon for a powerful attack and deal" + ((self.attackp + self.magicp) / 2) + " damage.")
            target.health -= str(((self.attackp + self.magicp)/2) + target.armor)
    def equip(self, AR_object):
        self.equipment[AR_object.type] = AR_object
        self.armor += AR_object.value
        print(self.name + " has just equipped " + AR_object.name + "!\n" + self.name+"'s armor is now " + str(self.armor))
        """if (AR_object.type == "Shirt"):
            self.equipment["Shirt"] = AR_object
            self.armor += AR_object.value
            print(self.name + " has just equipped " + AR_object.name + "!\n" + self.name+"'s armor is now " + str(self.armor))
        elif (AR_object.type == "Pants"):
            self.equipment["Pants"] = AR_object
            self.armor += AR_object.value
            print(self.name + " has just equipped " + AR_object.name + "!\n" + self.name+"'s armor is now " + str(self.armor))
        elif (AR_object.type == "Shield"):
            self.equipment["Shield"] = AR_object
            self.armor += AR_object.value
            print(self.name + " has just equipped " + AR_object.name + "!\n" + self.name+"'s armor is now " + str(self.armor))"""
    def WE_equip(self, WE_object):
        print("You have just equipped " + WE_object.name + "!")
        self.weapons[WE_object.type] = WE_object
        # Rings increase health, not magic power or attack power. Conditional statement so that it increases health instead of causing errors
        if WE_object.type == "Ring":
            self.health += WE_object.value
            self.health -= self.weapons[WE_object.type].value
        else:
            if (self.weapons[WE_object.type] == object):
                self.attackp -= self.weapons[WE_object.type].attackp
                self.magicp -= self.weapons[WE_object.type].magicp
            self.attackp += WE_object.attackp
            self.magicp += WE_object.magicp
        print("Your attack is now "+ str(self.attackp) + " points\nYour Magic Power is now " + str(self.magicp) + " points. \nYour health is now " + str(self.health) + " health points")






class ring(object):
    def __init__(self, RI_name, RI_type, RI_value, RI_enchant):
        self.type = RI_type
        self.enchant = RI_enchant
        self.name = RI_name
        self.value = RI_value
        if (self.enchant):
            self.value = RI_value + 3

    def add_enchant(self, enchant_strentgh):
        self.value += enchant_strentgh
        print ("Congratulations!! " + self.name + " Has just been enchanted to increase it's power by " + str(enchant_strentgh))

class weapon(object):
    def __init__(self, WE_name, WE_type, WE_attackp, WE_magicp):
        self.name = WE_name
        self.type = WE_type
        self.attackp = WE_attackp
        self.magicp = WE_magicp
    def addEnchant(self, en_value, en_type):
        if (en_type == "magic"):
            self.magicp += en_value
        elif (en_type == "attack"):
            self.attackp += en_value


class enemy(object):
    def __init__(self, name, power, lvl, type, armor, health):
        self.health = health
        self.name = name
        self.power = power
        self.lvl = lvl
        self.type = type
        self.armor = armor
    def attack(self, target):
        target.health -= self.power - (target.armor * .45)
        print(self.name + " dealt " + str((self.power - (target.armor * .45))) + " damage to " + target.name)

class armor(object):
    def __init__(self,name, type, value, durability):
        self.name = name
        self.type = type
        self.value = value
        self.dur = durability
        self.maxdur = durability
    def crit(self, power):
        self.dur -= power*.25 - self.value
        if (self.dur <= self.maxdur*.1):
            print("Warning: " + self.name + " is almost broken!")


