class Employe:
    def __init__(self, nom_complet, fonction, date_de_naissance, salaire):
        self.nom_complet = nom_complet
        self.fonction = fonction
        self.date_de_naissance = date_de_naissance
        self.salaire = salaire
    def mieux_paye_que(self , Emp) :
        return self.salaire>Emp.salaire

class Departement :
    def __init__(self,numDep,description,Le=[]):
        self.numDep=numDep
        self.description=description
        self.Le=Le

    def ajouteEmploye(self,emp) :
        self.Le.append(emp)

    def coutDep(self) :
        s=0
        for e in self.Le :
            s+=e.salaire
        return s
    def plusCouteuxQue(self,dep) :
        return self.coutDep() > dep.coutDep()