
#Aţi fost angajaţi la o companie de telecomunicaţii deoarece ei recepţionează în fiecare zi mesaje 
#de la o sursă necunoscută. Mesajele sunt formate doar din cifre şi v-aţi dat seama că mesajele au 
#fost codate folosind un cifru simplu. Mesajul original era format din majusculele limbii engleze, 
#fiecare dintre acestea fiind convertite într-un număr, folosind următoarea corespondență:
#• A → 1
#• B → 2
#• ...
#• Z →26
#Din moment ce mesajul apare ca un șir de cifre neîntrerupte, există multe moduri în care ar putea 
#fi decodat, dar cei care le transmit s-au gândit la următorul scenariu:
#• Când următoarele două cifre din mesaj pot fi interpretate ca un număr de două cifre pe care 
#îl putem decoda, le vom interpreta astfel, ignorând posibilitatea interpretării unei singure 
#cifre.
#• Dacă pe poziţia curentă se află un 0, secvenţa 0x se va interpreta ca x, unde x este orice 
#cifră între 1 şi 9, iar cifra x se va decoda ca atare. (Exemplu: 01 → 1 → A).
#• Două cifre de 0 consecutive vor fi decodate ca un spațiu.
#         Cerinţă
#Să se decodeze mesajul, folosind scenariul de mai sus.
#      Date de intrare
#Pe o singură linie se va citi un şir de cifre neîntrerupte, reprezentând mesajul codat.
#      Date de ieşire
#Se va afişa, pe o singură linie, mesajul decodat. Linia se va termina obligatoriu cu un caracter 
#newline ("\n")
#
#  EXEMPLU
# IN: 195318520                    OUT: SECRET
# IN: 2671513152000011202          OUT: ZGOMOT ALB

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


#crearea dictionarului pentru decodare
dictionar={}
dictionar['1']= 'A'
dictionar['2']= 'B'
dictionar['3']= 'C'
dictionar['4']= 'D'
dictionar['5']= 'E'
dictionar['6']= 'F'
dictionar['7']= 'G'
dictionar['8']= 'H'
dictionar['9']= 'I'
dictionar['10']= 'J'
dictionar['11']= 'K'
dictionar['12']= 'L'
dictionar['13']= 'M'
dictionar['14']= 'N'
dictionar['15']= 'O'
dictionar['16']= 'P'
dictionar['17']= 'Q'
dictionar['18']= 'R'
dictionar['19']= 'S'
dictionar['20']= 'T'
dictionar['21']= 'U'
dictionar['22']= 'V'
dictionar['23']= 'W'
dictionar['24']= 'X'
dictionar['25']= 'Y'
dictionar['26']= 'Z'
dictionar['01']= 'A'
dictionar['02']= 'B'
dictionar['03']= 'C'
dictionar['04']= 'D'
dictionar['05']= 'E'
dictionar['06']= 'F'
dictionar['07']= 'G'
dictionar['08']= 'H'
dictionar['09']= 'I'




#citirea mesajului codat
mesaj = str(input())

#initializarea mesajului decodat
mesaj_decodat = ''

#crearea unui index util in parcurgerea mesajului codat
index = 0


while index < len(mesaj):
     #daca cele 2 cifere din mesaj sunt diferite de '00' 
    if mesaj[index:index+2] != '00':
         #daca numarul format cu cele 2 cifre e < 27
        if int(mesaj[index:index+2]) < 27:
            #se salveaza numarul in variabila key 
            key = mesaj[index:index+2]
            #daca numarul apartine dictionarului
            if key in dictionar:
                #cele 2 cifre se decodeaza conform dictionarului
                mesaj_decodat = mesaj_decodat + dictionar[key]
                #se incrementeaza indexul cu 2 pozitii
                index +=2
                
          #daca numarul format cu cele 2 cifre nu e < 27
        else:
            #cifrele se iau separat, ca numere independente
            key = mesaj[index]
            #se decodeaza cifra conform dictionarului
            mesaj_decodat = mesaj_decodat + dictionar[key]
            #indexul se incrementeaza cu o pozitie
            index +=1
            
     #daca cele 2 cifere din mesaj sunt egale cu '00'
    else:
        #cifrele sunt decodate ca spatiu
        mesaj_decodat = mesaj_decodat + ' '
        #se incrementeaza indexul cu 2 pozitii
        index +=2
    
#se afiseaza mesajul decodat
print(mesaj_decodat)
        

