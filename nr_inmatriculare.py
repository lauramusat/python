#
#Se va dezvolta un program care interpretează o secvenţă de date de intrare, formată din una sau mai 
#multe linii. Programul parcurge secvenţa de intrare şi determină dacă fiecare din linii reprezintă un 
#număr de înmatriculare românesc valid, caz în care afişează linia respectivă în consolă. 
#        Date de intrare
#Secvenţa de intrare este formată din linii terminate de caracterul newline (\n), generat prin apăsarea 
#tastei Enter. Fiecare linie este formată din 3 şiruri de caractere separate de spaţiu. Structura fiecărei 
#linii este ilustrată generic în cele ce urmează:
#String1 String2 String3
#unde String1, String2 şi String3 sunt şiruri de caractere a căror structură va fi descrisă în continuare.
#        Logica internă
#Programul va verifica dacă, luate împreună, cele 3 şiruri de caractere din fiecare linie reprezintă un 
#număr de înmatriculare valid, folosind următoarele reguli:
# Valorile valide pentru String1 sunt: AB, AR, AG, B, BC, BH, BN, BT, BV, BR, BZ, CS, 
#CL, CJ, CT, CV, DB, DJ, GL, GR, GJ, HR, HD, IL, IS, IF, MM, MH, MS, NT, OT, PH, 
#SM, SJ, SB, SV, TR, TM, TL, VS, VL, VN (atenţie: doar litere mari!)
# String2 e format din 2 sau 3 caractere numerice (numărul de caractere numerice nu este 
#condiţionat de valoarea String1)
# String3 e format din exact 3 caractere litere mari
#        Date de ieşire
#Programul trebuie să afişeze la ieşire, în consolă (pe stream-ul stdout), exclusiv liniile de intrare 
#care reprezintă un număr de înmatriculare valid conform regulilor de mai sus. Liniile ce conţin 
#numere valide nu vor fi modificate în niciun fel, iar ordinea lor va fi păstrată. Fiecare dintre liniile 
#afişate va fi terminată de caracterul newline (\n).
#
#  EXEMPLU:
#   IN:                      OUT:
#  AB 123 ABC               AB 123 ABC
#  B 23 DEF                 B 23 DEF
#

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


String1 = [ "AB", "AR", "AG", "B", "BC", "BH", "BN", "BT", "BV", "BR", "BZ", "CS", 
"CL", "CJ", "CT", "CV", "DB", "DJ", "GL", "GR", "GJ", "HR", "HD", "IL", "IS", "IF",
"MM", "MH", "MS", "NT", "OT", "PH", "SM", "SJ", "SB", "SV", "TR", "TM", "TL", "VS",
"VL", "VN" ]

numere= ""

#se introduc date cat timp nu se apasa enter la o intrare  
while True:
    nr_introdus = input()
    if nr_introdus:
        #la numarul introdus se adauga caracterul "\n" la final
        numere = numere + nr_introdus + "\n"
    else:
        break
    
#numerele introduse sunt separate cu ajutorul lui strip() pe linii diferite
nr_introdus = numere.strip()
#dupa separare numerele sunt salvate intr-o lista
nr_introdus = nr_introdus.split("\n")

#pentru ficare numar din lista se verifica conditiile impuse pentru un numar valid
for i in nr_introdus:
    if i.split()[0] in String1:
        if i.split()[1].isdigit()==True  and len(i.split()[1])>=2 and len(i.split()[1])<4:
            if len(i.split()[2])==3:
                if i.split()[2].isupper() == True:
                    print(i)
                    



    
                
