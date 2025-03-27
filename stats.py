def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    
    return file_contents

def word_count(text):
    return len(text.split())

def character_count(text):
    char_dic = {}
    lower_case_text = text.lower()
    for c in lower_case_text:
        char_dic[c] = char_dic.get(c, 0) + 1
    
    return char_dic

def sorted_dic(dic):
    updated_dic = sorted(dic.items(), key=lambda item: item[1], reverse=True)
    return updated_dic