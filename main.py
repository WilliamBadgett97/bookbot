def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    number_of_words = count_words(text)
    word_count = number_of_letter_occurrences(text)
    generate_report(word_count, book_path, number_of_words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(str):
    return len(str.split())


def number_of_letter_occurrences(text):
    word_count = {}
    for c in text:
        if c.isalpha():
            letter_to_append = c.lower()
            if letter_to_append in word_count:
                word_count[letter_to_append] += 1
            else:
                word_count[letter_to_append] = 1
    return word_count

def generate_report(word_count, book_path, number_of_words):
    # convert dict to list of dict - So we can sort
    def sort_on(dict):
        # Sort on the count key
        return dict["count"]
    
    list_of_chars = []
    for k,v in word_count.items():
        list_of_chars.append({'letter':k, 'count': v})
    list_of_chars.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path}---")

    print(f"{number_of_words} words found in the document \n")

    for item in list_of_chars:
        print(f"The {item['letter']} character was found {item['count']} times")
    
    print("--- End report ---")
    








main()


