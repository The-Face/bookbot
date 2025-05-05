def get_num_words(text):
   word_list = text.split()
   word_count = len(word_list)
   return word_count

def get_num_character(text):
   character_count = {}
   for char in text:
      char = char.lower()
      if char in character_count:
         character_count[char] += 1
      else:
         character_count[char] = 1
   return character_count

def sort_on(dict):
   return dict[1]

def convert_to_list(dict):
   character_list = list(dict.items())
   return character_list
