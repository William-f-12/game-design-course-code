#! python3.8
# Monster.py - monster class

import numpy as np
from islandTiles import island_map

class Monster:

    def __init__(self, description):
        self.description = description
        self.finding_probility = 0.2
        self.is_in_player_area = False
        self.area_in = None
        self.map = list(island_map.keys())[1:]


    def search(self):
        """monster search"""

        self.finding_probility += 0.1


    def attack(self, have_sword):
        """monster attack"""

        print("\n### Nooo!!! You see %s is looking at you! ###\n" % self.description)
        print("What do you decide to do?")
        print("A.Fight with a sword / B.Run as fast as you can / C.Pretend you are dead")
        choice = input("(A / B / C):")

        if choice == "A":
            if have_sword:
                print("\nYou've been fighting for a minute, you both are tired and injured")
                print("What do you do now?")
                print("A.Continue fighting / B.Run as fast as you can")
                choice = input("(A / B):")
                if choice == "A":
                    print("\nThis monster finally kill you...\n")
                elif choice == "B":
                    print("\nThis monster realize you are not a man to be messed with and leave for now\n")
                    return True
                else:
                    print("\nYou didn't make a choice and eaten by this monster...\n")

        elif choice == "B":
            print("\nThe monster catch you in seconds, you are not as fast as you thought...\n")

        elif choice == "C":
            if np.random.rand() < 0.5:
                print("\nYou are so lucky! The monster is not hungry. It leaves...\n")
                return True
            else:
                print("\nThe monster is hungry right now, you are eaten...\n")

        else:
            print("\nYou didn't make a choice and eaten by this monster...\n")
        return False


    def hunt(self, player_area, have_sword):
        """let the monster move"""

        self.area_in = np.random.choice(self.map)
        if self.area_in == player_area:
            # monster find player
            if np.random.rand() < self.finding_probility:
                self.search()
                return self.attack(have_sword)
            # monster does not find player
            else:
                print("You hear some strange sound, but find nothing special.")
        
        return True