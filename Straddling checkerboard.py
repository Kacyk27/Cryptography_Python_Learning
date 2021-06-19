table = [["8", "3", "1", "4", "0", "5", "7", "2", "6", "9"],
         ["" ,""  ,""  ,"n" ,"e" ,"z" ,"a" , "i", "o", " "],
         ["ć", "u", "w", "t", "g", "r", "f", "p", "ń", "ó"],
         ["ś", "c", "b", "k", "s", "ę", "d", "m", "ł", "ź"],
         ["ż", "?", "ą", "!", "l", "j", ".", ",", "y", "h"]]

'''Creating dictionary of numbers and characters'''
slownik_kodu={}
z=1
x=[]
y=[]
a1=0
a2=0
a3=0
while z<5:
    for i in table[z]:
        if i != "" and z==1:
            x.append(i)
            y.append(table[0][len(x)+2])

        else:
            if z==2:

                x.append(i)
                y.append(f"8{table[0][a1]}")
                a1+=1
            elif z==3:
                x.append(i)
                y.append(f"3{table[0][a2]}")
                a2+=1
            elif z==4:
                x.append(i)
                y.append(f"1{table[0][a3]}")
                a3+=1

    zipobj = zip(x,y)
    slownik_kodu.update(zipobj)
    z+=1

print(slownik_kodu)

