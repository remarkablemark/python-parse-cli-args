from sys import argv

if len(argv) > 1:
    args = argv[1:]
    print(f"Arguments passed: {args}")
else:
    print("No arguments passed.")
