t = int(input())

for t in range(t):
    inp = input().split()
    a, b, n, count = int(inp[0]), int(inp[1]), int(inp[2]), 0

    while True:
        soma = a + b
        if a > b: b = soma
        else: a = soma
        count += 1

        if soma > n: 
            print(count)
            break





