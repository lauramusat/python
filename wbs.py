#Pentru compresia unui şir binar se foloseşte tehnica White Block Skipping adaptat - ignorarea blocurilor (grupelor)
#uniforme (compuse numai din biţi de 0 sau numai din biţi de 1). Şirul este împărţit în blocuri (grupe) de câte n biţi,
#codate independent. Există două codări posibile: codarea în care se ignoră blocurile compuse numai din biţi 0, şi codarea
#în care se ignoră blocurile compuse numai din biţi 1. In final, se alege codarea care asigură raportul maxim de compresie.
#In cazul în care cele două variante de compresie ajung la acelaşi raport de compresie, se utilizează varianta în care se
#ignoră blocurile compuse numai din biţi 0.
#Pentru codarea în care se ignoră blocurile compuse numai din biţi 0, şirul comprimat începe cu un bit 0, la care se adaugă
#codurile corespunzătoare blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă toţi biţii blocului sunt
#nuli, blocul este înlocuit de un bit unic de zero; dacă cel puţin un bit din bloc este nenul, atunci biţii blocului se copiază
#şi în faţa lor este adăugat un bit de 1 (ca prefix).
#Pentru codarea în care se ignoră blocurile compuse numai din biţi 1, şirul comprimat începe cu un bit 1, la care se adaugă
#codurile corespunzătoare blocurilor de biţi din şirul iniţial, codate după regula următoare: dacă toţi biţii sunt 1, blocul
#este înlocuit de un bit unic de 1; dacă cel puţin un bit din bloc este nul, atunci biţii blocului se copiazăşi în faţa lor este
#adăugat un bit de 0 (ca prefix).
#            Cerință
#Dându-se un număr N pozitiv reprezentand numărul de elemente din şir, apoi numărul n pozitiv reprezentând numărul
#de elemente din fiecare bloc ce va fi codat, apoi cele N elemente ale şirului, să se genereze şirul comprimat (codat) şi să
#se calculeze raportul de compresie (raportul dintre numărul de biţi din şirul iniţial - N - şi numărul de biţi din şirul
#comprimat). Dacă şirul de intrare nu poate fi împărţit exact în grupe de n biţi, ultimii biţi rămaşi se codează ca şi când
#ar face parte dintr-un grup neuniform (dar fără a adăuga biţi de completare).
#        Date de intrare
#Pe prima linie se află numărul întreg pozitiv N, reprezentând numărul de elemente din şir, urmat de caracterul newline,
#apoi numărul întreg pozitiv n, reprezentând numărul de elemente din fiecare grupă, urmat de caracterul newline. Pe
#următoarele N linii se află elementele şirului (numere de 0 sau 1), câte unul pe linie, urmat de caracterul newline.
#       Date de ieșire
#Se va afișa pe prima linia valoarea raportului de compresie, cu două zecimale, cu rotunjire, apoi şirul comprimat, câte
#un număr (0 sau 1) pe fiecare linie. 
#
#    EXEMPLU
# IN:                       
#   10
#   5
#   0
#   0
#   0
#   0
#   0
#   0
#   0
#   0
#   1
#   1
#OUT:
#   1.25
#   0
#   0
#   1
#   0
#   0
#   0
#   1
#   1

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~





nr_biti = int(input())         #nr biti ce vor fi introdusi pentru codare
bloc_biti = int(input())       #dimensiunea blocurilor in care vor fi impartiti bitii introdusi


bloc = []
sir_biti = ""



for i in range(nr_biti):        #se introduc bitii pe rand
    bit = input()
    sir_biti = sir_biti + bit   #bitii sunt salvati intr-un sir
    


#print(sir_biti)

n = int(len(sir_biti)) 
x=0
while x < n:                   #se imparte sirul de biti in blocuri 
                               #blocurile sunt salvate intr-o lista
    bloc.append(sir_biti[x:x+bloc_biti])
    x = x + bloc_biti

#print(bloc)

       #pentru codarea in care se ignora blocurile de "0"

sir_0 = ""
for i in range(bloc_biti):     #se construieste sirul ce contine numai "0" de dimensiunea unui bloc  
    sir_0 = sir_0 + "0"

bloc_codat_0 = "0"             #se initializeaza sirul codat cu "0"

for i in range(len(bloc)):     #se parcurge lista cu blocuri 
                               #se construieste sirul codat urmand regulile de codare
    if bloc[i] == sir_0:
        bloc_codat_0 = bloc_codat_0 + "0"
    else:
        bloc_codat_0 = bloc_codat_0 + "1" + bloc[i]

        
                               #se calculeaza raportul de compresie pentru acest tip de codare
raport_0 = float(nr_biti/len(bloc_codat_0)) 

#print(bloc_codat_0)
#print(raport_0)

      #pentru codarea in care se ignora blocurile de "1"

sir_1 = ""
for i in range(bloc_biti):     #se construieste sirul ce contine numai "1" de dimensiunea unui bloc  
    sir_1 = sir_1 + "1"

bloc_codat_1 = "1"             #se initializeaza sirul codat cu "1"

for i in range(len(bloc)):     #se parcurge lista cu blocuri
                               #se construieste sirul codat urmand regulile de codare
    if bloc[i] == sir_1:
        bloc_codat_1 = bloc_codat_1 + "1"
    else:
        bloc_codat_1 = bloc_codat_1 + "0" + bloc[i]

        
                                #se calculeaza raportul de compresie pentru acest tip de codare
raport_1 = float(nr_biti/len(bloc_codat_1))

#print(bloc_codat_1)
#print(raport_1)


      #se compara cele 2 rapoarte de compresie si se afiseaza raportul cel mai mare si codarea corespunzatoare
if raport_0 >= raport_1:
    print("%.2f" %raport_0)
    for x in bloc_codat_0:
        print(x)
else:
    print("%.2f" %raport_1)
    for x in bloc_codat_1:
        print(x)
    
    
        


        

