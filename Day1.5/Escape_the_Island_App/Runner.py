#! python3.8
# Runner.py - to run the game

import os
from GameContorller import GameController

class Runner:

    def __init__(self):
        self.number_of_games_played = 0
        self.max_number_of_days_survived = 0
        self.saved_times = 0
        self.playing = True

    def play(self):
        # intro message
        print("Welcome to Escape the Island! A game of survival...")

        while(self.playing):
            os.system("cls")
            newGame = GameController()
            newGame.play()
            self.win_times(newGame.saved)
            self.save_max_number_of_days(newGame.days)
            self.number_of_games_played += 1
            self.playing = self.ask_to_play_again()
        
        print("Game end")
        os.system("pause")

    def save_max_number_of_days(self, days_survived):
        if days_survived > self.max_number_of_days_survived:
            self.max_number_of_days_survived = days_survived

        print("You survived a max number of", self.max_number_of_days_survived, "days!")

    def win_times(self, is_save):
        if is_save:
            self.saved_times += 1

        print("You have been saved", self.win_times, "times!")

    def ask_to_play_again(self):
        while(True):
            play_again = input("Play again? (Y/N): ")
            if play_again == "Y":
                return True
            elif play_again == "N":
                return False
            else:
                print("Invalid input.\n")