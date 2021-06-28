lista=[]
with open("Chlopi.txt","r", encoding="utf-8") as file:
    for line in file.readlines():
        x=line.strip("\n")
        if x != "":
            lista.append(x)

with open("Lalka.txt","r", encoding="utf-8") as file:
    for line in file.readlines():
        x=line.strip("\n").strip("\u2009")
        if x != "":
            lista.append(x)


with open("Pan_Tadeusz.txt","r", encoding="utf-8") as file:
    for line in file.readlines():
        x=line.strip("\n")
        if x != "":
            lista.append(x)


with open("plik_do_quadgramu.txt","w", encoding="utf-8") as file:
    for i in lista:
        i=i.lower()
        file.write(i+" ")
