import time
import random
from ngram import Ngram_score

table = [["8", "3", "1", "4", "0", "5", "7", "2", "6", "9"],
         ["" ,""  ,""  ,"n" ,"e" ,"z" ,"a" , "i", "o", " "],
         ["ć", "u", "w", "t", "g", "r", "f", "p", "ń", "ó"],
         ["ś", "c", "b", "k", "s", "ę", "d", "m", "ł", "ź"],
         ["ż", "!", "ą", "?", "l", "j", ".", ",", "y", "h"]]

'''
1. Trzeba stworzyć tablicę częstotliwości dla używanego alfabetu (bigram.txt, trigram.txt quadram.txt).
2. Wyrzucamy zbędne symbole, których nie ma w alfabecie (w plikach albo w pamięci), liczymy i zapisujemy w formacie znaki - cyfry
3. Klucz - szukanie na poziomych cyfrach, możliwe jednoznaczne obliczenie.
4. Klucz składa się z 3 liczb, 7 symboli znanych o nieznanej kolejności, 30 pozostałych symbolach. (łączna długość == 40)
5. Najprościej wyznacza się te 3 pierwsze liczby.
szyfr substytucji
metoda wspinaczki lub wyżarzanie
'''

'''Define encoding function '''
def encode(tekst,table):


    '''Creating dictionary of numbers and characters'''
    slownik_kodu = {}
    z = 1
    x = []
    y = []
    a1 = 0
    a2 = 0
    a3 = 0
    while z < 5:
        for i in table[z]:
            if i != "" and z == 1:
                x.append(i)
                y.append(table[0][len(x) + 2])

            else:
                if z == 2:

                    x.append(i)
                    y.append(f"8{table[0][a1]}")
                    a1 += 1
                elif z == 3:
                    x.append(i)
                    y.append(f"3{table[0][a2]}")
                    a2 += 1
                elif z == 4:
                    x.append(i)
                    y.append(f"1{table[0][a3]}")
                    a3 += 1

        zipobj = zip(x, y)
        slownik_kodu.update(zipobj)
        z += 1

    result=""
    tekst=tekst.lower()
    for i in tekst:
        if i in slownik_kodu.keys():
            result = result + slownik_kodu[i] + " "

    print("*******Szyfrowanie********")
    return f"{result.replace(' ', '')}"


'''Define decode func'''

def decode(proba,table):

    '''Creating dictionary of numbers and characters'''
    slownik_kodu = {}
    z = 1
    x = []
    y = []
    a1 = 0
    a2 = 0
    a3 = 0
    while z < 5:
        for i in table[z]:
            if i != "" and z == 1:
                x.append(i)
                y.append(table[0][len(x) + 2])

            else:
                if z == 2:

                    x.append(i)
                    y.append(f"8{table[0][a1]}")
                    a1 += 1
                elif z == 3:
                    x.append(i)
                    y.append(f"3{table[0][a2]}")
                    a2 += 1
                elif z == 4:
                    x.append(i)
                    y.append(f"1{table[0][a3]}")
                    a3 += 1

        zipobj = zip(x, y)
        slownik_kodu.update(zipobj)
        z += 1

    result=""


    wskaznik=0
    decode_list=[]

    while wskaznik< len(proba):
        if proba[wskaznik] in slownik_kodu.values():
            decode_list.append(proba[wskaznik])
            wskaznik+=1
        else:
            decode_list.append(proba[wskaznik]+proba[wskaznik+1])
            wskaznik+=2

    for i,j in enumerate(decode_list):
        for k,v in slownik_kodu.items():
            if j==v:
                result=result+k

    print("*******Deszyfrowanie********")
    return f"{result.capitalize()}"


# proba1="Wszechświat ma około czternaście miliardów lat."
# print(encode(proba1,table))
#
# proba2="81305033193881278493279634636693358408547383320932210278537898191078417"
# print(decode(proba2,table))

'''We are gonna to try atack this code in atack below.'''

ngrams= Ngram_score("pl_quadgram.txt", sep="$")

nr_pl_znak_i_inter=[243,261,263,281,322,324,347,378,380,47,63,46,32,44]

alphabet = "".join([chr(97+i) for i in range(26)])

for i in nr_pl_znak_i_inter:
    alphabet=alphabet+chr(i)
print(alphabet)
print(len(alphabet))

