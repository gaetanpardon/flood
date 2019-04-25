import random

class Dice :
    #Nface =0
    #Lface = []
    #Lproba =[]
    #Dtype= 'd' # d:a definir ns:numerique simple nc: numérique complex mm:mixte muet mc:mixte cara c:caractére

    def __init__(self,type='d',N=0,Lp=[],Lf=[],pos=0):
        i=0
        self.Nface = 0
        self.Lface = []
        self.Lproba =[]
        self.Dtype= 'd'
        self.pos=0
        s=False
        if "ns"==type :
            if N>0 :
                self.Nface = N
                for i in range(N) :
                    self.Lface.append(i+1)
                self.Nface=N
                self.Dtype=type

        if (type=="ns" or type=="nc") and self.Dtype=='d' :
            if Lf!=[] :
                self.Dtype="nc"
                if N>0 :
                    self.Nface=N
                else :
                    self.Nface=len(Lf)
                s=True
                i=0
                Lor=[]
                for i in range(self.Nface):
                    Lor.append(0)
                for i in range(self.Nface):
                    self.Lface.append(Lf[i])
                    if self.Dtype!="mm" :
                        try :
                            self.Lface[i]=int(Lf[i])
                            if int(Lf[i])<self.Nface and int(Lf[i])>0 :
                                Lor[int(Lf[i])-1]=int(Lf[i])
                            else :
                                s=False
                        except :
                            self.Dtype="mm"
                for i in range(self.Nface):
                    if Lor[i]!=i+1 :
                        s=False

                if s :
                    self.Dtype="ns"
        if pos>0 and pos<=self.Nface :
            self.pos=pos


        return

    def get_position (self):
        if self.Dtype=="ns" :
            return(self.pos+1)
        else :
            return (self.Lface[self.pos])

    def set_position (self,pos) :
        if pos>0 and pos<=self.Nface :
            self.pos=pos
        return (self.pos)
    def roll(self):
        v=random.randint(0,self.Nface)
        r=self.set_position(v)
        if r!=v :
            print("echec")