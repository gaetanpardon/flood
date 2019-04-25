import math

class forme :

    def __init__(self,Cx,Cy,R):
        self.FSR=R
        self.FScx=Cx
        self.FScy = Cy

    def move(self,x,y):
        self.FScx += x
        self.FScy += y

    def laser(self,Ox,Oy,A):
        # (dcos+x-fx)²=dcos²+x²+fx²+2dcosx-2dcosfx-2xfx
        b=math.cos(A)*(2*Ox-2*self.FScx)+math.sin(A)*(Oy-2*self.FScy)
        c=self.FSR**2-self.FScx**2-self.FScy**2-Ox**2-Oy**2+2*Ox*self.FScx+2*Oy*self.FScy

        d=b**2+4*c
        #print(b,c,d) débug
        if d>=0 :
            print(b,math.sqrt(d))
            dis=(-b-math.sqrt(d))/2

            if dis>0 :
                print("cas1")
                return (dis)
            else :
                dis = (-b + math.sqrt(d)) / 2
                if dis > 0:
                    print("cas2")
                    return (dis)
                else:
                    return (0)
        else :
            return (0)
    def coorS(self):
        return (self.FScx,self.FScy,self.FSR)
    def contact(self,O2):
        x,y,R=O2.coorS()
        #print(x,y,R)#debug
        dc=math.sqrt((x-self.FScx)**2+(y-self.FScy)**2)
        #print(dc,self.FSR,R)#debug
        if dc<=R+self.FSR and self.FSR<=R+dc and R<=dc+self.FSR :
            return (1)
        else:
            return (0)
