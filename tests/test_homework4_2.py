import unittest
from homeworks.homework4_2 import normalize_sentence, define_insert, calculate_whitespaspaсes, process_text

class TestHomework4_2(unittest.TestCase):
    def setUp(self):
        self.input_text = '''homEwork:
tHis iz your homeWork, copy these Text to variable.



You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
'''
        self.expected_text = '''Homework:
this is your homework, copy these text to variable.



you need to normalize it from letter cases point of view. also, create one more sentence with last words of each existing sentence and add it to the end of this paragraph.variable view paragraph here mistake tex whitespaces 87.



it is misspelling here. fix“iz” with correct “is”, but only when it is a mistake.



last is to calculate number of whitespace characters in this tex. carefull, not only spaces, but all whitespaces. i got 87.
'''

    def test_calculate_whitespaces_known_value(self):
        normalized_text = normalize_sentence(self.input_text)
        whitespace_count = calculate_whitespaspaсes(normalized_text)
        self.assertEqual(whitespace_count, 87)

    def test_normalize_sentence(self):
        input_text = 'it iZ misspeLLing here.'
        normalized_text = normalize_sentence(input_text)
        self.assertEqual(normalized_text, 'it is misspelling here.')

    # def test_correct_insert(self):
    #     input_text = 'check this. whatever it. test test works. really works fine. and word paragraph. '
    #     self.normalized_text = normalize_sentence(self.input_text)
    #     self.expected_last_words_sentence = "this it works fine paragraph"
    #     self.word_after_paragraph = "variable view paragraph here mistake tex whitespaces 87."


class TestDefineInsert(unittest.TestCase):
    def test_correct_last_words_sentence(self):
        input_text = 'check this. whatever is. test test works. really works fine. and word paragraph. '
        normalized_text = normalize_sentence(input_text)
        #expected combined sentence
        expected_last_words_sentence = "this is works fine paragraph."
        #call foo
        result_text = define_insert(normalized_text)

        sentences = result_text.split("\n")
        self.assertIn(expected_last_words_sentence, result_text,
                      "last word sentence is not correct")

    def test_correct_insert_position(self):#check if inserted in correct position
        input_text = 'check this. whatever is. test test works. really works fine. and word paragraph. '
        normalized_text = normalize_sentence(input_text)
        expected_last_words_sentence = "this is works fine paragraph."

        # call foo
        result_text = define_insert(normalized_text)

        # find word paragraph
        paragraph_pos = result_text.lower().find("paragraph.")

        # check where inserted
        post_paragraph_content = result_text[paragraph_pos + len("paragraph."):]
        self.assertTrue(post_paragraph_content.strip().startswith(expected_last_words_sentence),
                        f"sentence inserted in wrong position': {post_paragraph_content.strip()}")



class TestNormalizeSentence(unittest.TestCase):
    def test_replace_standalone_iz(self):
        # test case 1 standalone iz
        input_text = "This iz a test."
        normalized_text = normalize_sentence(input_text)
        self.assertEqual(normalized_text, "this is a test.")

        #test case 2 "iz"
        input_text = 'This "iZ" a test.'
        normalized_text = normalize_sentence(input_text)
        self.assertEqual(normalized_text, 'this "iz" a test.')

if __name__ == "__main__":
    unittest.main()