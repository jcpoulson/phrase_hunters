import sys
from phrasehunter.game import Game 

if __name__ == '__main__':
    while True:
        game = Game()
        game.start()
        while True:
            try:
                play_again = input("\nWould you like to play again: Y/N > ")
                if play_again == 'n':
                    print("\nThanks for playing\n")
                    sys.exit()
                elif play_again == 'y':
                    break
                elif play_again != 'y' or 'n':
                    raise ValueError("Please enter either Y or N: ")
            except ValueError as err:
                print("{}".format(err))

