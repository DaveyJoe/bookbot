from stats import get_no_of_words, get_no_of_chars, sorted_list
import sys


def get_book_text(file_path):

    file_content = ""
    with open(file_path) as f:

        file_content = f.read()

        return file_content
    

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:

        path = sys.argv[1]

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {get_no_of_words(get_book_text(path))} total words")
        print("--------- Character Count -------")
        sorted_list(get_no_of_chars(get_book_text(path)))

main()
