import random

class Ability:
    '''
    An ability is an action that has a damage value.

    name: str
    max_damage: int
    '''

    def __init__(self, name, max_damage):
        self.name = name
        self.max_damage = max_damage

    def attack(self):
        '''Return a random value between 0 and the initialized max_damage strength.'''

        rand_hit = random.randint(0, self.max_damage)
        return rand_hit

class Weapon(Ability):
    '''Weapon extends Ability'''

    def attack(self):
        '''
        This method overrides Ability.attack() and returns a random value
        between one half to the full attack power of the weapon.
        '''

        rand_attack = random.randint((self.max_damage//2), self.max_damage)
        return rand_attack

class Armor:
    '''
    Armor is an action that returns a block value

    name: str
    max_block: int
    '''

    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block

    def block(self):
        '''Return a random value between 0 and the initialized max_block strength.'''

        rand_block = random.randint(0, self.max_block)
        return rand_block

class Hero:
    '''
    Hero takes in abilities and armors and can use those values to attack
    other heroes.

    name: str
    starting_health: int (default = 100)
    '''

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
        Update kills with num_kills.

        num_kills: int
        '''

        self.kills += num_kills

    def add_deaths(self, num_deaths):
        '''
        Update deaths with num_deaths.

        num_deaths: int
        '''

        self.deaths += num_deaths

    def add_ability(self, ability):
        '''
        Adds all abilities to ability list.

        ability: Ability Object
        '''

        self.abilities.append(ability)

    def attack(self):
        '''Calculate the total damage from all ability attacks.'''

        total_damage = 0
        for ability in self.abilities:
            total_damage += ability.attack()
        return total_damage

    def add_armor(self, armor):
        '''
        Adds armor to self.armors

        armor: Armor Object
        '''

        self.armors.append(armor)

    def defend(self):
        '''
        Runs `block` method on each armor.
        Returns sum of all blocks.
        '''

        total_blocked = 0
        for armor in self.armors:
            total_blocked += armor.block()
        return total_blocked

    def take_damage(self, damage):
        '''
        Updates self.current_health to reflect the damage minus the defense.

        damage:int
        '''

        self.current_health -= max(0, damage - self.defend())

    def is_alive(self):
        '''
        Return True or False depending on whether the hero is alive or not.
        '''

        return self.current_health > 0

    def fight(self, opponent):
        '''
        Heroes fight by attacking each other and taking damage.
        Exits loop if either one of their health reaches 0.
        Returns draw if there are no abilities in the Hero object

        Adds kills and deaths to respective Hero objects.

        opponent: Hero Object
        '''

        if (len(self.abilities) + len(opponent.abilities)) > 0:
            while self.is_alive() and opponent.is_alive():
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())
            if self.is_alive():
                print(f'{self.name} won a battle.')
                self.add_kill(1)
                opponent.add_deaths(1)
            elif opponent.is_alive():
                print(f'{opponent.name} won a battle.')
                opponent.add_kill(1)
                self.add_deaths(1)
            else:
                print(f'{self.name} and {opponent.name} drew the battle')
                self.add_deaths(1)
                self.add_kill(1)
                opponent.add_kill(1)
                opponent.add_deaths(1)
        else:
            print('Draw')

    def add_weapon(self, weapon):
        '''
        Adds weapon to self.abilities

        weapon: Weapon object
        '''

        self.abilities.append(weapon)

class Team:
    '''
    Initialize your team with its team name, and takes in lists of hero objects.

    name: str
    '''

    def __init__(self, name):
        self.name = name
        self.heroes = []

    def remove_hero(self, name):
        '''
        Remove hero from heroes list. If Hero isn't found return 0.

        name: str
        '''

        for hero in self.heroes:
            if name == hero.name:
                self.heroes.remove(hero)
            else:
                pass
        return 0

    def view_all_heroes(self):
        '''Prints out all heroes to the console in self.heroes'''

        for hero in self.heroes:
            print(hero.name)

    def add_hero(self, hero):
        '''
        Add Hero object to self.heroes

        hero: Hero Object
        '''

        self.heroes.append(hero)

    def attack(self, other_team):
        '''
        Battle each team against each other. Selects a hero randomly from each
        team's list of heroes and battles them against each other.

        Loop ends when one team's kills totals the amount of heroes in the other
        team's hero list.

        other_team = Team Object
        '''

        attacking = True
        print('\n')
        while attacking:
            #Assigns heroes to different list to battle
            first_team = []
            second_team = []
            for hero in self.heroes:
                if hero.is_alive():
                    first_team.append(hero)
            for hero in other_team.heroes:
                if hero.is_alive():
                    second_team.append(hero)

            #Checks if there are any heroes remaining in the heroes list
            if len(first_team) == 0:
                if len(second_team) == 0:
                    print('Its a draw!')
                    attacking = False
                    break
                else:
                    print(f'{other_team.name} has won!')
                    attacking = False
                    break
            elif len(second_team) == 0:
                if len(first_team) == 0:
                    print('Its a draw!')
                    attacking = False
                    break
                else:
                    print(f'{self.name} has won!')
                    attacking = False
                    break
            else:
                #Calls the heroes to fight
                first_hero = random.choice(first_team)
                second_hero = random.choice(second_team)
                first_hero.fight(second_hero)

    def revive_heroes(self):
        '''Reset all heroes health to starting_health in heroes list.'''

        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def stats(self):
        '''
        Prints team statistics by taking in each heroe's kill and death count.
        Then calculates the KDR based off of those values.
        '''

        kdr = 0
        total_kills = 0
        total_deaths = 0
        for hero in self.heroes:
            total_kills += hero.kills
            total_deaths += hero.deaths
        if total_deaths == 0:
            kdr = total_kills
        else:
            kdr = total_kills/total_deaths
        return kdr

    def surviving_victors(self):
        '''
        Finds the surviving Heroes and prints them to terminal.
        If there is someone alive in a list of heroes, then it returns that
        that team has won.
        '''

        for hero in self.heroes:
            if hero.is_alive():
                print(hero.name)

class Arena:
    '''
    Uses Team objects to 'battle' against each other. Also creates functions
    that allow for user inputs to create their own abilities, weapons, armors
    and heroes.

    Shows the stats of each battle then returns who won.
    '''

    def __init__(self):
        self.team_one = Team("Team One")
        self.team_two = Team("Team Two")
        self.battles = 0

    def create_ability(self):
        '''Prompts user for information to create ability values then returns it.'''

        name = input("Enter an Ability name: ")
        max_damage = input("Enter the Ability's max power (number): ")
        return Ability(name, int(max_damage))

    def create_weapon(self):
        '''Prompts user for information to create weapon values then returns it.'''

        name = input("Enter a Weapon name: ")
        max_damage = input("Enter the Weapon's max power (number): ")
        return Weapon(name, int(max_damage))

    def create_armor(self):
        '''Prompts user for information to create armor values then returns it.'''

        name = input("Enter an Armor name: ")
        max_block = input("Enter the Armor's max block (number): ")
        return Armor(name, int(max_block))

    def create_hero(self):
        '''
        Prompts user to give a name for Hero. Then uses the other values from
        ability, weapon, and armor to add to the new Hero created and returns the hero.
        '''

        name = input("Enter a Hero name: ")
        new_Hero = Hero(name, starting_health=100)
        new_Hero.add_ability(self.create_ability())
        new_Hero.add_weapon(self.create_weapon())
        new_Hero.add_armor(self.create_armor())
        return new_Hero

    def build_team_one(self):
        '''
        Prompts the user for how many heroes they want in their Team.
        For the amount given, calls the create_hero function to create hero objects
        and adds them to the team.
        '''

        hero_amount = input("How many heroes do you want to make (number):  ")
        for i in range(0, int(hero_amount)):
            self.team_one.add_hero(self.create_hero())
        pass

    def build_team_two(self):
        '''
        Prompts the user for how many heroes they want in their Team.
        For the amount given, calls the create_hero function to create hero objects
        and adds them to the team.
        '''

        hero_amount = input("How many heroes do you want to make (number):  ")
        for i in range(0, int(hero_amount)):
            self.team_two.add_hero(self.create_hero())
        pass

    def team_battle(self):
        '''Battle team_one and team_two together using attack function.'''

        self.team_one.attack(self.team_two)

    def show_stats(self):
        '''Prints team statistics and winner to terminal.'''

        #Shows Kills and Deaths, as well as ratio
        print(f'Team One KDR: {self.team_one.stats()}')
        print(f'Team Two KDR: {self.team_two.stats()}')

        #Prints out any hero that has not been killed and determines the
        #winner based off of that criteria
        print('Surviving Heroes: ')
        self.team_one.surviving_victors()
        self.team_two.surviving_victors()

if __name__ == "__main__":
    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
