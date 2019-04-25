from appJar import gui

class statu :
    def __init__ (self , vd ,chaine, prstatu=None) :
        self.D=vd
        self.memoire = []
        L=[]
        if prstatu == None :
            L=[]
        else :
            L=prstatu.getL()
        print(L)
        self.memoire=L.append(chaine)
    def getL(self):
        return self.memoire

    def getA(self):
        return (self.D,self.memoire)


class Master :
    def __init__(self,app,dice):
        self.old=[]
        self.position=0
        self.Pvapp=app
        self.dice=dice
    def actu(self,C):
        ch=C
        self.old = self.old[:self.position]
        if self.position==0 :
            prst=None
        else :
            prst=self.old[-1]
        s= statu(self.dice.get_position(),ch,prst)
        self.old.append(s)
        self.position+=1
    def undo(self):
        if self.position>0 :
            self.position-=1
            s=self.old[self.position]
            self.restore(s)
    def restore(self,s):
        vd,Lch = s.getA()
        self.app.clearListBox()
        self.app.setListItem("caca", Lch)
        self.dice.set_position(vd)
        self.app.setLabel("dice value", self.dice.get_position())

    def redo(self):
        if self.position<len(self.old)-1 :
            self.position+=1
            s=self.old[self.position]
            self.restore(s)

