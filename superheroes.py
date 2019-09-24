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
                print(f'{self.name} won a battle.')
                self.add_kill(1)
                opponent.add_deaths(1)
            else:
                print(f'{opponent.name} won a battle.')
                opponent.add_kill(1)
                self.add_deaths(1)
        else:
            print('Draw')

    def add_weapon(self, weapon):
        '''
        Add weapon to self.abilities
        '''
        self.abilities.append(weapon)

class Team:
    def __init__(self, name):
        '''
        Initialize your team with its team name
        '''
        self.name = name
        self.heroes = []
        self.survivors = []

    def helper_kills(self):
        '''
        Helper Functions to clean up code and check when someone has won.
        (outdated)
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
        print('\n')
        while attacking:
            #Randomly assigns order for the heroes to battle
            team_hero = self.heroes[random.randint(0, (len(self.heroes))-1)]
            other_team_hero = other_team.heroes[random.randint(0, (len(other_team.heroes))-1)]

            #Calls the heroes to fight
            team_hero.fight(other_team_hero)

            #Checks if there are any heroes remaining in the heroes list
            if self.helper_kills() > (len(other_team.heroes)-1):
                #print(f'{self.name} has won!')
                attacking = False
                break
            elif other_team.helper_kills() > (len(self.heroes)-1):
                #print(f'{other_team.name} has won!')
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
        kdr = 0
        total_kills = 0
        total_deaths = 0
        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths
        if total_deaths == 0:
            kdr = float(total_kills)
        else:
            kdr = float(total_kills/total_deaths)
        return kdr

    def surviving_victors(self):
        '''
        Finds the surviving Heroes and prints them out.
        '''
        is_victor = False
        for hero in self.heroes:
            if hero.is_alive():
                print(hero.name)
                is_victor = True
        if is_victor:
            print(f'{self.name} has won the battle!')

class Arena:
    def __init__(self):
        '''
        Takes Heroes and adds them to their respective teams.
        '''
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")

    def create_ability(self):
        '''
        Prompt for Ability information.
        return Ability with values from user Input
        '''
        name = input("Enter an Ability name: ")
        max_damage = input("Enter the Ability's max power (number): ")
        return Ability(name, int(max_damage))

    def create_weapon(self):
        '''
        Prompt user for Weapon information
        return Weapon with values from user input.
        '''
        name = input("Enter a Weapon name: ")
        max_damage = input("Enter the Weapon's max power (number): ")
        return Weapon(name, int(max_damage))

    def create_armor(self):
        '''
        Prompt user for Armor information
        return Armor with values from user input.
        '''
        name = input("Enter an Armor name: ")
        max_block = input("Enter the Armor's max block (number): ")
        return Armor(name, int(max_block))

    def create_hero(self):
        '''
        Prompt user for Hero information
        return Hero with values from user input.
        '''
        name = input("Enter a Hero name: ")
        new_Hero = Hero(name, starting_health=100)
        new_Hero.add_ability(self.create_ability())
        new_Hero.add_weapon(self.create_weapon())
        new_Hero.add_armor(self.create_armor())
        return new_Hero

    def build_team_one(self):
        '''
        Prompt the user to build team_one
        '''
        hero_amount = input("How many heroes do you want to make (number):  ")
        for i in range(0, int(hero_amount)):
            self.team_one.add_hero(self.create_hero())
        pass

    def build_team_two(self):
        '''
        Prompt the user to build team_two
        '''
        hero_amount = input("How many heroes do you want to make (number):  ")
        for i in range(0, int(hero_amount)):
            self.team_two.add_hero(self.create_hero())
        pass

    def team_battle(self):
        '''
        Battle team_one and team_two together.
        '''
        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''
        Prints team statistics and winner to terminal.
        '''
        #Shows Kills and Deaths, as well as ratio
        print(f'Team One KDR: {self.team_one.stats()}')
        print(f'Team Two KDR: {self.team_two.stats()}')

        #Prints out any hero that has not been killed and determines the
        #winner based off of that criteria
        print('Surviving Heroes: ')
        self.team_one.surviving_victors()
        self.team_two.surviving_victors()


if __name__ == '__main__':
    arena = Arena()
    arena.build_team_one()
    arena.build_team_two()
    arena.team_battle()
    arena.show_stats()
