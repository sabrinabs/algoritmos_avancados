tam = int(input())
sequence = input().split()

result = []
for c in range(len(sequence)-1,-1,-1):
    if sequence[c] not in result: result.insert(0, sequence[c])

print(len(result))
for j in result:
    if j != result[-1]:
        print(j + ' ', end='')
    else:
        print(j)