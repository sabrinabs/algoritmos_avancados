def ehab(x):
    n = []
    for c in range(1, x+1): n.append(c)

    for i in range(x):
        for j in range(x):
                if (n[i] % n[j] == 0 and n[i]*n[j] > x and n[i] / n[j] < x): return print(n[i], n[j])
                elif (n[j] % n[i] == 0 and n[i]*n[j] > x and n[j] / n[i] < x): return print(n[j], n[i]) 
    
    return print(-1)

x = int(input())
ehab(x)

