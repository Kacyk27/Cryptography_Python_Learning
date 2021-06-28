from itertools import islice, tee
quad_dict={}
n=4
lista=[]
with open("plik_do_quadgramu.txt","r",encoding="utf-8") as file:
    for line in file.readlines():
        wskaznik=0
        quadgram = zip(*(islice(seq, index, None) for index,seq in enumerate(tee(line,n))))
        lista1=list(quadgram)
        lista.append(lista1)


lista2=[]
for i in lista:
    for j in i:
        chars=f"{j[0]}{j[1]}{j[2]}{j[3]}"
        lista2.append(chars)

for i in lista2:
    if i not in quad_dict:
        d1={i:1}
        quad_dict.update(d1)
    else:
        quad_dict[i]+=1


quad_dict=sorted(quad_dict.items(),key=lambda item: item[1], reverse=True)


with open("pl_quadgram.txt","w", encoding="utf-8") as file:
    for k,v in quad_dict:
        file.write(f"{k}${v}\n")