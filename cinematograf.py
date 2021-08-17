#
#V-ați hotărât în ultimul moment să mergeți la cinematograf pentru a vedea un film cu prietenii, dar în 
#același timp vă grăbiți să vă întoarceți acasă cât mai repede. V-ați interesat de dinainte și ați văzut că 
#filmele care rulează acum la cinema durează aproximativ același timp. Deci, vă interesează în 
#principal ca filmul pe care o să îl vizionați să înceapă cât mai repede din momentul în care ajungeți 
#la casa de bilete, iar, în cazul în care sunt mai multe filme care încep la ora dorită, să îl alegeți pe cel 
#cu prețul biletului cel mai mic. 
#          Cerință
#Dându-se ora la care ajungeți la cinematograf, scrieți un program care să selecteze din lista de filme 
#pe cel care respectă cel mai bine dorințele voastre.
#        Date de intrare
#Se vor citi de la tastatură (fluxul stdin) de pe prima linie ora la care ajungeți la cinema, în format 
#hh:mm, iar de pe a doua linie un număr întreg n reprezentând numărul de oferte disponibile în 
#programul cinematografului. De pe următoarele n linii se vor citi datele despre fiecare film din ofertă 
#     în formatul:
#     <oră> <preț> <nume film>
#Datele din format vor fi separate prin câte un spațiu. Ora de începere a fiecărui film va fi tot în 
#formatul hh:mm, prețul va fi un număr întreg fără semn, iar numele filmului va fi un șir de caractere, 
#el putând fi format din mai multe cuvinte, dar pentru ușurință, ele vor fi separate prin caracterul 
#cratimă (‘-’). Fiecare linie se va termina cu un caracter newline (‘\n’).
#     Date de ieșire 
#Programul va afișa pe ecran (stream-ul standard de ieșire) un singur șir de caractere, reprezentând 
#numele filmului ales, în formatul dat în datele de intrare.
#
#           EXEMPLE:
# Intrare :                                        Iesire:
# 16:45                                             Mos-Craciun-in-misiune
# 4
# 18:00 15 Bohemian-Rhapsody
# 16:50 20 Mos-Craciun-in-misiune
# 12:00 13 Creed-II
# 16:55 20 Grinch

# 22:00                                            Covorul-zburator
# 4
# 17:00 15 Overlord
# 16:50 20 Morometii-2
# 23:05 13 Covorul-zburator
# 23:05 19 Bohemian-Rhapsody

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



#citirea orei de sosire la cinema
ora_sosire = input()
   #se transforma ora din sir intr-o lista prin split cu caracterul " : "
ora_sosire = ora_sosire.split(":")
   #se calculeaza ora in minute
ora_min = int(ora_sosire[0])*60 + int(ora_sosire[1])

diferenta = 100000
nume_film = ""

#se citest numarul de oferte disponibile
nr_oferte = int(input())
dic = {}

#se citesc ofertele disponibile
for i in range(nr_oferte):
    detalii_film = input()
    #detaliile despre film sut separate prin split
    detalii_film = detalii_film.split(" ")
    #ora filmului e separata prin split cu caracterul ":"
    ora_film = detalii_film[0].split(":")
    #ora e calculata in minute
    ora_film_min = int(ora_film[0])*60 + int(ora_film[1])
    detalii_film[0] = str(ora_film_min)
    #ora in minute si pretul fiecarui film sunt salvate intr-un dictionar 
    dic[detalii_film[2]] = detalii_film[0] + " " + detalii_film[1]


#ppentru fiecare element din dictionar 
for i in dic :
    #se calculeaza diferenta dintre ora de inceput a filmului si ora de sosire la cinema
    comparator = abs(int( int(dic[i].split(" ")[0]) - ora_min))
       #daca noua diferenta calculata este mai mica decat cea anterioaara 
    if comparator < diferenta :
          # si daca ora de inceput este mai mare decat cea de sosire la cinema 
        if int(dic[i].split(" ")[0]) > ora_min:
            # se salveaza diferenta convenabila
            diferenta = comparator
            # se salveaza numele filmului intr-o variabila
            nume_film = i
            # se salveaza pretul filmului intr-o variabila
            pret = int(dic[i].split(" ")[1])
       # daca diferenta calculata este egala cu cea anterioara 
    if comparator == diferenta :
          #daca ora de inceput este mai mare decat cea de sosire la cinema 
        if int(dic[i].split(" ")[0]) > ora_min:
            #se compara preturile filmelor cu aceeasi ora de inceput
            if int(dic[i].split(" ")[1]) < pret:
                #se salveaza pretul cel mai mic
                pret = int(dic[i].split(" ")[1])
                #se salveaza numele filmului
                nume_film = i

#se printeaza numele filmului care satisface cerintele impuse       
print(nume_film)
     


    
