import re


def normalize_sentence(my_string):
    my_string1 = my_string.lower()#lower case
    my_string2 = re.sub(r'(?<![“"])(?<!\w)\biz\b(?!\w)', 'is', my_string1)#replace  standalone iz
    return my_string2

# def define_insert(my_string2):
#     sentences = re.split(r'(?<=[.])', my_string2)
#
#     # last word of every sentences
#     last_words = []
#     for sentence in sentences:
#         words = re.findall(r'\b\w+\b', sentence)
#         if words:
#             last_word = words[-1]
#             last_words.append(last_word)
#     word_after = 'paragraph.'
#     insert_index = my_string2.lower().find('paragraph')
#     sent_last_word = ' '.join(last_words)  #ready sentence
#     sentence_before_insert = my_string2[:insert_index+len(word_after)]#where to insert new sentence
#     sentence_after_insert = my_string2[insert_index+len(word_after):]#where continue the rest of the text after inserting new sentence
#     new_sentence = sentence_before_insert + sent_last_word +"." + sentence_after_insert
#     return new_sentence



def define_insert(my_string2):
    sentences = re.split(r'(?<=[.])', my_string2)

    # last word of every sentences
    last_words = []
    for sentence in sentences:
        words = re.findall(r'\b\w+\b', sentence)
        if words:
            last_word = words[-1]
            last_words.append(last_word)

    # find word 'paragraph' and its position
    word_to_find = 'paragraph.'
    paragraph_index = my_string2.lower().find(word_to_find)  # Позиция слова "paragraph"

    if paragraph_index == -1:
        raise ValueError(f"'{word_to_find}' not found in the text!")

    # word paragraph with all spaces and whitespaces
    insert_index = paragraph_index + len(word_to_find)
    while insert_index < len(my_string2) and my_string2[insert_index] in (' ', '\n', '\t'):
        insert_index += 1

    # sentence consists of last words
    sentence_to_insert = ' '.join(last_words) + '.'

    # insert new combined sentence
    part_before = my_string2[:insert_index]
    part_after = my_string2[insert_index:]
    new_sentence = part_before + '\n' + sentence_to_insert + '\n' + part_after

    return new_sentence

def calculate_whitespaspaсes(new_sentence):
    symbol_counts = 0
    for i in new_sentence:
        if i.isspace():
            symbol_counts += 1
    return symbol_counts


def process_text(my_string):
    normalized_text = normalize_sentence(my_string)
    text_with_new_sentence = define_insert(normalized_text)
    whitespace_count = calculate_whitespaspaсes(text_with_new_sentence)
    whitespace_count_old_sentence = calculate_whitespaspaсes(normalized_text)
    return text_with_new_sentence, whitespace_count,whitespace_count_old_sentence


if __name__ == "__main__":
    my_string = '''homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

    final_text, space_count,space_count_old = process_text(my_string)
    print(final_text)
    print(f"Whitespace count with old sentence: {space_count_old}")
    print(f"Whitespace count with new sentence: {space_count}")
