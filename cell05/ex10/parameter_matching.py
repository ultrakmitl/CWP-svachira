import sys

if len(sys.argv) != 2:
    print("none")
else:
    key = sys.argv[1]
    word = input("What was the parameter? ")
    if key == word:
        print("Good job!")
    else:
        print("Nope, sorry...")