tekst_jawny= """

Krótka i piękna kariera Zenona Ziembiewicza, zakończona tak groteskowo i tragicznie, dała
się teraz od strony tego niedorzecznego finału rozważać całkiem na nowo. Jego powszechnie
znana sylwetka, trochę pochylona, przemykająca prawie co dnia długim, odkrytym autem
przez ulice miasta, jego twarz o garbatym profilu i ascetycznie wydłużonej dolnej szczęce, dla
jednych przyjemna i nawet rasowa, dla innych jezuicka i nienawistna, jego zachowanie się w
różnych poszczególnych sytuacjach, jego niektóre zapamiętane słowa - to wszystko otrzymało
teraz zupełnie inne kwalifikacje.
Katastrofa, która zwaliła się na dom Ziembiewiczów, wydawała się niczym nie przygotowana,
jak spadająca na głowę z otwartego okna doniczka z pelargonią. Nie wyjaśniała sytuacji,
raczej zaciemniała ją do reszty. Istotne przyczyny wypadku nie dały się łatwo wyrozumieć -
zwłaszcza jeżeli wziąć pod uwagę, że Ziembiewicz prowadził życie spokojne i dobrze
zorganizowane, nie zdawał się poszukiwać żadnych przygód, a w lepszych kołach
towarzyskich uchodził nawet za człowieka bardzo pod każdym względem przyzwoitego -
mimo poglądów nowoczesnych i przynależności politycznej raczej nieprzyjemnej.
Umiera się w byle jakim miejscu życia. I dzieje człowieka zawarte między urodzeniem jego a
śmiercią wyglądają niekiedy jak nonsens. Któż bowiem jest w możności o każdej chwili
przemijającej pamiętać, by mogła ona być na wszelki wypadek jego gestem ostatnim? Śmierć
nieraz chwyta człowieka in flagranti, zanim zdążył przedsięwziąć jakiekolwiek środki
ostrożności. Najbardziej logiczny plan życia, najściślej wyprowadzona formuła jego wartości
rozpada się nagle, gdy ujawniona zostanie ostatnia niewiadoma
W wypadku Zenona Ziembiewicza było to może tylko zobiektywizowanie. Bo póki żył - od
strony siebie, umieszczony pośrodku swego życia, zabezpieczony swą świadomością i nią
jakoś usprawiedliwiony - wyglądał na pewno inaczej. Miał swoje zasady, racje i motywy
postępowania w taki właśnie sposób, nie inny. Nawet stosunek do może przystojnej, ale
ostatecznie całkiem pospolitej dziewczyny musiał mieć jakiś sens w jego rozumieniu. Teraz
wszelkie przesłanki subiektywne, motywy, konieczności, wszelkie imponderabilia zapadły się
wraz z nim. Był widziany już tylko od zewnątrz, od strony tej ulicy, która go sądziła z jego
czynów, z jego publicznych słów, która znała tylko fakty. Nie było już czego temu
przeciwstawić. Sprawa była taka, jak wyglądała: pospolity skandal, ujawnienie się romansu z
wychowanką czy protegowaną własnej żony, rzecz niesmaczna, której nie umiał przyzwoicie
ani dorzecznie, po męsku, załatwić.
O przebywającej teraz w więzieniu owej dziewczynie, niejakiej Justynie Bogutównie,
mówiono, że podczas swej ostatniej bytności u Ziembiewicza, w jego biurze, zachowywała
się jak historyczka, że jej krzyk słychać było w całym gmachu. Po aresztowaniu uspokoiła się
natychmiast i przyznała do winy, nie chciała jednak wyjawić jej motywów. Mówiła tylko,
jeszcze widocznie pod działaniem wstrząsu, że jest "przysłana od umarłych", i bez żadnych
oznak protestu dała się odwieźć do więzienia."""

tekst_jawny=tekst_jawny.replace("\n"," ")

krypto_tekst=encode(tekst_jawny,table)
print(krypto_tekst)
print(decode(krypto_tekst,table))

#**************************************************************

slow_czestotliwosci={}
for znak in krypto_tekst:
    if znak not in slow_czestotliwosci:
        d1={znak:1}
        slow_czestotliwosci.update(d1)
    else:
        slow_czestotliwosci[znak]+=1
slow_czestotliwosci=sorted(slow_czestotliwosci.items(),key=lambda item: item[1], reverse=True)

print(slow_czestotliwosci)

