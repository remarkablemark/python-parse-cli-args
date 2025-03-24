from argparse import ArgumentParser

parser = ArgumentParser(description="A 'Hello, world!' program")
parser.add_argument("name", help="Your name")

args = parser.parse_args()

print(f"Hello, {args.name}!")
