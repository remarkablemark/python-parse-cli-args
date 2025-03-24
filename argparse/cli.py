from argparse import ArgumentParser

parser = ArgumentParser(
    prog="argparse/cli",
    description="'Hello, world!' program",
    epilog="https://docs.python.org/library/argparse.html"
    # add_help=False
)

parser.add_argument("--version", "-v", action="version", version="%(prog)s 1.2.3")
# parser.add_argument("--help", action="help", help="show this help message and exit")

parser.add_argument("name", help="name to greet")
parser.add_argument("--salutation", "-s", default="Hello", help="greeting or salutation")
parser.add_argument("--color", "-c", action="store_true", help="colorize the text")

args = parser.parse_args()

color = "\033[95m" if args.color else ""
print(f"{color}{args.salutation}, {args.name}!")
