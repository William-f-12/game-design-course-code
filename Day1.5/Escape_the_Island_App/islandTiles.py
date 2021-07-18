#! python3.8
# islandTiles.py - all info about different on the island

from IslandTile import IslandTile

camp = IslandTile("your campsite",("A dead bird", "Some fish bones"),("Your safe home!"),"You are back at your meager camp")

temple = IslandTile(

    "temple",
    
    ("Golden Monkey Statuette", "Sword"),
    
    ("Boulder Trap",),
    
    "As you push your way through the thick vegetation, you stumble upon an ancient Temple standing stalwart in a small clearing. The area around the temple seems quiet. Too quiet..."
    
    )

beach = IslandTile(

    "beach",

    ("Sand", "More Sand", "Even More Sand"),

    ("Birds", "Crabs", "A Dead Fish", "A message in a bottle", "a beat up Practice Dummy"),

    "You emerge from the jungle onto the beach. 'If I weren't stuck here, this beach would be a beautiful place,' you think to yourself bitterly."
    
    )

spring = IslandTile(
    
    "spring",
    
    ("Water", "Water", "Water", "Water", "Water", "Food"),
    
    ("Crocodile", "Nothing", "a small deer"),
    
    "The soft gurgle of water leads you up a small bluff to reveal a small spring, its waters bubbling out of the rocks."
    
    )

ravine = IslandTile(
    
    "ravine",
    
    ("Rock", "Food", "Tree branches"),
    
    ("Crumbling Cliffs", "Scenic views", "A fallen tree","The meaning of life, the universe, and everything"),
    
    "There is barely any warning as you emerge from the jungle and find yourself facing a massive ravine. You look precariously over the edge, but it is so deep you cannot see the bottom"
    
    )

shallow = IslandTile(
    
    "shallow",
    
    ("Food", "Food", "Sea Water"),
    
    ("Many fishes", "Sea Water", "Beautiful shells"),
    
    "A beauti area of beach, shallow water with some beautiful fishes swim in it. You can take a nice bath here."
    
    )

island_map = {

    "camp": camp,
    
    "temple": temple, 

    "beach": beach, 
    
    "spring": spring, 
    
    "ravine": ravine, 

    "shallow": shallow,
    
    }

def ask_which_area(all_areas: list):
    """let player choose which area they want to search"""

    areas = ", ".join(all_areas)
    while True:
        chosen_area = input("Where would you like to search today? (%s): " % areas)
        if chosen_area in all_areas:
            break
        
        print("Unkown area, please pick again.")
    
    return chosen_area