import pytest
from  homeworks.homework4_2 import normalize_sentence, define_insert, calculate_whitespaspaсes, process_text

input_text =  '''homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''

def test_calculate_whitespaces_():
    string_input = ('''for testing should be.13     
    ''')
    normalized_text = normalize_sentence(input_text)
    whitespace_count = calculate_whitespaspaсes(normalized_text)
    assert whitespace_count==87, "wrong whitespace count"
    normalized_text = normalize_sentence(string_input)
    whitespace_count = calculate_whitespaspaсes(normalized_text)
    assert whitespace_count == 13, "wrong whitespace count"


def test_normalize_sentence():
    input_text = 'it iZ misspeLLing here.'
    normalized_text = normalize_sentence(input_text)
    assert normalized_text == 'it is misspelling here.',"incorrect normalization text func"


def test_correct_last_words_sentence():
    input_text = 'check this. whatever is. test test works. really works fine. and word paragraph.'
    expected_last_words_sentence = "this is works fine paragraph."
    _,last_word_sentence = define_insert(input_text)
    assert last_word_sentence ==expected_last_words_sentence,"last word sentence is not correct"

def test_correct_insert_position():#check if inserted in correct position
    input_text = '''check this. whatever is. test test works. really works fine. and word paragraph.
    '''
    expected_result = '''check this. whatever is. test test works. really works fine. and word paragraph.
    this is works fine paragraph.'''
    foo_result,_ = define_insert((input_text))
    assert foo_result == expected_result, "sentence inserted in wrong position"

def test_normalization_text():
    input_text = "This iz a test."
    expected_text = "this is a test."
    normalized_text = normalize_sentence(input_text)
    assert normalized_text == expected_text, "incorrect normalization standalone iz"

    input_text = 'This "iZ" a test.'
    normalized_text = normalize_sentence(input_text)
    expected_text = 'this "iz" a test.'
    assert normalized_text == expected_text, "incorrect normalization for iz when it should stay iz"


