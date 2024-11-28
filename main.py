def count_words(file_contents):
     num_of_words = 0
     lines = file_contents.split()
     num_of_words += len(lines)
     return num_of_words

def count_characters(file_contents):
    """
    Returns count of occurances in text of each character from a to z. 
    """
    char_count = {}
    for char in file_contents:
        if char in char_count:
            if char.isalpha():
                char_count[char.lower()] +=1
        else:
            if char.isalpha(): 
                char_count[char.lower()] = 1
    return char_count




def read_book_contents():
    with open('./books/frankenstein.txt') as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt")
        print(f"{count_words(file_contents)} words found in the document")
        char_count = count_characters(file_contents)
        sorted_char_connt = dict(sorted(char_count.items()))
        for char, count in sorted_char_connt.items():
            print(f"The '{char}' was found {count} times")





def main():
    read_book_contents()


if __name__ == '__main__':
    main()


