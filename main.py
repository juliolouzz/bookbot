def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words_number = find_number_words(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{words_number} words found in the text \n")
    letters = find_letters_ocurrences(text)
    list_of_dicts = convert_dict_to_list(letters)
    sorted_list_of_dicts = sorted(list_of_dicts, key=lambda v: v["count"], reverse=True )
    print_report(sorted_list_of_dicts)
    print("--- End report ---")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()


def find_number_words(text):
    text_to_list_string = text.split()
    words_number = len(text_to_list_string)
    return words_number


def find_letters_ocurrences(text):
    lowerd_text = text.lower()
    letters_dict = {}
    for letter in lowerd_text:
        if letter.isalpha():
            if letter in letters_dict:
                letters_dict[letter] += 1
            else:
                letters_dict[letter] = 1
    return letters_dict


def convert_dict_to_list(dict_obj):
    list_of_dicts = [{"letter": k, "count": v} for k, v in dict_obj.items()]
    return list_of_dicts

def print_report(sorted_list_of_dicts):
    for item in sorted_list_of_dicts:
        print(f"The '{item['letter']}' character was found {item['count']} times")


main()