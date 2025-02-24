from stats import word_counter
from stats import letter_counter

def get_book_text(path):
    with open(path) as file:
        text = ""
        for line in file:
            text += line
    return text


def main():
    frank = get_book_text("books/frankenstein.txt")

    word_counter(frank)

    letters = letter_counter(frank)
    print(letters)

main()