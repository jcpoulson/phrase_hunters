import random
from phrasehunter.phrase import Phrase

class Game:
    def __init__(self):
        self.missed = 0
        self.lives = 5
        self.phrases = [Phrase('Playstation Four'), Phrase('Matcha Soda'), Phrase('Demon Slayer'), Phrase('Finishing This Fight'), Phrase('Team Treehouse')]
        self.active_phrase = None
        self.guesses = []

    def welcome(self):
        print("\n\nHello There, welcome to the phrase hunters game, try and complete the phrase in a limited number of tries\n")

    def get_random_phrase(self):
        rand_phrase = random.choice(self.phrases)
        return rand_phrase

    def get_guess(self):
        ask = input("\n\nGuess a letter within the phrase: ")
        if len(ask) > 1:
            raise ValueError("\nYou entered more than one letter")
        elif ask.isalpha() != True:
            raise ValueError("\nYou entered an invalid character")
        print()
        return ask.lower()

    def game_over(self):
        print("\n\nSorry, You ran out of tries")
    
    def start(self):
        self.welcome()
        self.active_phrase = self.get_random_phrase().phrase
        phrase = Phrase(self.active_phrase)
        phrase.display()
        while True:
            try:
                guess = self.get_guess()
                # if a player guesses the same letter twice
                if guess in self.guesses:
                    print("You already guessed this letter, try a different one \n")
                    phrase.redisplay(guess)
                elif guess not in self.active_phrase.lower():
                    self.guesses.append(guess)
                    self.missed += 1
                    self.lives -= 1
                    phrase.check_letter(guess)
                    print("\n\nyou guessed wrong\n")
                    print("you have {} out 5 tries left\n".format(self.lives))
                    phrase.redisplay(guess)
                elif guess in self.active_phrase.lower():
                    self.guesses.append(guess)
                    print("\nyou guessed right\n\n")
                    self.guesses.append(guess)
                    phrase.check_letter(guess)
                    phrase.redisplay(guess)
                    check = phrase.check_complete()
                    if check == True:
                        break
                if self.lives == 0:
                    self.game_over()
                    break
            except ValueError as err:
                print("{}".format(err))
