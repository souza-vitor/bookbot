from stats import word_counter
from stats import letter_counter
from stats import report

def get_book_text(path):
    with open(path) as file:
        text = ""
        for line in file:
            text += line
    return text


def main():
    path_name = "books/frankenstein.txt"
    frank = get_book_text(path_name)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_name}...")
    print("----------- Word Count ----------")

    word_counter(frank)
    print("--------- Character Count -------")
    
    letters = letter_counter(frank)
    letter_list = report(letters)

    for letter in letter_list:
        print(f"{letter['letter']}: {letter['num']}")

    print("============= END ===============")



main()