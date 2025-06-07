from stats import get_num_chars, get_num_words


def main():
    num_words = get_num_words()
    print(f"{num_words} words found in the document")
    num_chars = get_num_chars()
    print(num_chars)


main()
