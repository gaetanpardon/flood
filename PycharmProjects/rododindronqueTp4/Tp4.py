import sqlite3
import os, sys
from surface import Membre
from interface import MembreDAO

def connecte_base(db_name):
    try:
        assert os.path.isfile(db_name)
        db = sqlite3.connect(db_name)
        print("Connexion à ", db_name, "OK.")
        return db
    except:
        print("Erreur de connexion : la base n'existe pas!")
        sys.exit()


db = connecte_base("biblio.db")
c = db.cursor()

try:
    liste_tuples = c.execute("SELECT * from livre ").fetchall()
    for t in liste_tuples:
        print(t)
except sqlite3.OperationalError as err:
    print("Erreur SQL :" + err.args[0])


m=Membre(12,"rododigne","nez ixpas",4444 )


t1=m.idMembre
t2=m.nomMembre
t3=m.adrMembre
t4=m.cpMembre

print(t1,t2,t3,t4)


m.emprunte("7089PQIU")

print(m.emprunts)
mrodo=m
Lp=[]
try:
    liste_tuples = c.execute("SELECT * from membre ").fetchall()
    for t in liste_tuples:
        m=Membre(t[0],t[1],t[2],t[3])
        Lp.append(m)
        print(t)
except sqlite3.OperationalError as err:
    print("Erreur SQL :" + err.args[0])

print(Lp)
print(m)
#"""
try:
    liste_tuples = c.execute("SELECT * from emprunt ").fetchall()
    for t in liste_tuples:
        print(t)
except sqlite3.OperationalError as err:
    print("Erreur SQL :" + err.args[0])
#"""


def aempr(m) :
    Lempr=[]
    try:
        liste_tuples = c.execute("SELECT * from emprunt where IdMembre="+str(m.id())).fetchall()
        for t in liste_tuples:
            Lempr.append(t)

    except sqlite3.OperationalError as err:
        print("Erreur SQL :" + err.args[0])
    return Lempr

def exemprM(m) :
    L=aempr(m)
    for elt in L :
        m.emprunte(elt[0])
    return None

for elt in Lp :
    exemprM(elt)
    print(elt)

a=MembreDAO("biblio.db")

print(a.getMembreById(12))
a.createMembre(mrodo)