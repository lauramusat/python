#
#George tocmai a învăţat despre sistemul de numeraţie cu bază 2 (sistemul de numeraţie binar).
#I se pare interesant şi a inventat jocul PC (permutări circulare), pe care vrea să îl joace cu prietenul său Armin.
#George îi spune lui Armin un număr natural nenul n, scris în baza 10 (sistemul zecimal),
#pe care acesta trebuie să-l transforme în baza 2. Se obţine astfel o secvenţă de cifre binare (biţi),
#care trebuie să înceapă cu 1 (primul bit din stânga în reprezentarea binară a numărului n să fie 1).
#
#Ideea jocului inventat de George a fost aplicarea uneia sau mai multor permutări circulare asupra scrierii în baza 2 a numărului n.
#Într-o permutare circulară, toate cifrele secvenţei date, exceptând-o pe ultima, sunt mutate cu o poziţie spre dreapta, ultima cifră devenind prima.
#
#De exemplu, dacă n=107, scrierea sa în baza 2 este 1101011. Prin permutări circulare succesive putem obţine, în ordine, secvenţele:
#
#              1110101
#              1111010
#              0111101
#              1011110
#              0101111
#              ...

#Fiecare astfel de secvenţă reprezintă transcrierea în bază 2 a unui număr natural m care are o anumită valoare în baza 10. Lui George jocul nu i s-ar mai părea așa
#interesant dacă n-ar reuși să scrie un program care să determine în locul lui numărul natural m. Ajutaţi-l!
#
#Cerinţă
#Să se afle cel mai mare număr natural m, scris în baza 10, a cărui scriere în baza 2 se poate obține prin una sau mai multe permutări circulare ale scrierii în baza 2 a numărului n.
#
#EXEMPLU
#   Scrierea în baza 2 a lui 13 este 1101. Rezultă că numărul de biți utilizați pentru procesarea de date este 4. Dintre cele 4 permutări circulare ale acestui șir:
#
#                  1101
#
#                  1110
#
#                  0111
#
#                  1011
#
#     Cea care generează numărul maxim în zecimal este 1110, adică 14.
#*********************************************************************************************************************************************************************************

n = int(input())
if n < 100000:                                      #conditie de executie a programului

    #scrierea numarului in baza 2
    b = bin( n ).replace( "0b", "" )     
   
    #i indica numarul de permutari 
    index = len( b )

    #m va salva valoarea celei mai mari permutari
    m = n
 
    while index > 0:
        c = b[ len( b )-1 ] + b[ :len( b )-1 ]      #permutarea sirului cu 1 pozitie si salvarea sirului permutat in c
        
        b = c                                       #sirul b e reactualizat
        d = "0b" + c                                # se adauga caracterele "0b" pt a se realiza conversia bin -> dec
        val_dec = int( d, 2 )                       # conversie bin -> dec
       
   
        if val_dec > m:                             #se compara valorile permutarilor 
            m = val_dec                             #se salveaza in m cea mai mare valoare
            
        
            
        index = index - 1                           #se decrementeaza indexul

    print( m )

else:
    print("Numarul nu apartine intervalului (0,100000)")
    

    

    

