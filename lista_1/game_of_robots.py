nk = input().split()
n,k = int(nk[0]), int(nk[1])
sequence = input().split()

num = 0
for c in range(n):
    num += c
    if num >= k:
        num -= c
        break

dif = k - num
print(sequence[dif-1])
