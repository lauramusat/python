#
#Cărţile din biblioteca UPB trebuie mutate într-o nouă locaţie, iar aranjarea lor pe rafturi
#se va face într-o manieră inovativă, urmărindu-se minimizarea numărului de rafturi necesare.
#Bibliotecara știe că are un număr suficient de rafturi încât să pună toate cărțile. Pe fiecare raft
#încap cărți însumând în total D pagini. De asemenea, ştie câte cărţi cu un anumit număr
#de pagini există în bibliotecă.Dat fiind acestea şi urmărind să ocupe cât mai puţine rafturi,
#bibliotecara şi-a propus să aranjeze cărţile pe rafturi:

#raft după raft,
#alegând întotdeauna să completeze raftul curent cu cea mai groasă carte disponibilă,
#trecând la următorul raft numai în condiţiile în care pe raftul curent nu mai poate fi plasată nicio carte dintre cele rămase şi
#asigurându-se că a plasat pe rafturi toate cărţile.

#Cerinţă

#Scrieţi un program care o poate ajuta pe bibliotecară să aranjeze cărţile pe rafturi în mod eficient,
#conform regulilor enunţate mai sus.

#Date de intrare

#Se vor citi de la tastatură (fluxul stdin) următoarele date:

#·        de pe prima linie: două numere întregi D şi k, separate prin spaţiu, reprezentând D – dimensiunea rafturilor
#         exprimată în număr de pagini, k – numărul de dimensiuni diferite pentru cărţile ce trebuie aranjate în bibliotecă;

#·        de pe următoarele k linii: câte două numere întregi n şi p, reprezentând numărul de cărţi n de grosime
#         p pagini ce trebuie aranjate în bibliotecă.

#Cele k linii ce conțin informații despre cărți sunt date în ordinea inversă a grosimii p.

#Toate liniile conţinând date de intrare sunt finalizate cu caracterul newline (tasta Enter).

#Date de ieşire

#Programul va afişa pe ecran (stream-ul standard de ieşire) m linii, corespunzătoare celor m rafturi
#pe care a fost plasată cel puţin o carte, în ordinea completării lor (conform regulilor).
#Fiecare dintre cele m linii va conţine o serie de numere întregi, separate prin spaţiu,
#reprezentând dimensiunile cărţilor ce au fost plasate pe acel raft, în ordinea plasării lor pe raft (conform regulilor).
#
#  EXEMPLU
#IN:                        OUT:
# 200 5                   130 60
# 2 130                   130 60
# 4 120                   120 80
# 2 80                    120 80
# 3 60                    120 60   
# 7 50                    120 50
#                         50 50 50 50
#                         50 50 
#
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






dk = input()
dk = dk.split(" ")
d = int(dk[0])  #dimensiunea rafturilor
k = int(dk[1])  # nr de dimensiuni diferite

carti = {}

for x in range(k):
    np = input()   
    np= np.split(" ")
    n = int(np[0])    #nr de carti
    p = int(np[1])    #nr de pagini
    carti[p] = n
    



pg_pe_raft = 0
raft = []
z = 0




for i in carti:
    while carti[i] != 0:                #cat timp sunt carti disponibile
        if i <= d - pg_pe_raft:                    #daca  cartea incape pe raft
            raft.append(i)                     #se adauga cartea pe raft
            carti[i] -=1                       #se scade nr de carti neasezate 
            pg_pe_raft = pg_pe_raft + i       #se incrementeaza nr de pagini de pe raft
                                  
            for y in carti:             #se parcurge dictionarul din nou
                if carti[y] != 0:
                    if y <= d - pg_pe_raft:
                        raft.append(y)
                        carti[y] -=1
                        pg_pe_raft = pg_pe_raft + y
                        if min(carti) > d - pg_pe_raft :    #daca nu mai incap pagini pe raft
                            z = 1
                            break
        else:
             z = 1
        if z == 1 or carti[i] == 0:    #raftul e plin sau nu mai sunt carti
             print(raft)
             raft.clear()
             z = 0
             pg_pe_raft = 0
                            
                



        
        
            
