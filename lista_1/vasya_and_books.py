n = int(input())
stack = input().split()
steps = input().split()

dicio = {}
for l in range(len(stack)):
    dicio[stack[l]] = l

a = 0  
for c in range(len(steps)):
    index = dicio[steps[c]] 
    if index >= a:
        print((index + 1) - a) 
        a = index + 1
         
    else: print(0)