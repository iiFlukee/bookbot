def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    text = text.lower()
    chars = {}

    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sort_char_counts(char_dict):
    char_list = []
    for char, count in char_dict.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})

    def sort_on(dict_item):
        return dict_item["num"]
    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    