def get_no_of_words(text):
    words = text.split()
    num = len(words)

    return num

def get_no_of_chars(text):

    chars_dict = {}

    for i in text:
        character = i.lower()
        if character in chars_dict:
            chars_dict[character] += 1
        else:
            chars_dict[character] = 1
    
    return chars_dict

def sort_on(items):
    return items["num"]

def sorted_list(dict_of_chars):

    sorted = []
    for i in dict_of_chars:
        if i.isalpha():
            sorted.append({"char":i,"num":dict_of_chars[i]})

    sorted.sort(reverse=True, key=sort_on)

    for i in sorted:
        character, nums = i["char"], i["num"]
        print(f"{character}: {nums}")
    
