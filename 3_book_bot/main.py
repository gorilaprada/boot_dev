import sys
from stats import count_words, count_characters, sort_result, sort_on

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

arg_1_path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    text = get_book_text(arg_1_path)
    word_count = count_words(text)
    char_dict = count_characters(text)
    sorted_results = sort_result(char_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {arg_1_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_results:
        if item["name"].isalpha():
            print(f"{item["name"]}: {item["num"]}")
    print("============= END ===============")

main()
