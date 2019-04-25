import math
import random

class Forme:  # definition of a basic forme, from wich will derive the car forme

    def __init__(self, center_x, center_y, radius):
        self.forme_radius = radius
        self.forme_center_x = center_x
        self.forme_center_y = center_y


    def move(self, x, y):
        self.forme_center_x += x
        self.forme_center_y += y

    def laser(self, Ox, Oy, A):
        # (dcos+x-fx)²=dcos²+x²+fx²+2dcosx-2dcosfx-2xfx
        b = math.cos(A) * (2 * Ox - 2 * self.forme_center_x) + math.sin(A) * (Oy - 2 * self.forme_center_y)
        c = self.forme_radius ** 2 - self.forme_center_x ** 2 - self.forme_center_y ** 2 - Ox ** 2 - Oy ** 2 + 2 * Ox * self.forme_center_x + 2 * Oy * self.forme_center_y

        d = b ** 2 + 4 * c
        # print(b,c,d) débug
        if d >= 0:
            dis = (-b - math.sqrt(d)) / 2

            if dis > 0:
                return (dis)
            else:
                dis = (-b + math.sqrt(d)) / 2
                if dis > 0:
                    return (dis)
                else:
                    return (0)
        else:
            return (0)

    def coorS(self):
        return (self.forme_center_x, self.forme_center_y, self.forme_radius)

    def contact(self, O2):
        x, y, R = O2.coorS()
        # print(x,y,R)#debug
        dc = math.sqrt((x - self.forme_center_x) ** 2 + (y - self.forme_center_y) ** 2)
        # print(dc,self.forme_radius,R)#debug
        if dc <= R + self.forme_radius and self.forme_radius <= R + dc and R <= dc + self.forme_radius:
            return (1)
        else:
            return (0)

    def getcoor(self):
        return (self.forme_center_x ,self.forme_center_y)


class Car(Forme):
    def __init__(self, center_x, center_y, radius, cp,Rroue,Iroue):
        super().__init__(center_x, center_y, radius)
        self.A = 0
        self.cp = cp#capacité capteut
        self.Lc = [-math.pi / 4, 0, math.pi / 4]#liste capteur
        self.Rroue=Rroue#rayon roue
        self.Iroue=Iroue
        self.vg=0
        self.vd=0

    def RAZ (self) :
        self.forme_center_x = 0
        self.forme_center_y=0
        self.forme_radius =0
        self.vg = 0
        self.vd = 0
        self.A = 0

    def rlaser(self, LO):
        Ld = []
        for c in self.Lc:
            dm = self.cp
            for O in LO:
                d = O.laser(self.forme_center_x, self.forme_center_y, c + self.A) - self.forme_radius
                if d < dm and d>0:
                    dm = d
            Ld.append(dm)
        return (Ld)


    def move(self, x, y,a):
        super().move(x,y)
        self.A+=a


    def moveR(self ,vd,vg) :
        x=self.Rroue/2*( vd + vg )*math.cos(self.A)
        y = self.Rroue / 2 * (vd + vg) * math.sin(self.A)
        a=self.Rroue/self.Iroue *(vd-vg)

    def moteur(self,cr,v):
        return (math.pi*cr/120+v/2)
    def moveC (self,crd,crg):
        self.vd=self.moteur(crd,self.vd)
        self.vg = self.moteur(crg, self.vg)



    def getcoor(self):
        return (self.forme_center_x ,self.forme_center_y,self.A)



class Carte :
    def __init__(self, Msize, tgO):
        self.wall=Forme(0,0,Msize)
        self.car=Car(0,0,15,45,3,10)
        d=random.uniform(-Msize+30,Msize-30)
        a=random.uniform(-math.pi,math.pi)
        self.arri=Forme(d*math.cos(a),d*math.sin(a),10)
        self.LO=[self.wall]
        for itgO in range(tgO) :
            t=Forme(random.uniform(-Msize,Msize),random.uniform(-Msize,Msize),random.uniform(0,25))
            if self.car.contact(t) ==0 and self.arri.contact(t) :
                self.LO.append(Forme(t.self.forme_center_x,t.forme_center_y,t.radius))


    def laserma(self):
        Ld=self.car.rlaser(self.LO)

    def life(self):
        carlife=True
        for O in self.LO :
            if self.car.contact(O) != 0 :
                carlife=False
        return (carlife)