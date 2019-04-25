from cards import Card
from deck import Deck

def test_str():
    assert str(Card(1, Card.SPADES)) == 'Card(1, spade)'


def test_card_equality():
    assert Card(1, Card.SPADES) == Card(1, Card.SPADES)
    assert Card(1, Card.SPADES) != Card(1, Card.DIAMONDS)

    assert Card(1, Card.SPADES) != Card(13, Card.DIAMONDS)


def test_card_lesser_than():
    assert not Card(3, Card.SPADES) < Card(3, Card.SPADES)
    assert Card(2, Card.SPADES) < Card(3, Card.SPADES)


def test_card_larger_than():
    assert not Card(3, Card.SPADES) > Card(3, Card.SPADES)
    assert Card(3, Card.SPADES) > Card(2, Card.SPADES)


def test_image():
    assert Card(11, Card.DIAMONDS).image() == "resources/Playing_card_diamond_11.gif"



def test_deck_creation():
    deck = Deck()
    assert deck != None

def test_deck_empty_at_creation():
    deck = Deck()
    assert len(deck) == 0

def test_add_card():
    deck = Deck()
    deck.add(Card(1, Card.SPADES))
    assert len(deck) == 1



def test_show_first():
    deck = Deck()
    deck.add(Card(1, Card.SPADES))
    deck.add(Card(2, Card.SPADES))
    assert deck.show_first() == Card(2, Card.SPADES)

def test_show_last():
    deck = Deck()
    deck.add(Card(1, Card.SPADES))
    deck.add(Card(2, Card.SPADES))
    assert deck.show_last() == Card(1, Card.SPADES)


def test_get_empty_deck():
    deck = Deck()

    assert deck.get() == None

def test_get_first():
    deck = Deck()
    deck.add(Card(1, Card.SPADES))
    deck.add(Card(2, Card.SPADES))
    card = deck.get()

    assert card == Card(2, Card.SPADES)
    assert len(deck) == 1

def test_reset() :
    deck = Deck()
    deck.reset()
    assert len(deck)==52

