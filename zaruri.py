#*******************************************************************************************************************
#                              Problema 2018.3.1 - Zaruri
#            
# Costică e în vacanță și l-au trimis părinții la țară. Acolo se plictisește groaznic și căutând prin dulapul 
# bunicului, a dat peste o pungă plină ochi cu zaruri. Neavând cu cine să joace zaruri, Costică s-a apucat 
# să le clădească, unul peste celălalt, cât de sus a putut. Uitându-se apoi la isprava făcută, i-a venit ideea 
# să afle care sunt numerele zarurilor de pe fețele acestora care nu se văd. Dându-și seama că deși e 
# posibil, e mai complicat, și că el e mai degrabă leneș decât curios, s-a hotărât să afle doar suma tuturor 
# numerelor de pe toate fețele zarurilor care nu se văd.
# Cerinţă
# Dându-se un număr N de zaruri și valorile de pe fețele vizibile ale zarurilor, calculați suma tuturor 
# fețelor care nu se văd. Se ignoră ordinea reală a numerelor pe fețele zarurilor, adică cele 6 numere 
# pot apărea pe zar în orice aranjament.

#
#*********************************************************************************************************************

# introducerea numarului de zaruri

n = int( input( "Introduceti N:" ) )
print( n )

# calculul sumei tuturor fetelor celor N zaruri
sum_total = ( 1+2+3+4+5+6 )*n
print("Suma toatla a fetelor de pe cele {} zaruri este: ".format(n),sum_total)
print('\n')

# initializarea listei
f = [0]

# initializarea variabilei suma cu 0
# variabila calculeaza suma fetelor care se vad, introduse de utilizator
suma = int(0)

while f[ len(f)-1 ] != '7':       # conditie de incheiere a introduceri , caracterul introdus =7                                     
    print("Pentru a marca sfarsitul introducerii adaugati 7")
    f = list(input("Introduceti valorile de pe fetele vizibile:"))
    print(f)
    for x in range(len(f)):
        if int(f[x])== 7:
            break
        suma += int(f[x])
       
    
    
print("S-a incheiat introducerea datelor")
print("Suma fetelor introduse pana acum este: ",suma)

# calculul sumei fetelor care nu se vad
rez = sum_total - suma
print("\nSuma fetelor care nu se vad este: ",rez)

        
   
    
           
            
