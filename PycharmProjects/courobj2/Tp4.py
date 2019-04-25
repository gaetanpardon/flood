from appJar import gui
from dice import Dice
from Masterstate import Master
from datetime import datetime

dice = Dice()
DICE_LABEL = "dice value"

def on_click(button):
    dice.roll()
    ac= datetime.today()
    chaine= str(ac) +":"+str(dice.get_position())
    M.actu(chaine)

    app.setLabel(DICE_LABEL, dice.get_position())
    app.addListItem("caca",chaine)

def on_click2(button):
    M.undo()

app = gui()
M=Master(app,dice)

ac= datetime.today()
chaine= str(ac) +":"+str(dice.get_position())

M.actu(chaine)
app.addLabel(DICE_LABEL, dice.get_position(), 0, 0)
app.addButton("roll", on_click, 0, 1)
app.addButton("undo2", on_click2, 1, 1)
app.addListBox("caca","",1,1)
app.addListItem("caca",chaine)

app.go()