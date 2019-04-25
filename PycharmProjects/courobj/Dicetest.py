from Obj import Dice

def test_dice_creation_no_argument():
    d = Dice()
    assert d.get_position() == 1


def test_dice_creation_initial_position():
    d = Dice(position=5)
    assert d.get_position() == 5


def test_set_position():
    d = Dice()
    assert d.get_position() == 1
    d.set_position(3)
    assert d.get_position() == 3


def test_roll():
    d = Dice()
    d.roll()
    assert 1 <= d.get_position() <= d.NUMBER_FACES