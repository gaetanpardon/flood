class Card:
    SPADES = "spade"
    HEARTS = "heart"
    CLUBS = "club"
    DIAMONDS = "diamond"

    def __init__(self, value, color):
        self.value = value
        self.color = color

    def __str__(self):
        return "Card(" + str(self.value) + ", " + str(self.color) + ")"

    def __eq__(self, other): #cor
        if Card == type(other) :
            return self.value == other.value and self.color == other.color
        else :
            return False
    def __hash__(self):
        return hash((self.value, self.color))

    def __lt__(self, other):
        return (other.value == 1 and self.value != 1) or 1 < self.value < other.value

    def __gt__(self, other):
        return (self.value == 1 and other.value != 1) or self.value > other.value > 1

    def image(self):
        return "resources/Playing_card_" + self.color + "_" + str(self.value) + ".gif"