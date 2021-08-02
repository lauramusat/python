# 
# Împreună cu echipa de la firmă ați inventat un nou algoritm de generare de numere pseudo-aleatoare.
# Pentru a valida că generatorul poate fi folosit în algoritmi criptografici (cryptographically secure)
# trebuie să implementați și să rulați o baterie de teste.
# Unul din aceste teste verifică numărul de apariții pentru fiecare secvență posibilă de doi biți: 00, 01, 10 și 11
# cât și raportul între numărul de biți de 0 și de 1. Pentru ca secvența de biți să fie aleatoare,
# trebuie ca numărul de apariții pentru fiecare din cele patru perechi să fie aproximativ egale
# și în același timp numărul de biți de 0 să fie aproximativ egal cu cei de 1. Mai precis,
# trebuie ca raporturile R1 dintre numărul de apariții a perechii care apare de cele mai multe ori
# și numărul de apariții a perechii care apare de cele mai puține ori,cât și raportul R2
# între numărul de apariții ale celui mai frecvent bit și numărul de apariții ale celui mai puțin frecvent bit
# să fie mai mici sau egale cu 110%.
#
#            Cerință

# Dându-se un număr n reprezentând numărul de biți generat de RNG și secvența de n biți,
# să se calculeze raporturile R1 și R2 și să se decidă dacă generatorul este valid sau nu.

#          Date de intrare

# Pe prima linie se află n, numărul de biți generați. Pe a doua linie se află o secvență continuă de n biți
# (valori de 0 sau 1), ne-separați prin spații.

#          Date de ieșire

# Programul va afișa în consolă (pe stream-ul stdout) pe prima linie raporturile R1 și R2 calculate conform descrierii,
# valori fracționare cu două zecimale,separate prin spațiu,
# iar pe a doua linie valoarea 1 dacă generatorul este valid sau 0 dacă nu este.
#
#*************************************************************************************************************************************


            #citirea numarului de biti
n = int(input())
            #citirea secventei de biti sub forma de sir
sir =str(input())

lista = []
lista1 = []
            #introducerea elementelor din sir doua cate doua intr-o lista
for i in range(0,n,2):
    lista.append(sir[i:i+2])

            #numarearea secventelor de biti 
for x in lista:
    nr_00 = lista.count("00")
    nr_01 = lista.count("01")
    nr_10 = lista.count("10")
    nr_11 = lista.count("11")

 
            #crearea unei liste ce contine nr. de aparitii ale secventelor de biti
nr_perechi = [ nr_00, nr_01, nr_10, nr_11 ]

            #eliminarea din lista a elementelor cu valoare 0
for x in nr_perechi:
    if x != 0:
        lista1.append(x)
    
            #sortarea crescatoare a listei
lista1.sort()

            #primul element din lista are valoarea cea mai mica
minim = lista1[0]
            #ultimul element din lista are valoarea cea mai mare
maxim = lista1[len(lista1)-1]
            #calculul raportului R1
r1 = maxim / minim

            #determinarea nr de apariti in sir ale bitilor "0" si "1"
for x in sir:
    nr_0 = sir.count("0")
    nr_1 = sir.count("1")

            #nr de aparitii ale bitilor sunt introduse intr-o lista 
nr_biti = [ nr_0, nr_1 ]
            #sortatrea crescatoare a listei
nr_biti.sort()
            #calculul raportului R2
r2= nr_biti[1] / nr_biti[0]


            #afisarea celor 2 rapoarte cu 2 zecimale dupa virgula
txt = "{:.2f} {:.2f}"
print(txt.format(r1, r2))

            #se verifica daca secventa este aleatoare
if r1*100 <=110 and r2*100 <=110:
    print("1")
else:
    print("0")

