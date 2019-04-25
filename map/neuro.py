import math

def neuro (E,Lp,Le) : #lp [f,e1,e2,e3...]
    x=0
    for i in range(E) :
        x+=Lp[i+2]*Le[i]

    sign= 1 - 2/(1+math.exp(Lp[0]*x))
    return (sign)

#class Rneuro (Lgn) :

def basetopo (Lgn,dm45,d0,dp45,pa,fx,fy,px,py) : #len(Lgn) = 40
    Ll1 = [[3, 9, 6, 0],
           [10, 6, 9, 1],
           [2, 0, 13, 11],
           [8, 1, 4, 10],
           [4, 5, 2, 8],
           [2, 13, 5, 1],
           [12, 6, 9, 3],
           [0, 7, 12, 11],
           [4, 8, 10, 6],
           [13, 4, 0, 12],
           [2, 3, 7, 4],
           [9, 5, 11, 3],
           [8, 9, 12, 0],
           [4, 3, 2, 8]
           ]
    Ll2 = [[4, 10, 0, 8, 5],
           [6, 5, 4, 0, 12],
           [1, 7, 13, 6, 3],
           [5, 7, 11, 2, 8],
           [4, 1, 12, 7, 0],
           [3, 11, 6, 5, 9],
           [9, 11, 2, 13, 7],
           [13, 9, 10, 4, 8]
           ]
    Ll3m = [[0, 2, 6, 5, 3],
            [6, 4, 0, 2, 1],
            [3, 4, 1, 7, 5]
            ]
    Ll4 = [[2, 1],
           [1, 2],
           [2, 0],
           [1, 0],
           [2, 0]
           ]
    Ll5s = [[3, 2, 4, 1],
             [2, 0, 1, 3],
             [4, 1, 3, 0],
             [0, 2, 4, 3],
             ]

    LLl=[Ll1,Ll2,Ll3m,Ll4,Ll5s]

    dm20=neuro(2,Lgn[0],[dm45,d0])
    dp20=neuro(2,Lgn[1],[dp45,d0])
    d0a=neuro(3,Lgn[2],[dm20,pa,dp20])
    vpx=neuro(2,Lgn[3],[px,fx])
    vpy=neuro(2,Lgn[4],[py,fy])
    vdxya=neuro(3,Lgn[5],[vpx,vpy,pa])
    Lem = [dm45, d0, dp45, pa, fx, fy, px, py,dm20,dp20,d0a,vpx,vpy,vdxya]
    ineuro = 5
    for Lli in LLl :
        Lr=[]
        for Leneu in Lli :
            ineuro+=1
            Le=[]
            for e in Leneu :
                Le.append(Lem[e])
            sn=neuro(len(Leneu),Lgn[ineuro],Le)
            Lr.append(sn)
        Lem=Lr[:]
    return (Lem[0]*12,Lem[1]*12,Lem[3]*Lgn[ineuro+1][0]+px,Lem[4]*Lgn[ineuro+1][2]+py)





