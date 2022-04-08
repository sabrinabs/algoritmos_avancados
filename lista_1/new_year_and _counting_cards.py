s = input()

count = 0
for c in s:
    if c in 'aeiou' or (c.isdigit() == True and int(c) % 2 != 0): count += 1

print(count)
