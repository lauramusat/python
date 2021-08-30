#
#Problema 2018.1.1 – Blockchain hash (PDF / PDF(EN))
#Pentru a deveni competitivă în domeniul Blockchain și a monedelor virtuale,
#firma la care lucrați a dezvoltat un algoritm de hashing inovativ pentru valori numerice.
#Algoritmul funcționează în modul următor: asupra unui număr natural se face
#următoarea transformare: dacă numărul are cel puțin două cifre, se iau pe rând
#din număr câte două cifre vecine și se scade cea mai mică din cea mai mare.
#Cu cifrele astfel obținute se formează un nou număr. De exemplu, pentru numărul 5734,
#din cifrele 5 și 7 se obține 2, din 7 și 3 se obține 4 iar din 3 și 4 se obține 1.
#Formăm deci un nou număr 241, căruia i se poate aplica aceeași transformare,
#obținându-se 23. Din 23, prin același procedeu, obținem 1.
#Dacă numărul este format dintr-o singură cifră, transformarea îl lasă nemodificat.
#Hash-ul se calculează realizând succesiv transformarea asupra numărului original și apoi
#asupra rezultatului obținut, de k ori, și sumând toate rezultatele parțiale și rezultatul
#final (excluzând valoarea de start).

#Cerință

#Se dau două numere naturale N şi k și apoi încă N numere naturale.
#Se cere să se determine valoarea maximă a hash-ului care se va obține aplicând algoritmul
#de hash celor N numere folosind k pentru numărul de iterații de transformare, conform descrierii de mai sus.

#Date de intrare

#La intrarea programului se prezintă pe prima linie două numere naturale N și k,
#separate prin spațiu. Pe a doua linie se află cele N numere, separate tot prin spații.
#Liniile de intrare se încheie cu caracterul newline (\n), obținut prin apăsarea tastei Enter.

#Date de ieșire

#Programul va afișa la consolă (pe stream-ul stdout) un singur număr, reprezentând
#valoarea maximă dintre toate hash-urile obținute conform procedeului descris anterior.
#
#EXEMPLU
#
#intrare:                      iesire:
# 2 2                           264
# 5734 1234


#se citeste N si k
Nk=input()
N=int(Nk.split(" ")[0])
k=int(Nk.split(" ")[1])

lista_nr = []
sir =""
lista_transformari = []
suma = 0
lista_sume =[]

#se citesc cele N numere
numere = input()

#se salveaza numerele intr-o lista
lista_nr = numere.split(" ")

#se prelucreaza fiecare numar din lista
for i in range(len(lista_nr)):
     nr_curent = int(lista_nr[i])
     index = k
     #cat timp nr de succesiuni este nenul
     while( index > 0 ):
         #daca numarul e format din mai mult de o cifra
        if nr_curent > 9 :
            nr_curent = str(nr_curent)
            #se efectueaza diferentele dintre cifrele sucesive din numar
            for y in range(len(nr_curent)-1):
                if nr_curent[y] >= nr_curent[y+1]:
                    dif =  int(nr_curent[y]) - int(nr_curent[y+1])
                    #diferenttele se alatureaza intr-un sir formand un nou numar
                    sir = sir + str(dif)
                else:
                    dif = int(nr_curent[y+1]) - int(nr_curent[y])
                    sir = sir + str(dif)

            #transformarea se salveaza intr-o lista        
            lista_transformari.append(sir)
            #nr_curent devine nr creat din diferentele nr anterior
            nr_curent = int(sir)
            #se decrementeaza indexul de succesiuni
            index = index - 1
            #se reinitializeaza sirul
            sir =""

         #daca numarul e format dintr-o cifra
        else:
            #transformarile asupra lui nu-l modifica
            sir = sir + str(nr_curent)
            lista_transformari.append(sir)
            #urmatorul nr_curent va avea aceeasi valoare
            nr_curent = nr_curent
            #se decrementeaza indexul de succesiuni
            index = index -1
            #se reinitializeaza sirul
            sir=""
        
     #dupa ce s-au terminat transformarile asupra unui nr 
     for z in range( len( lista_transformari ) ):
         #se calculeaza suma valorilor transformarilor
        suma = suma + int(lista_transformari[z])
        
     #suma este salvata intr-o lista
     lista_sume.append(suma)
     #se reinitializaeaza variabila suma
     suma = 0
     #se goleste lista de transformari
     lista_transformari.clear()
     

#dupa ce s-au efesctuat transformari asupra tuturor numerelor
#se printeaza suma maxima 
print(max(lista_sume))
    
        



    
            
            
        
                
            
    
