number = 0

while number < 11:
    mult = 0
    print(f"Table de {number}:", end="")

    while mult < 11:
        result = number * mult
        print(f" {result}", end="")
        mult += 1

    print()
    number += 1
