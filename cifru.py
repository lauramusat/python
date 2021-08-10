#
#
#Una din cele mai vechi metode de a cripta informaţia este printr-un cifru de substituţie. Acest cifru 
#se realizează prin înlocuirea fiecărui caracter din textul de intrare cu alt caracter.
#       Cerinţă
#Dându-se un text de intrare şi un tabel de substituţie, să se scrie un program care să cripteze textul 
#de intrare.
#       Date de intrare
#Pe prima linie citită de la tastatură (stream-ul stdin) se află textul de intrare. Pe următoarea linie se 
#află perechi de câte două caractere: caracterul din textul de intrare şi caracterul cu care acesta 
#trebuie înlocuit. Cele două caractere sunt separate prin virgulă şi perechile sunt separate prin spaţiu. 
#Doar literele mici (26), literele mari (26) şi cifrele (10) se vor înlocui în text, în total tabelul de 
#substituţie are deci 62 de elemente. Lungimea maximă a textului este de 1000 de caractere. Ambele 
#linii se termină cu apăsarea tastei Enter (caracterul newline, \n).
#       Date de ieşire
#Programul va afişa pe ecran (stream-ul standard de ieşire), pe o singură linie, textul criptat. Din 
#textul de intrare se vor înlocui doar literele mici şi mari şi cifrele, restul caracterelor rămânând 
#nemodificate. Linia se termină obligatoriu cu caracterul newline (\n)
#
#EXEMPLU
#            Intrare
# Ana are 37 de mere coapte (din care doar 35 coapte corespunzator)!
# a,H b,j c,6 d,I e,2 f,R g,5 h,t i,h j,k k,m l,f m,D n,F o,1 p,0 q,c r,G 
# s,n t,N u,e v,B w,r x,U y,p z,A A,8 B,X C,S D,P E,T F,a G,M H,d I,K J,L 
# K,3 L,C M,i N,9 O,E P,w Q,o R,z S,4 T,O U,q V,V W,J X,x Y,Z Z,u 0,l 1,y 
# 2,W 3,s 4,Q 5,g 6,v 7,7 8,b 9,Y
#                Ieşire
#       8FH HG2 s7 I2 D2G2 61H0N2 (IhF 6HG2 I1HG sg 61H0N2 61G2n0eFAHN1G)!

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



    #citirea textului de la tastatura
text = str( input() )
dic = {}
txt_criptat = ""
    #citirea tabelului de criptare de la tastatura
char = str( input() )
    #transforamrea elementelor din tabelul de criptare in elemente ale unei liste
lst = char.split(" ")

    # fiecare element din lista [de forma: (caracter,caract_criptat)] este separat in 2 si salvat intr o alta lista c
for x in range( len( lst ) ):
    c = lst[x].split(",")
           #elementele din lista c sunt introduse intr-un dictionar
    dic[c[0]] = c[1]
    
    # pentru fiecare caracter din text se face criptarea
for i in text:
    if i in dic:
        i = dic[i]
        txt_criptat += i
        # daca caracterul nu apare in tabelul de criptare, ramane la fel
    else:
        i = i
        txt_criptat += i
        

print( txt_criptat )
