import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(f"What was parameter? {sys.argv[1]}")

    if sys.argv[1] == "Hello":
        print("Good job!")
    else:
        print("Nope, sorry...")
