from stats import get_num_words


def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def main():
    num_words = get_num_words()
    print(f"{num_words} words found in the document")


main()
