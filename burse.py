<<<<<<< HEAD
#
#Doamna secretară trebuie să stabilească numărul de studenți ce vor lua bursă de merit în anul 
#universitar următor și să identifice studentul care va lua bursa de performanță (există o singură bursă 
#de performanță). Are la dispoziție lista tuturor studenților și notele obținute de aceștia la diversele 
#discipline. Bursa de performanță se acordă studentului integralist cu media cea mai mare. Bursele de 
#merit se acordă în ordinea descrescătoare a mediilor, în limita numărului maxim de burse, tuturor 
#studenților integraliști care au media generală peste 8.00.

#         Cerinţă
#Stabiliți ce student va lua bursă de performanță și câți studenți vor lua bursă de merit în anul 
#universitar următor.

#       Date de intrare
#Se vor citi de la tastatură (fluxul stdin) următoarele date:
#• Trei numere întregi pozitive m, n, p separate prin spaţiu, reprezentând
#o m – numărul de studenţi,
#o n – numărul de discipline,
#o p – numărul de burse de merit disponibile;
#• 2*m linii de pe care se citesc, în ordine, în formatul:
#o <NS>, un şir de caractere reprezentând numele studentului;
#o <N1> <N2> ... <Nn>, n numere întregi din intervalul 1 – 10 separate prin spaţiu 
#reprezentând notele obţinute de respectivul student la cele m discipline;
#Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline (tasta Enter).

#        Date de ieşire
#Programul va afișa pe ecran (stream-ul standard de ieșire):
#• Pe prima linie: numărul de studenți ce vor lua bursă de merit
#• Pe a doua linie: numele studentului care va lua bursă de performanță și media media lui (număr 
#fracționar cu 2 zecimale) separate prin spațiu.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


mnp = input()
mnp = mnp.split(" ")

m = int(mnp[0])     #nr studenti
n = int(mnp[1])     #nr discipline
p = int(mnp[2])     #nr burse de  merit disponibile

studenti = {}
contor_medii = 0
medie_max = 0


for i in  range(m):
       #se introduce numele studentului
    nume = input()
       #se introduc notele studentului care sunt salvate intr-o lista sub forma de nr. intregi
    note_student = [ int(x) for x in input().split(" ") ]
       #se calculeaza media
    medie = sum(note_student)/n
    k = 0
       #daca notele studentului nu sunt > 5 k devine 1 -> stud nu e integralist
    for j in range(n):
        if note_student[j] < 5:
            k = 1
       #daca k e 0 (student integralist) 
    if k == 0:
            #numele si media lui generala sunt inroduse intr-un dictionar
        studenti[nume] = medie
            #daca media > 8 studentul are sanse sa ia bursa 
        if medie >=8:
            #contorul de medii se incrementeaza
            contor_medii += 1

        #se cauta in dictionar studentul cu media maxima care va lua bursa de performanta    
for i in studenti:
    if studenti[i] > medie_max:
        medie_max = studenti[i]
        stud_max = i

        #se afiseaza nr de burse de merit care se acorda
            #daca sunt prea multi elevi cu medie > 8 nr de burse de merit = p
if contor_medii > p:
    print(p)
else:
            #altfel se afiseaza nr de burse > 8 gasite, din care se elimina cea de performanta
    print(contor_medii-1)

        #se afiseaza numele si media studetului cu bursa de performanta
print(stud_max, "%.2f" %medie_max)
=======
#
#Doamna secretară trebuie să stabilească numărul de studenți ce vor lua bursă de merit în anul 
#universitar următor și să identifice studentul care va lua bursa de performanță (există o singură bursă 
#de performanță). Are la dispoziție lista tuturor studenților și notele obținute de aceștia la diversele 
#discipline. Bursa de performanță se acordă studentului integralist cu media cea mai mare. Bursele de 
#merit se acordă în ordinea descrescătoare a mediilor, în limita numărului maxim de burse, tuturor 
#studenților integraliști care au media generală peste 8.00.

#         Cerinţă
#Stabiliți ce student va lua bursă de performanță și câți studenți vor lua bursă de merit în anul 
#universitar următor.

#       Date de intrare
#Se vor citi de la tastatură (fluxul stdin) următoarele date:
#• Trei numere întregi pozitive m, n, p separate prin spaţiu, reprezentând
#o m – numărul de studenţi,
#o n – numărul de discipline,
#o p – numărul de burse de merit disponibile;
#• 2*m linii de pe care se citesc, în ordine, în formatul:
#o <NS>, un şir de caractere reprezentând numele studentului;
#o <N1> <N2> ... <Nn>, n numere întregi din intervalul 1 – 10 separate prin spaţiu 
#reprezentând notele obţinute de respectivul student la cele m discipline;
#Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline (tasta Enter).

#        Date de ieşire
#Programul va afișa pe ecran (stream-ul standard de ieșire):
#• Pe prima linie: numărul de studenți ce vor lua bursă de merit
#• Pe a doua linie: numele studentului care va lua bursă de performanță și media media lui (număr 
#fracționar cu 2 zecimale) separate prin spațiu.
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


mnp = input()
mnp = mnp.split(" ")

m = int(mnp[0])     #nr studenti
n = int(mnp[1])     #nr discipline
p = int(mnp[2])     #nr burse de  merit disponibile

studenti = {}
contor_medii = 0
medie_max = 0


for i in  range(m):
       #se introduce numele studentului
    nume = input()
       #se introduc notele studentului care sunt salvate intr-o lista sub forma de nr. intregi
    note_student = [ int(x) for x in input().split(" ") ]
       #se calculeaza media
    medie = sum(note_student)/n
    k = 0
       #daca notele studentului nu sunt > 5 k devine 1 -> stud nu e integralist
    for j in range(n):
        if note_student[j] < 5:
            k = 1
       #daca k e 0 (student integralist) 
    if k == 0:
            #numele si media lui generala sunt inroduse intr-un dictionar
        studenti[nume] = medie
            #daca media > 8 studentul are sanse sa ia bursa 
        if medie >=8:
            #contorul de medii se incrementeaza
            contor_medii += 1

        #se cauta in dictionar studentul cu media maxima care va lua bursa de performanta    
for i in studenti:
    if studenti[i] > medie_max:
        medie_max = studenti[i]
        stud_max = i

        #se afiseaza nr de burse de merit care se acorda
            #daca sunt prea multi elevi cu medie > 8 nr de burse de merit = p
if contor_medii > p:
    print(p)
else:
            #altfel se afiseaza nr de burse > 8 gasite, din care se elimina cea de performanta
    print(contor_medii-1)

        #se afiseaza numele si media studetului cu bursa de performanta
print(stud_max, "%.2f" %medie_max)
>>>>>>> 67e79533874dd59f1adf55288ac0ed2efa5cb042
