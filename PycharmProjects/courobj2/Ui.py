

from appJar import gui
from dice import statdice

app = gui()
#app.setGeometry(200, 200)

def refresh() :
    app.setLabel("dice", str(dice.get_position()))
    app.setLabel("moy", str(dice.mean()))
    app.setLabel("lancer", str(dice.stat()))
    return


def press_roll(button):
    dice.roll()
    refresh()
    return

def press_roll10(button):
    for i in range(10) :
        dice.roll()
    refresh()
    return

def press_roll100(button):
    for i in range(100) :
        dice.roll()
    refresh()
    return
def press_rollM(button):
    for i in range(1000000) :
        dice.roll()
    refresh()
    return

def get_integer(button):
    print(app.getEntry("user_entry"))
    try :
        r=int(app.getEntry("user_entry"))
    except :
        r=0
    print(r)
    for i in range(r) :
        dice.roll()
    refresh()
def reset(button) :
    dice.reset()
    refresh()
def setprob(button) :
    entre=(app.getEntry("user_entry"))
    L=entre.split(",")
    dice.setproba(L)

dice = statdice()
app.addLabel("position", "Position : ", 0, 0)
app.addLabel("dice", str(dice.get_position()), 0, 1)
app.addButton("Roll", press_roll, 0, 2)
app.addButton("Roll10", press_roll10, 0, 3)
app.addButton("Roll100", press_roll100, 0, 4)
app.addButton("RollM", press_rollM, 0, 5)
app.addLabel("user_int", "Custom rolls (int) : ", 1, 0)
app.addEntry("user_entry", 1, 1)
app.addButton("OK", get_integer, 1, 3)
app.addButton("reset", reset, 1, 4)
app.addLabel("moy",str(dice.mean()),2,0)
app.addLabel("lancer",str(dice.stat()),3,0)
app.addEntry("probal", 4, 0)
app.addButton("OK2", setprob, 4, 3)
app.go()