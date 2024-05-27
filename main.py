def main():
    book_source = "books/frankenstein.txt"
    with open(book_source) as f:
        file_contents = f.read()

    print(f"--- Begin report of {book_source} ---")
    
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")

    letter_count = count_letters(file_contents)
    for letter in letter_count:
        print(f"The '{letter}' character was found {letter_count[letter]} times")

    print("--- End report ---")

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(string):
    lower_string = string.lower()
    chars = {}

    for char in lower_string:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    
    return chars

main()