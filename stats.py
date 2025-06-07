def get_book_text(book):
    with open(f"books/{book}.txt") as f:
        file_contents = f.read()
    return file_contents


def get_num_words(book):
    text = get_book_text(book)
    words = text.split()
    return len(words)


def get_num_chars(book):
    text = get_book_text(book)
    chars = {}
    for char in text:
        c = char.lower()
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_on(dict):
    return dict["num"]


def sorted_list_from_dict_of_chars(dict):
    chars = []
    for char in dict:
        chars.append({"char": char, "num": dict[char]})
    chars.sort(reverse=True, key=sort_on)
    return chars


def pretty_print_book_info(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}.txt...")
    print("----------- Word Count ----------")
    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    list_of_chars = sorted_list_from_dict_of_chars(get_num_chars(book))
    for char in list_of_chars:
        print(f"{char['char']}: {char['num']}")
    print("============= END ===============")
