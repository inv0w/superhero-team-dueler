import random

class Ability:
    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        rand_hit = random.randint(0, self.max_damage)
        return rand_hit

class Weapon(Ability):
    def attack(self):
        '''
        This method returns a random value
        between one half to the full attack power of the weapon.
        '''
        rand_attack = random.randint((self.max_damage//2), self.max_damage)
        return rand_attack

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        '''
        Return a random value between 0 and the initialized max_block strength.
        '''
        rand_block = random.randint(0, self.max_block)
        return rand_block

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = []
        self.armors = []

    def add_ability(self, ability):
        '''
        Adds all abilities to ability list.
        '''
        self.abilities.append(ability)

    def attack(self):
        '''
        Calculate the total damage from all ability attacks.
          return: total:Int
        '''
        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''
        Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)


    def defend(self, incoming_damage):
        '''
        Runs `block` method on each armor.
        Returns sum of all blocks
        '''
        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()
        return total_blocked

    def take_damage(self, damage):
        '''
        Updates self.current_health to reflect the damage minus the defense.
        '''
        self.current_health -= (damage - self.defend(damage))

    def is_alive(self):
        '''
        Return True or False depending on whether the hero is alive or not.
        '''
        if self.current_health >= 0:
            return True
        else:
            return False

    def fight(self, opponent):
        '''
        Current Hero will take turns fighting the opponent hero passed in.
        '''
        if (len(self.abilities) + len(opponent.abilities)) < 1:
            print('Draw')
        else:
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
        if self.is_alive():
            print(f'{self.name} won!')
        else:
            print(f'{opponent.name} won!')

class Team:
    def __init__(self, name):
        '''
        Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        # TODO: Implement this method to remove the hero from the list given their name.
        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
            else:
                pass
        return 0

    def view_all_heroes(self):
        '''
        Prints out all heroes to the console.
        '''
        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''
        Add Hero object to self.heroes.
        '''
        self.heroes.append(hero)


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.

    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    hero3 = Hero("test")
    weapon = Weapon("axe", 80)
    print(weapon.attack())
    ability1 = Ability("Super Speed", 300)
    ability2 = Ability("Super Eyes", 130)
    ability3 = Ability("Wizard Wand", 80)
    ability4 = Ability("Wizard Beard", 20)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)
