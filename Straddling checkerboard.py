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

    return f"Zaszyfrowany tekst: {result.replace(' ', '')}"

proba1="Wszechświat ma około czternaście miliardów lat."

print(encode(proba1,table))

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


    return f"Tekst odszyfrowany: {result.capitalize()}"


proba2="81305033193881278493279634636693358408547383320932210278537898191078417"

print(decode(proba2,table))

'''We are gonna to try atack this code in atack below this comment.'''

# ngrams= Ngram_score("pl_quadgrams_zmniejszone.txt")

nr_pl_znak_i_inter=[243,261,263,281,322,324,347,378,380,47,63,46,32,44]

alphabet = "".join([chr(97+i) for i in range(26)])

for i in nr_pl_znak_i_inter:
    alphabet=alphabet+chr(i)




