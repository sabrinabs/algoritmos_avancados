def shuffle():
    str1 = input()
    str2 = input()

    if len(str1) == len(str2):
        str1, str2 = list(str1), list(str2)
        str1.sort()
        str2.sort()
        if str1 == str2: return "YES"
        else: return 'NO'
    else:
        c, f = 0, len(str1)
        for i in range(len(str2)-len(str1)+1):
            comp = ''
            for j in range(c, f):  comp = comp + str2[j]
            c += 1
            f += 1
            comp, str1 = list(comp), list(str1)
            comp.sort()
            str1.sort()
            if comp == str1: return "YES"
        return 'NO'

n = int(input())
for c in range(n):
    print(shuffle())
