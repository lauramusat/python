#
# Un faimos cazino din București dorește să detecteze mai rapid trișorii de la mesele lor de cărți.
# Folosind un program de recunoaștere a imaginilor se pot detecta ce cărți sunt jucate
# de fiecare jucător de la masă și se dorește să se descopere dacă vreunul din ei a scos cărți din buzunar.
# Jocul monitorizat se joacă cu două pachete clasice (52 de cărți fiecare, fără Joker).
#
#      Cerință
# Scrieți un program care să ajute la detectarea trișorilor. În cazul în care se detectează că o carte apare de prea multe ori,
# programul va afișa cartea și va opri jocul.
#
#     Date de intrare
# Se vor citi de la tastatură (fluxul stdin) următoarele date:
#
# Pe prima linie se află numărul n, reprezentând numărul maxim de mâini ce vor fi jucate;
# Pe următoarele n linii se află cartea jucată, în formatul:
#              <număr_carte> <semn_carte>
#    Date de ieşire
# În cazul în care nimeni nu încearcă să trișeze se va afișa textul JOC OK. În cazul în care cineva a încercat sa trișeze,
# se va afișa cartea problemă în același formatca la intrare: numărul cărții urmat de semn, separate prin spațiu.
#            EXEMPLU
#     8                         IESIRE
#  11 caro                     11 pica        Asul de pică este prima carte jucată de trei ori.
#  11 pica                    
#  11 caro
#  11 pica
#  11 pica
#  11 caro
#  14 pica
#  6 caro
#*********************************************************************************************************************************************



# citire nr de maini ce vor fi jucate
n = int(input())

dictionar = {}
i = 0
mesaj = "JOC OK"

while n > 0:
    nr_semn = input()  # citirea nr carte si semn carte
    
    if nr_semn in dictionar:                          #daca cartea a mai fost jucata
        dictionar[nr_semn] += 1                       #valoarea din dictionar se incrementeaza

    else:
        dictionar[nr_semn] = 1                        #daca nu a mai fost jucata,valoarea ramane 1
   
    if dictionar[nr_semn] >= 3 and i == 0:            #cand o carte e jucata de cel putin 3 ori
        mesaj = nr_semn                               # se afiseaza cartea
        i = 1
    n = n-1
    

print(mesaj)            #daca nu au fost incercari de frauda se afiseaza mesajul standard
