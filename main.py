from stats import get_book_text, word_count, character_count, sorted_dic
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    
    book_content = get_book_text(file_path)
    words = word_count(book_content)
    char_count = sorted_dic(character_count(book_content))
            
    
    print(f'''============ BOOKBOT ============
Analyzing book found at {file_path}...
----------- Word Count ----------
Found {words} total words
--------- Character Count -------''')
    for key, item in char_count:
        if key.isalpha():
            print(f"{key}: {item}")
    print("============= END ===============")

main()