from argparse import ArgumentParser

parser = ArgumentParser(description="A 'Hello, world!' program")

parser.add_argument("-v", "--version", action="version", version="%(prog)s 1.2.3")
parser.add_argument("name", help="Your name")

args = parser.parse_args()

print(f"Hello, {args.name}!")
