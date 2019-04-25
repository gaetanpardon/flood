

import numpy.random


class Dice:
    NUMBER_FACES = 6

    def __init__(self, position=1, probabilities=None):
        self.position = position
        if probabilities:
            self.probabilities = probabilities
        else:
            self.probabilities = [1 / self.NUMBER_FACES] * self.NUMBER_FACES

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position

    def roll(self):
        self.set_position(numpy.random.choice([i for i in range(1, self.NUMBER_FACES + 1)], p=self.probabilities))

    def setproba (self , probabilities=[]) :
        Lp=[0,0,0,0,0,0]
        s=0
        v=0
        for i in range(self.NUMBER_FACES) :
            try :
                a=int(probabilities[i-1])
            except :
                a=-1
            if a>=0 :
                s+=a
            else :
                v+=1
            Lp[i-1]=a
            print(a)
        for i in range(self.NUMBER_FACES):
            if Lp[i - 1]<0 :
                Lp[i-1]=int((1-s)/v)
        print(Lp)
        if s>=0 and s<=1 :
           self.probabilities=Lp

class statdice (Dice) :

    def __init__(self, position=1, probabilities=None):
        super().__init__( position, probabilities)
        self.Lp=[0,0,0,0,0,0]

    def set_position(self, new_position=1):
        super().set_position(new_position)
        self.Lp[new_position-1]=self.Lp[self.get_position()-1]+1

    def stat (self) :
        return (self.Lp[:])
    """def roll(self):
        super().roll()
        self.Lp[self.get_position()-1]=self.Lp[self.get_position()-1]+1"""


    def mean (self) :
        s=0
        for elt in self.Lp :
            s+=elt
        if s!=0 :
            Ls=[]
            for elt in self.Lp :
                Ls.append(elt/s)
            return (Ls)
        else :
            return ([0,0,0,0,0,0])

    def reset(self):
        self.set_position()
        self.Lp=[0,0,0,0,0,0]