import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

from stats import get_words, num_char, sort_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    file_contents =get_book_text(path)
    num_words = get_words(file_contents)
    print(f'Found {num_words} total words')
    num_letter = num_char(file_contents)
    sorted_list = sort_dict(num_letter)
    for item in sorted_list:
        print(f"{item['letter']}: {item['num']}")

main()