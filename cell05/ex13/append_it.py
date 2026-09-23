import sys
if len(sys.argv) < 2:
    print("none")
else:
    matching_params = [param for param in sys.argv[2:] if param.endswith("ism")]
    if matching_params:
        print(", ".join(matching_params))
    else:
        print("none")