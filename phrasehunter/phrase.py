class Phrase:
    def __init__(self, phrase):
        self.phrase = phrase
        self.correct_guesses = 0
        self.right_letters = []
    
    def display(self):
        for letter in self.phrase:
            if letter == ' ':
                print(' ', end=" ")
            else:
                print('_', end=" ")
    
    # This method unlike display takes the guess argument and uses the guess argument to redisplay 
    # the phrase to the screen, this time with added letters
    def redisplay(self, guess):
        for letter in self.phrase.lower():
            if letter == guess:
                if guess not in self.right_letters:
                    self.right_letters.append(guess)
        for letter in self.phrase.lower():
            if letter not in self.right_letters:
                if letter == ' ':
                    print(' ', end=" ")
                else:
                    print('_', end=" ")
            if letter in self.right_letters:
                print(letter, end=" ")

    def check_letter(self, guess):
        if guess in self.phrase:
            self.correct_guesses += 1
            
    # This method uses """.join(set(self.phrase))" to pull just the letters one time that go 
    # into phrase, for example if "E" shows up twice in the phrase, it will only show up once in this new list
    # then compares that list to the right_letters list
    def check_complete(self):
        spaces = 0
        phrase_length = "".join(set(self.phrase))
        
        for letter in self.phrase:
            if letter == ' ':
                spaces += 1
        if (len(self.right_letters) + spaces) == len(phrase_length):
            print("\n\nCongratualtions, you just won the game")
            return True