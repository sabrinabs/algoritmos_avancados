n = input().split()
lista = input().split()
ones = lista.count('1')

for c in range(int(n[1])):
    ent = input().split()
    a, b = int(ent[0]), int(ent[1])

    if a == 1: 
        if lista[b-1] == '1': ones -= 1
        elif lista[b-1] == '0': ones += 1
        lista[b-1] =  str((1 - int(lista[b-1])))
    
    elif a == 2: print(0) if b > ones else print(1)

