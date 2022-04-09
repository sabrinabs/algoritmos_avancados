def do_not_be_distracted(str):
    lista_n_repetidas = []
    for c in str: 
        if c not in lista_n_repetidas: lista_n_repetidas.append(c)
    
    verificadas = []
    for i in range(len(lista_n_repetidas)):
        for j in range(len(str)-1):
            if str[j] not in verificadas:
                if str[j] != str[j+1]:
                    verificadas.append(str[j])
                    c = j
                    f = len(str) - 1
                    for k in range(c, len(str)-1):
                        if str[c] == str[f]:
                            return 'NO'
                        else:
                            f -= 1
        
    return 'YES'

n = int(input())
for l in range(n):
    d = int(input())
    str = input()
    print(do_not_be_distracted(str))
                    
                    
