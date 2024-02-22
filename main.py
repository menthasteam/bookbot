
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)
    num_letters_lst = dict_to_lst(num_letters)
    num_letters_lst.sort(key=sort_on, reverse=True)
    
    print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n")
    for letter_dict in num_letters_lst:
        print(f"The '{letter_dict['character']}' character was found {letter_dict['count']} times")
    print("--- End report ---")


def dict_to_lst(original_dict):
    list_of_dictionaries = []
    for key in original_dict:
        new_dict = {'character': key, 'count': original_dict[key]}
        list_of_dictionaries.append(new_dict)
    return list_of_dictionaries


def sort_on(dict_item):
    return dict_item["count"]


def get_num_letters(text):
    letters_dict = {}
    text_lowered = text.lower()
    for char in text_lowered:
        if char.isalpha():
            if char in letters_dict:
                letters_dict[char] += 1
            else:
                letters_dict[char] = 1
    return letters_dict

    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()




main()
