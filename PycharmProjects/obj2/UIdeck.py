from appJar import gui

from cards import Card
from deck import Deck


app = gui()


app.addLabelOptionBox("color", [Card.DIAMONDS, Card.SPADES, Card.CLUBS, Card.HEARTS], 0, 0)
app.addLabelOptionBox("value", [str(i) for i in range(1, 14)], 0, 1)

dc=Deck()
dd=Deck()

def actualise() :
    c = dc.show_first()
    if c == None:
        app.setImage("card_image", "resources/empty.gif")
    # color = app.getOptionBox("color")
    # value = app.getOptionBox("value")
    else:
        app.setImage("card_image", c.image())

    cd = dd.show_first()
    if cd==None :
        app.setImage("card_imageD", "resources/empty.gif")
    else :
        app.setImage("card_imageD", cd.image())
    app.setLabel("card", str(len(dc)))

def on_click(button):
    actualise()

def on_clickR(button):
    dc.reset()
    actualise()


def on_clickP(button):
    c=dc.get(0)
    dd.add(c)
    actualise()


def on_clickA(button):
    color = app.getOptionBox("color")
    value = app.getOptionBox("value")
    dc.add(Card(value,color))
    actualise()


#app.addButton("show card", on_click, 2, 0)
app.addButton("addcard",on_clickA,2,0)
app.addButton("RAZ", on_clickR, 1, 0)
app.addLabel("card",str(len(dc)),1,1)
app.addButton("Pioch", on_clickP, 2, 1)

app.addImage("card_image", "resources/empty.gif", 3, 0,1)
app.addImage("card_imageD", "resources/empty.gif", 3, 1,1)


app.go()