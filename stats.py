
def count_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"


def count_chars(text):
    chars = {}
    for letter in text:
        letter = letter.lower()
        if letter == ' ':
            continue
        if letter not in chars:
            chars[letter] = 1
        else:
            chars[letter] = chars[letter] + 1

    return chars


def sort_dict(dictionary):
    sorted_list = list(dictionary.items())
    sorted_list.sort(key=lambda item: item[1], reverse=True)
    return dict(sorted_list)



    

        
