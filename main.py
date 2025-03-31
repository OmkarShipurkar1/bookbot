from stats import count_words, count_chars, sort_dict
import sys

if len(sys.argv) != 2: 
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text():
    with open(f"{book_path}") as f:
        file_contents = f.read()

    return file_contents


car = {
  "brand": "Toyota",
  "model": "Camry",
  "year": 2019
}


print("============ BOOKBOT ============")
print(f"Analyzing book found at {book_path}...")
print("----------- Word Count ----------")
print(count_words(get_book_text()))
print("--------- Character Count -------")
sorted_dict = sort_dict(count_chars(get_book_text()))
for _ in sorted_dict:
    if _.isalpha():
        print(f"{_}: {sorted_dict[_]}")
    else:
        continue
print("============= END ===============")


