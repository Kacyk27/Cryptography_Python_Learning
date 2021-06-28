x=[]
with open("pl_quadgrams.txt", "r", encoding="utf-8") as file:
    for line in file:
        x.append(line)

with open("pl_quadgrams_zmniejszone.txt","w",encoding="utf-8") as file:
    for i in x:
        print(i.lower(), file=file, end="")
