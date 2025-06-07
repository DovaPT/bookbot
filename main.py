from stats import pretty_print_book_info
import sys


def main():
    args = sys.argv
    if len(args) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    pretty_print_book_info(args[1])


main()
