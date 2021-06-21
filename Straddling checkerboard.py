table = [["8", "3", "1", "4", "0", "5", "7", "2", "6", "9"],
         ["" ,""  ,""  ,"n" ,"e" ,"z" ,"a" , "i", "o", " "],
         ["ć", "u", "w", "t", "g", "r", "f", "p", "ń", "ó"],
         ["ś", "c", "b", "k", "s", "ę", "d", "m", "ł", "ź"],
         ["ż", "/", "ą", "?", "l", "j", ".", ",", "y", "h"]]

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
    proba=proba.split(" ")

    #Tutaj wstawianie spacji iteracyjnie

    for i,j in enumerate(proba):
        for k,v in slownik_kodu.items():
            if j==v:
                result=result+k



    return f"Tekst odszyfrowany: {result.capitalize()}"


proba2="813050333881278493279634636693358408547383320932210278537898191078417"
#proba2="81 30 5 0 33 19 38 81 2 7 84 9 32 7 9 6 34 6 36 6 9 33 5 84 0 85 4 7 38 33 2 0 9 32 2 10 2 7 85 37 89 81 9 10 7 84 17"

print(decode(proba2,table))


