def count_words(text):
    return len(text.split())

def count_characters(text):
    # Text transform
    whole_text = text.lower()
    # Set of characters in text
    char_list = set(whole_text)
    # Creating the result without count
    result = {}
    for char in char_list:
        result[char] = 0
    # Counting each character and adding it into the result
    for char in whole_text:
        if char in char_list:
            result[char] +=1

    return result

def sort_on(items):
    return items["num"]

def sort_result(result):
    new_list = []
    for key in result:
        value = result[key]
        entry = {"name": key, "num": value}
        new_list.append(entry)
    new_list.sort(reverse=True, key=sort_on)
    return new_list
