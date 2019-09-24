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
        self.deaths = 0
        self.kills = 0

    def add_kill(self, num_kills):
        '''
        Update kills with num_kills
        '''
        self.kills += num_kills

    def add_deaths(self, num_deaths):
        '''
        Update deaths with num_deaths
        '''
        self.deaths += num_deaths

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

    def defend(self):
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
        self.current_health -= (damage - self.defend())

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
        if (len(self.abilities) + len(opponent.abilities)) > 0:
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive():
                print(f'{self.name} won the battle.')
                self.add_kill(1)
                opponent.add_deaths(1)
            else:
                print(f'{opponent.name} won the battle.')
                opponent.add_kill(1)
                self.add_deaths(1)
        else:
            print('Draw')

class Team:
    def __init__(self, name):
        '''
        Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []
        self.battle_roster = []

    def helper_kills(self):
        '''
        Helper Functions to clean up code
        '''
        tot_kills = 0
        for hero in self.heroes:
            tot_kills += hero.kills
        return tot_kills

    def remove_hero(self, name):
        '''
        Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
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

    def attack(self, other_team):
        '''
        Battle each team against each other.
        '''
        attacking = True
        while attacking:
            #Randomly assigns order for the heroes to battle
            team_hero = self.heroes[random.randint(0, (len(self.heroes))-1)]
            other_team_hero = other_team.heroes[random.randint(0, (len(other_team.heroes))-1)]

            #Calls the heroes to fight
            team_hero.fight(other_team_hero)

            #Checks if there are any heroes remaining in the heroes list
            if self.helper_kills() > (len(other_team.heroes)-1):
                print(f'Team {self.name} has won!')
                attacking = False
                break
            elif other_team.helper_kills() > (len(self.heroes)-1):
                print(f'Team {other_team.name} has won!')
                attacking = False
                break
            else:
                pass

    def revive_heroes(self):
        '''
        Reset all heroes health to starting_health
        '''
        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''
        Print team statistics
        '''
        for hero in self.heroes:
            print(f'{hero.name} -- Kills: {hero.kills} Deaths: {hero.deaths}')


if __name__ == '__main__':
    team1 = Team('One')
    team2 = Team('Two')
    hero1 = Hero('Ghostie')
    hero2 = Hero('Blademaster')
    hero3 = Hero('Keanu')
    hero4 = Hero("Chuck")
    ability1 = Ability("Spookify", 90)
    ability2 = Ability("Slice", 85)
    ability3 = Ability("Dice", 70)
    ability4 = Ability("Time Distort", 70)
    ability5 = Ability("Karate Chop", 75)
    hero1.add_ability(ability1)
    hero2.add_ability(ability2)
    hero2.add_ability(ability3)
    hero3.add_ability(ability4)
    hero4.add_ability(ability5)
    team1.add_hero(hero1)
    team1.add_hero(hero4)
    team2.add_hero(hero2)
    team2.add_hero(hero3)
    team1.attack(team2)
