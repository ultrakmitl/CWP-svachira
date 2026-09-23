array = [2, 8, 9, 48, 8, 22,-12, 2]

print(f"Original array: {array}")

new_array = [num + 2 for num in array if num + 2 > 5]

new_array = list(set(new_array))
print(f"New array: {new_array}")