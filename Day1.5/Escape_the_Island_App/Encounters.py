#! python3.8
# Encounters.py - control all the important encounter events

import numpy as np

class Encounters:

    @classmethod
    def Crocodile(cls, have_sword: bool):
        print("You encounter a crocodile. What would you do:")
        print("A.run / B.fight / C.use sword to kill this crocodile")
        choice = input("(A / B / C):")
        if choice == "C":
            if have_sword:
                print("You killed the crocodile with the sword and get some \n\t==> food <==.\n")
                print("But your sword was broken.")
                return True
            else:
                print("You do not have a sword yet." , end=" ")

        print("Oops, You become the desserts of this crocodile")
        return False


    @classmethod
    def Crumbling_Cliffs(cls):
        print("You encounter a Crumbling Cliffs.")
        if np.random.rand() < 0.65:
            print("Lucky! The crumbling cliffs do not affect the cliffs below you.\n")
            return True
        else:
            print("The cliffs below you crumble and you fall to your death")
            return False


    @classmethod
    def Sea_Water(cls):
        print("You are suddenlly feel so thirsty, and you see there is ton of sea water in front of you.")
        print("What would you do:")
        print("A.Drink some / B.Drink even more / C.Endure thirst")
        choice = input("(A / B / C):")
        if choice == "C":
            print("You walk away...")
            return False
        else:
            print("You are out of your mind! You become more thirsty...")
            return True