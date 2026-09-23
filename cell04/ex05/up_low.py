text = input()

for i in text:
    if i.islower():
        print(i.upper(), end='')
    else:
        print(i.lower(), end='')