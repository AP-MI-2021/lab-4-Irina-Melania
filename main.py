list = []
n= int(input("Introduceti numarul de elemente al listei"))
i=0
print("Introduceti elementele: ")
for i in range(0,n):
    x = int(input())
    list.append(x)
    i=i+1
i=0
for i in range(0,n):
    elem=list[i]
    if elem<0:
        print(elem)
least=0
cifra=int(input("Introduceti cifra:"))
for elem in list:
    if elem%10==cifra and (least==0 or elem<least):
        least=elem
print(least)


