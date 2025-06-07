def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents


def get_num_words():
    text = get_book_text()
    words = text.split()
    return len(words)


def get_num_chars():
    text = get_book_text()
    chars = {}
    for char in text:
        c = char.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars
