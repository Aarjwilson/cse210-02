from game.card import Card

class Director:
    def __init__(self):
        self.is_playing = True
        self.score = 0
        self.total_score = 300

        card = Card()

    def start_game(self):
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        draw_card = input("Higher or Lower? [h/l] ")
        
