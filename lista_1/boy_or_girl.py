user_name = input()
letters = []
for i in user_name:
    if i not in letters: letters.append(i)

print("CHAT WITH HER!") if len(letters) % 2 == 0 else print("IGNORE HIM!")
