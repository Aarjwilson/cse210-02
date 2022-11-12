from game.card import Card

class Director:
    def __init__(self):
        """
        Initialize the default values and create the two card objects.
        """
        self.is_playing = True
        self.hiLo = ""
        self.score = 300 # Player starts out with 300 points.

        self.current_card = Card()
        self.next_card = Card()

    def start_game(self):
        """
        This will make for a one shot start of the game on main.py

        this is where we will get the starting card number and, while
        game is still running, where all the functions will be called.
        """
        self.current_card.draw_card()

        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()
            self.play_again()
            

    def get_inputs(self):
        """
        Here we will display the first card and ask the player if it is Higher or lower.
        """
        print(f"\nThe card is: {self.current_card.value}")
        self.hiLo = input("Higher or Lower? [h/l] ")

    def do_updates(self):
        """
        Here we will generate the next card number and compare it to the players guess.
        points addition or subtraction will be determined by the results

        if score reachs "0" game over will be generated.
        """
        self.next_card.draw_card()

        if self.hiLo.lower() == "h" and self.next_card.value > self.current_card.value: #Correctly Guessed High
            self.score += 100
        elif self.hiLo.lower() == "l" and self.next_card.value < self.current_card.value: #Correctly Guessed Low
            self.score += 100
        elif self.hiLo.lower() == "h" and self.next_card.value < self.current_card.value: #Incorrectly Guessed High
            self.score -= 75
        elif self.hiLo.lower() == "l" and self.next_card.value > self.current_card.value: #Incorrectly Guessed Low
            self.score -= 75
        #Seperate if statement to determine if game should be stopped sooner.
        if self.score <= 0:
            self.is_playing = False

    def do_outputs(self):
        """
        Here we will print off the response, including the game over statement if 
        score reaches 0
        """
        print(f"Next card was: {self.next_card.value}")
        print(f"Your score is: {self.score}")

        if self.score <= 0:
            print("\nGame Over!\n")

    def play_again(self):
        """
        If not Game Over then the player can decide to play again or not.

        If game continues then the next card value will now be the currently cards value for the next round.
        """
        if self.is_playing:
            play = input("Play again? [y/n] ")

            if play.lower() == "y":
                self.current_card.value = self.next_card.value
                self.next_card = Card() #set next card to default
            elif play.lower() == "n":
                self.is_playing = False
        
        else:
            print("Thank you for playing!")

        
