def word_count(file_contents):
    num_words = file_contents.split()
    return len(num_words)

def char_count(file_contents):
    letter_count = {}
    for char in file_contents:
        if char.isalpha():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count



def sort_letters(char_dict):
    char_list = []

    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})


    char_list.sort(reverse=True, key=lambda x: x["num"])

    return char_list
