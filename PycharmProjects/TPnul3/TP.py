import sqlite3
import os, sys


def connecte_base(db_name):
    try:
        assert os.path.isfile(db_name)
        db = sqlite3.connect(db_name)
        print("Connexion à ", db_name, "OK.")
        return db
    except:
        print("Erreur de connexion : la base n'existe pas!")
        sys.exit()


db = connecte_base("foodmart.db")

c = db.cursor()

try:
    c.execute("SELECT * FROM employee")
except sqlite3.OperationalError as e:
    print("Erreur SQL :" + e.args[0])


liste_tuples = c.fetchall()
for t in liste_tuples:
    print(t)

"""
db = connecte_base("foodmart.db")
c = db.cursor()
try:
    c.execute("SELECT employee_id, full_name FROM employee")
    liste_tuples = c.fetchall()
    for t in liste_tuples:
        num_employe = t[0];
        nom = t[1];
        print(num_employe , nom);
except sqlite3.OperationalError as e:
    print("Erreur SQL :" + e.args[0])
#"""
#"""
db = connecte_base("foodmart.db")
c = db.cursor()
try:
    c.execute("SELECT count(employee_id) FROM employee Where salary>10000")
    liste_tuples = c.fetchall()
    for t in liste_tuples:
        num_employe = t[0];

        print(num_employe);
except sqlite3.OperationalError as e:
    print("Erreur SQL :" + e.args[0])
#"""
#"""
db = connecte_base("foodmart.db")
c = db.cursor()
try:
    c.execute("SELECT T1.employee_id, T1.full_name , T1.position_title , T1.birth_date , T1.salary FROM employee T1 INNER JOIN employee T2 on T1.supervisor_id=T2.employee_id Where T2.full_name='Mona Jaramillo'")
    liste_tuples = c.fetchall()
    for t in liste_tuples:
        num_employe = t[0];
        print(t);
except sqlite3.OperationalError as e:
    print("Erreur SQL :" + e.args[0])

#"""
#"""
from employee import Employe as Emp

e= Emp(t[1],t[2],t[3],t[4])

print(e.nom_complet, e.fonction, e.date_de_naissance , e.salaire)

#"""
#"""
Le=[]
try:
    c.execute("SELECT T1.employee_id, T1.full_name , T1.position_title , T1.birth_date , T1.salary FROM employee T1 INNER JOIN employee T2 on T1.supervisor_id=T2.employee_id Where T2.full_name='Mona Jaramillo'")
    liste_tuples = c.fetchall()
    for t in liste_tuples:
        e = Emp(t[1], t[2], t[3], t[4])
        num_employe = t[0];
        print(t);
        Le.append(e)
except sqlite3.OperationalError as e:
    print("Erreur SQL :" + e.args[0])

mp=Le[0]
for emp in Le :
    #print(emp.mieux_paye_que(mp) , emp.salaire)
    if emp.mieux_paye_que(mp) :
        mp=emp

print(mp.nom_complet)
from employee import Departement as Dep
Ld=[]
db = connecte_base("foodmart.db")
c = db.cursor()
try:
    c.execute("SELECT department_id , department_description FROM department ")
    liste_tuples = c.fetchall()
    for t in liste_tuples:
        print(t);
        d= Dep(t[0],t[1])
        Ld.append(d)
except sqlite3.OperationalError as e:
    print("Erreur SQL :" + e.args[0])

#"""
#"""
mp=Ld[0]
for emp in Ld :
    #print(emp.mieux_paye_que(mp) , emp.salaire)
    if emp.plusCouteuxQue(mp) :
        mp=emp
print(mp.numDep)