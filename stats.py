def get_words(file_contents):
    words = file_contents.split()
    return len(words)

def num_char(file_contents):
    num_letter = {}

    for char in file_contents:
        letter = char.lower()
        if letter in num_letter:
            num_letter[letter] += 1
        else:
            num_letter[letter] = 1
    return(num_letter)

def sort_dict(num_letter):
    sorted_list = []
    for letter, num in num_letter.items():
        sorted_list.append({"letter": letter, "num": num})
    sorted_list.sort(key = lambda item: item["num"], reverse = True)
    return sorted_list


    