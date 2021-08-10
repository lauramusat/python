#
#unteți șef de proiect la o companie și l-ați rugat pe Gigel să dea comandă de loturi de componente electronice
#pentru a realiza un set de plăci cu circuite electronice.
#Problema este că Gigel nu știe prea multă electronică așa că printre loturile pe care le-a comandat
#sunt și loturi cu tranzistoare condensatoare sau rezistoare insuficiente.
#Loturile care vă sunt utile sunt doar loturile care au un număr de condensatoare mai mare sau egal cu numărul de tranzistoare,
#numărul de rezistoare mai mare sau egal cu numărul de condensatoare,
#și au cel puțin un condensator, un tranzistor și un rezistor.
#În plus, vă interesează și lotul cu cele mai multe componente, pentru că din ele o să le mai completați pe cele lipsă.

#        Cerință

#Scrieți un program care primește la intrare loturile de componente și afișează câte dintre aceste loturi vă sunt utile
#și câte componente are lotul cel mai mare. Un lot se consideră util dacă respectă condițiile impuse mai sus. Aceste condiții trebuie îndeplinite simultan.

#       Date de intrare

#Se va citi de la tastatură (fluxul stdin) pe o singură linie un număr întreg n reprezentând numărul de loturi.
#Apoi, se vor citi cele n loturi după cum urmează: se citește pe o linie numărul de componente din lotul respectiv, k,
#iar pe următoarea linie k litere reprezentând tipurile de componente ale lotului, separate prin spatii
#(R reprezentând un rezistor, C reprezentând un condensator și T reprezentând un tranzistor).

#       Date de ieșire

#Programul va afișa pe ecran (stream-ul standard de iesire) două numere întregi,
#reprezentând numărul de loturi utile dintre cele citite cât și numărul de componente ale lotului cel mai mare, valori separate printr-un spațiu.
#             EXEMPLU
#
#               3                           Iesire: 1 6 
#
#               5
#
#               R C R T C
#
#               5
#
#               C R T R T
#
#               6
#
#               C C T C C T
#
#***********************************************************************************************************************************************************



     #citirea numarului de loturi
n = int(input())
k = 0
list1 = []

while n > 0:
    
     #citirea nr de componente din loturi
    nr_comp = int(input())

     #adaugarea nr de componente a loturilor intr-o lista
    list1.append(nr_comp)
    
     #daca nr de componente e diferit de 0 se introduc componentele 
    if nr_comp != 0:
        comp = str(input())
          #se determina nr de aparitii al fiecarui component in lotul din care face parte
        for x in comp:
            r = comp.count("R")
            t = comp.count("T")
            c = comp.count("C")
          #se verifica conditiile pentru un lot util
        if (c >= t) and  (r >= c):
            if ("C" in comp) and ("T" in comp) and ("R" in comp ):
                k += 1
    
   

    n = n -1

    
    #se sorteaza lista pentru a determina nr maxim de componente
list1.sort()
    #se afiseaza nr de loturi utile si  nr maxim de componente 
print(k,list1[len(list1)-1])


        
