class Membre:
    def __init__(self, idMembre, nomMembre, adrMembre, cpMembre):
        self.idMembre = idMembre
        self.nomMembre = nomMembre
        self.adrMembre = adrMembre
        self.cpMembre = cpMembre
        self.emprunts = []

    def emprunte(self, idLivre):
        self.emprunts += [idLivre]

    def __str__(self):
        return str(self.idMembre)+","+str(self.nomMembre)+","+str(self.adrMembre)+","+str(self.cpMembre) +","+str(self.emprunts)

    def id(self):
        return self.idMembre