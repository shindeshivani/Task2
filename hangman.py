import random 
class hangman:   
    def __init__(self) -> None:
        pass
    def man(self,lives):
        man_struct=[

"""-----------
     |   |
     O   |
    /|\\  |
    / \\  |
         |                                                                                                                                                       |
===========""",
"""---------
      |   |
      O   |
     /|\\  |
     /    |
          |                                                                                                                                                    |
============""",
"""-----------
      |   |
      O   |
     /|\\  |
          |
          |                                                                                                                                                       |
 ============""",
 """-----------
       |   |
       O   |
      /|   |
           |
           |                                                                                                                                                       |
==============""",  
"""------------
      |   |
      O   |
      |   |
          |
          |
==============""", 
"""-------------
       |   |
       O   |
           |
           |
           |                                                                                                                                                       |
============"""]
        return man_struct[lives]
    
    def guess_word(self):
        print("\nLet's start the game.")
        print("You have 6 lives to guess.")
        words=['apple','orange','pineapple','mango','grape','kiwi','banana','pear','papaya','']
        guessword=random.choice(words)
        lives=6
        guessed=False
    
        guess_letter=[ '_' for _ in guessword]
        # print(guess_letter)
        guess_set=set()

        while  '_' in guess_letter and lives>=1:
            print("\nCurrent state :\t"," ".join(guess_letter))
            # print(guess_letter)
            user_input=input("Enter the letter :\t").lower()

            if len(user_input)!=1 or not user_input.isalpha():
                print("Enter single letter input.\n")
                continue

            if user_input in guess_set and user_input in guessword: 
                print("You already guessed {}, which is in word.".format(user_input))
                
            guess_set.add(user_input)
            

            if user_input in guessword:
                for i ,letter in enumerate(guessword):
                    if letter==user_input:
                        guess_letter[i]=user_input
                print("Good guess!")        
                # print('Good guess: ', ''.join(guess_letter))         
              
                               
            else:
                lives-=1
                print("incorrect input, you have {} lives".format(lives))
                print(self.man(lives))
            
            if '_' not in guess_letter:
                guessed=True
                print("Congratulations! You guessed the word : ","".join(guess_letter))

        if not guessed:
            print("The word was {}.\nYou run out off live, try again later.\n".format(guessword))    
            # print(self.man(lives)) 

    def play_again(self):
        user_in=input("Do you want to play again? Y\\N:\n").lower()
        if user_in=='y':
            self.loop()
        elif user_in=='n':
            self.end_game()
        else:
            print("Enter correct input.")
            self.play_again()

    def end_game(self):
        print("See you soon!")        
 

    def loop(self):
        self.guess_word()
        self.play_again()          

obj=hangman()
obj.loop()




        