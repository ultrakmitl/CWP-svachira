age = int(input("Please tell me your age: "))
print(f"You are {age} years old.")
for i in range(1, 4):
    age += 10
    print(f"In {i * 10} years, you'll be {age} years old.")