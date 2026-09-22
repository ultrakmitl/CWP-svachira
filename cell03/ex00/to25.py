number = int(input("Enter a number less than 25: "))

if number < 25:
    for i in range(number, 26):
        print(f"Inside the loop, my variable is {number}")
        number += 1
else:
    print("Error")