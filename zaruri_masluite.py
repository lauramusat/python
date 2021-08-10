#
#Costică e în vacanță și l-au trimis părinții la țară.
#Acolo se plictisește groaznic și căutând prin dulapul bunicului, a dat peste o pungă plină ochi cu zaruri.
#Neavând cu cine să joace zaruri dar părându-i-se că unele din zaruri sunt mai grele decât celelalte,
#Costică a ales un zar și s-a apucat să îl testeze aruncând cu el și notând de câte ori a picat fiecare față.
#Încearcă apoi să-și dea seama dacă zarul e măsluit sau nu, considerând că diferența dintre
#numărul maxim de apariții a unei fețe și numărul minim de apariții (a oricăror altor fețe)
#nu trebuie să depășească 10% din numărul total de aruncări.
#
#      Cerinţă
#Dându-se un număr N de aruncări cu zarul și apoi N numere naturale în intervalul [1:6] reprezentând numerele
#obținute la aruncări, să se determine dacă zarul e măsluit conform condiției de mai sus.
#
#      Date de intrare
#De la intrare (fluxul stdin) de pe prima linie se citește numărul natural N, reprezentând numărul de aruncări cu zarul.
#Pe următoarele N linii se află câte un număr natural în intervalul [1:6] reprezentând numerele obținute la aruncări.
#
#      Date de ieşire
#La ieşire (fluxul stdout) se va afișa un singur număr, 0 sau 1, 0 dacă zarul e normal, și 1 dacă este măsluit.
#
# EXEMPLU:                   Iesire:
#       10                      0
#       1
#       4
#       2
#       5
#       4
#       6
#       2
#       1
#       3
#       3
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   #citirea numarului de aruncari
n = int(input() )
lista = []
lista1 = []
x = n
    #citirea fiecarui zar aruncat
while x > 0:
    nr = int( input() )
    #adaugarea zarurilor aruncate intr-o lista
    lista.append(nr)
    x = x - 1


    #determinarea nr de aparitii al fiecarei fete si salvarea lor intr-o lista
for i in lista:
    c = lista.count(i)
    lista1.append(c)

    #sortarea listei ce contine nr de aparitii al fetelor
lista1.sort()

    #determinarea nr maxim si minim de aparitie al unei fete
maxim = lista1[ len( lista1 ) - 1 ]
minim = lista1[0]

if(maxim == minim):
    minim = 0

dif = maxim - minim

    #conditia pentru ca zarurile sa fie normale
if (dif <= 0.1*n):
    print(0)
else:
    print(1)
