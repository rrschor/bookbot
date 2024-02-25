import os

# Get the current working directory
cwd = os.getcwd()

# Get txt files from ./books/ directory
txt_files = [file for file in os.listdir('books') if file.endswith('.txt')]

def open_file(file):
    with open(f'books/{file}', 'r') as file:
        book_text = file.read()
        number_of_characters = len(book_text.split())
        return book_text, number_of_characters

def count_chars(text):
    char_dict = {}
    chars = sorted(list(set(text.lower())))
    for char in chars:
        if char.isalpha():
            char_dict[char] = text.lower().count(char)
    return len(chars), char_dict

def build_report_text(text):
    num_chars, char_dict = count_chars(text)
    report_text = f'The text contains {num_chars} unique characters.\n'
    ordered_list = reversed(sorted(char_dict.items(), key=lambda x:x[1]))
    for char in ordered_list:
        report_text += f"The '{char[0]}' character was found {char[1]} times\n"
    return report_text

if __name__ == '__main__':
    for file in txt_files:
        book_text, number_of_characters = open_file(file)
        report_text = build_report_text(book_text)
        print(f'--- Begin report of {file.split('.')[0]}---')
        print(f'{file.split('.')[0]} contains {number_of_characters} words.')
        print('\n')
        print(report_text)
        print('\n')
        print(f'--- End report of {file.split('.')[0]}---')
