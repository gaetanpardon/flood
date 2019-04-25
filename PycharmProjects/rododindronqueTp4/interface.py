import sqlite3, os, sys
from surface import Membre


class MembreDAO:
    def __init__(self, db_name):
        try:
            assert os.path.isfile(db_name)
            db = sqlite3.connect(db_name)
            print("Connexion à ", db_name, "OK.")
            self.db = db
        except:
            print("Erreur de connexion : la base n'existe pas!")
            sys.exit()


    def getMembreById (self,id):
        try:
            liste_tuples = self.db.execute("SELECT * from Membre where IdMembre="+str(id)).fetchall()
            #print(liste_tuples)
            if liste_tuples!=[]:
                m=Membre(liste_tuples[0][0],liste_tuples[0][1],liste_tuples[0][2],liste_tuples[0][3])
                self.exemprM(m)
                return m
            else:
                return None
        except sqlite3.OperationalError as err:
            print("Erreur SQL ok:" + err.args[0])

    def aempr(self,m):
        Lempr = []
        try:
            liste_tuples = self.db.execute("SELECT * from emprunt where IdMembre=" + str(m.id())).fetchall()
            for t in liste_tuples:
                Lempr.append(t)

        except sqlite3.OperationalError as err:
            print("Erreur SQL :" + err.args[0])
        return Lempr

    def exemprM(self,m):
        L = self.aempr(m)
        for elt in L:
            m.emprunte(elt[0])
        return None

    def createMembre(self,m):
        if self.getMembreById(m.id())==None :
            try:
                self.db.execute("INSERT INTO Membre VALUES (?,?,?,?)",
                        (m.idMembre, m.nomMembre, m.adrMembre, m.cpMembre))
                #self.Nempr(m,m.emprunts)
            except  sqlite3.OperationalError as err:
                print("Erreur SQL :" + err.args[0])

        return None



    """
    def Nempr(self,m,Le):
        for elt in Le :
            #print(elt,m.idMembre)
            try:
                self.db.execute("INSERT INTO Membre VALUES (?,?,0,NULL)",(elt,m.idMembre))
            except  sqlite3.OperationalError as err:
                print("Erreur SQL :" + err.args[0])
        return None
    #"""

    def deleteMembre (self,m) :
        if self.getMembreById(m.id())==None :
            try:
                self.db.execute("(DELETE FROM Membre WHERE IdMembre=)"+str(m.id))

            except  sqlite3.OperationalError as err:
                print("Erreur SQL :" + err.args[0])
