from argparse import ArgumentParser

parser = ArgumentParser(description="A 'Hello, world!' program")

parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.2.3")
parser.add_argument("name", help="Your name")
parser.add_argument("-s", "--salutation", default="Hello", help="A greeting")
parser.add_argument("-c", "--color", action="store_true", help="Colorize the text")

args = parser.parse_args()

color = "\033[95m" if args.color else ""
print(f"{color}{args.salutation}, {args.name}!")
