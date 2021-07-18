#! python3.8
# GameController.py - control a single game

import os, time
import numpy as np
from islandTiles import island_map as tiles, ask_which_area 
from Encounters import Encounters
from Monster_Tiger import two_head_tiger

class GameController:

    def __init__(self):
        self.alive = True
        self.saved = False
        self.days = 0
        self.hunger = 7
        self.thirst = 3
        self.inventory = []
        self.island_map = tiles

    def show_info(self):
        """show basic information"""

        if self.days == 0:
                print("You have washed up on a Deserted Island! You must search the island for Food and Water to survive until rescue...")    
        
        os.system("cls")
        print("\nDays on the deserted island: "+str(self.days))
        print("hunger:", self.hunger)
        print("thirst:", self.thirst, end="\n\n")
        # show inventory
        print("Your Inventory: ")
        print("=================")
        if self.inventory:
            for item in self.inventory:
                print(item)
        else:
            print("Nothing here yet")
        print("=================\n")


    def play(self):
        # the main while loop
        while(self.alive):
            # show information
            self.show_info()

            # check hunger and thrist
            if self.hunger == 0:
                print("\nYou are too hungry to survive... Game Over.\n")
                self.alive = False
                continue
            if self.thirst == 0:
                print("\nYou die of thirst... Game Over\n")
                self.alive = False
                continue

            # winning condition
            saved_probility = self.days / 100
            if np.random.rand() < saved_probility:
                self.saved = True
                print("Lucky you!!! A ship passby and save you!")
                break
                
            if "Tree branches" in self.inventory:
                num_of_tree_branches = 0
                for item in self.inventory:
                    if item == "Tree branches":
                        num_of_tree_branches += 1
                if num_of_tree_branches >= 3:
                    print("\nYou have enough tree branches now")
                    choice = input("Do you want to make a raft and sail (Y/N): ")
                    if choice == "Y":
                        print("You end your island life and start a new adventure!")
                        break
                    else:
                        print("You decide to stay in the island...for now")
            
            # search the Island
            chosen_area = ask_which_area(self.island_map)
            tile = self.island_map[chosen_area]
            tile.enterTile()
            loot, encounter = tile.search()

            # encounters
            if encounter == "Crocodile":
                is_survived = Encounters.Crocodile("Sword" in self.inventory)
                if is_survived:
                    self.inventory.append("Food")
                    self.inventory.remove("Sword")
                else:
                    self.alive = False
                    continue
                
            elif encounter == "Crumbling Cliffs":
                is_survived = Encounters.Crumbling_Cliffs()
                if not is_survived:
                    self.alive = False
                    continue
            
            elif encounter == "Sea Water":
                is_thirsty = Encounters.Sea_Water()
                if is_thirsty:
                    self.thirst -= 1
                    print("thirst -1")

            # monster
            is_survived = two_head_tiger.hunt(tile.name, "Sword" in self.inventory)
            if not is_survived:
                self.alive = False
                continue

            # finish search
            print("You encounter "+str(encounter)+" and find \n\t==> "+str(loot)+" <==\n")
            self.inventory.append(loot)
            tile.leaveTile()

            # eat and drink
            if "Food" in self.inventory:
                choice = input("Do you want to eat some food? (Y/N)")
                if choice == "Y":
                    print("You eat a piece of food")
                    self.hunger += 2
                    self.inventory.remove("Food")
            if "Water" in self.inventory:
                choice = input("Do you want to drink some water? (Y/N)")
                if choice == "Y":
                    print("Water tastes good!")
                    self.thirst += 2
                    self.inventory.remove("Water")
                
            #This is the start of our player input section. We'll modify this code to make the gameplay fun.
            decision = input("Keep searching the Deserted Island? (Y/N/quit) ")

            if decision == 'quit':
                break
            elif decision == 'Y':
                print("Good choice, maybe you'll survive another day.")
            elif decision == 'N':
                print("Too bad! You're stuck here... Gotta keep searching.")
            else:
                print("I didn't understand. Maybe you've been stuck on this Island for too long...")

            # update info
            self.days += 1
            self.hunger -= 1
            self.thirst -= 1
            
            time.sleep(2)

        # game end
        if self.alive:
            if self.saved:
                print("Congratulations! You survive!")
            else:
                print("You leave the game...")
        else:
            print("Game over. You survived for "+str(self.days)+" days.")