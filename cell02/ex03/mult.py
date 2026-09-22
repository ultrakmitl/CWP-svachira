first = int(input("Enter the first number: "))
second = int(input("Enter the second number: "))
result = first * second

print(first,"x", second,"=", result)

if result > 0:
	print("The result is positive.")
elif result < 0:
	print("The result is negative.")
else:
	print("This result is both positive and negative.")
