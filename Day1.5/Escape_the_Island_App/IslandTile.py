#! python3.8
# IslandTile.py - the class for island tiles

import numpy as np

class IslandTile:
    
    def __init__(self, name, items, encounters, description):
        self.name = name
        self.items = items
        self.encounters = encounters
        self.description = description
        
        self.discovered = False
        
    def enterTile(self):
        #Your code here
        if self.discovered:
            print("You enter the "+self.name)
        else:
            print(self.description)
            self.discovered = True
            
    def leaveTile(self):
        print("After a long day of searching, you leave "+self.name+" and head back to camp\n")
    
    def search(self):
        encounter = None
        loot = None
        encounter = self.encounters[np.random.randint(len(self.encounters))]
        loot = self.items[np.random.randint(len(self.items))]

        return loot, encounter