from dice import Dice
from dice import statdice

def test_dice_creation_no_argument():
    dice = Dice()
    assert dice.get_position() == 1
    assert dice.probabilities == [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]


def test_dice_creation_initial_position():
    dice = Dice(position=5)
    assert dice.get_position() == 5
    assert dice.probabilities == [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]


def test_set_position():
    dice = Dice()
    assert dice.get_position() == 1
    dice.set_position(3)
    assert dice.get_position() == 3


def test_roll_no_proba():
    dice = Dice()
    dice.roll()
    assert 1 <= dice.get_position() <= dice.NUMBER_FACES


def test_roll_proba():
    dice = Dice(probabilities=[1, 0, 0, 0, 0, 0])
    dice.roll()
    assert dice.get_position() == 1


def test_statdice() :
    dice = statdice()
    assert dice.stat()==[0,0,0,0,0,0]
    dice.set_position(3)
    assert dice.stat()==[0,0,1,0,0,0]
    assert dice.mean()==[0,0,1,0,0,0]
    dice.roll()
    assert dice.stat()!=[0,0,3,0,0,0]