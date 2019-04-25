from appJar import gui

from cards import Card


app = gui()


app.addLabelOptionBox("color", [Card.DIAMONDS, Card.SPADES, Card.CLUBS, Card.HEARTS], 0, 0)
app.addLabelOptionBox("value", [str(i) for i in range(1, 14)], 0, 1)


def on_click(button):
    color = app.getOptionBox("color")
    value = app.getOptionBox("value")
    app.setImage("card_image", Card(int(value), color).image())

app.addButton("show card", on_click, 1, 0, 2)


app.addImage("card_image", "resources/empty.gif", 2, 0, 2)


app.go()