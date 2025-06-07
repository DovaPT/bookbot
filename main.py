def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def get_word_count():
    text = get_book_text()
    words = text.split()
    return len(words)


def main():
    num_words = get_word_count()
    print(f"{num_words} words found in the document")


main()
