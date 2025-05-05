import sys

if len(sys.argv) != 2:
   print("Usage: python3 main.py <path_to_book>")
   sys.exit(1)

def get_book_text(filepath):
   with open(filepath) as f:
      text = f.read()
   return text

from stats import get_num_words

text = get_book_text(sys.argv[1])
word_count = get_num_words(text)

from stats import get_num_character

character_count = get_num_character(text)

from stats import sort_on

from stats import convert_to_list

converted_list = convert_to_list(character_count)
sorted_list = sorted(converted_list, key=sort_on, reverse=True)

print("============BOOKBOT============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("-----------Word Count----------")
print(f"Found {word_count} total words")

for char, num in sorted_list:
   if char.isalpha() == True:
      print(f"{char}: {num}")

print("==========END==========")
