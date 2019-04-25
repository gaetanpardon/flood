from cards import Card


class Deck:



    def __init__(self):
        self.LC=[]
        return

    def add(self,cart):
        if type(cart)==type(Card(1, Card.SPADES)) :
            self.LC.append(cart)

    def __len__(self) :
        return len(self.LC)

    def show_first(self):
        if len(self.LC)==0 :
            return
        else :
            return self.LC[-1]
    def show_last(self):
        if len(self.LC)==0 :
            return
        else :
            return self.LC[0]

    def get(self,pos=-1):
        if len(self.LC)==0 :
            return
        else :
            return self.LC.pop(pos)

    def reset(self):
        self.LC=[]
        for i in range(13) :
            for c in [Card.DIAMONDS, Card.SPADES, Card.CLUBS, Card.HEARTS] :
                self.LC.append(Card(i+1,c))
        return