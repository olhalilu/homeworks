import unittest
from homeworks.homework4_1 import generate_dictionaries, generate_common_dict


class TestGenerateDictionaries(unittest.TestCase):
    def test_correct_number_of_dicts(self):#check if the correct number of dicts generated
        n = 5
        c = 3
        generated = generate_dictionaries(n, c)

        self.assertGreaterEqual(len(generated), 2)
        self.assertLessEqual(len(generated), n)

    def test_keys_and_values(self):#keys- letters, value-numbers
        n = 5
        c = 3
        generated = generate_dictionaries(n, c)

        for dictionary in generated:
            for key, value in dictionary.items():
                self.assertIsInstance(key, str)
                self.assertTrue(key.islower())
                self.assertIsInstance(value, int)
                self.assertGreaterEqual(value, 0)
                self.assertLessEqual(value, 100)

    def test_limit_keys_in_dict(self):
        n = 5
        c = 4
        generated = generate_dictionaries(n, c)

        for dictionary in generated:
            self.assertLessEqual(len(dictionary), c)


class TestGenerateCommonDict(unittest.TestCase):
    def test_common_dict_with_conflicts(self):
        input_dicts = [
            {'a': 5, 'b': 10},
            {'b': 20, 'c': 15},
            {'a': 25, 'c': 5},
        ]

        expected_result = {
            'a_3': 25,
            'b_2': 20,
            'c': 15,
        }

        result = generate_common_dict(input_dicts)
        self.assertEqual(result, expected_result)

    def test_common_dict_with_no_conflicts(self):#keys not repeated and have biggest values
        input_dicts = [
            {'a': 5},
            {'b': 10},
            {'c': 15},
        ]

        expected_result = {
            'a': 5,
            'b': 10,
            'c': 15,
        }

        result = generate_common_dict(input_dicts)
        self.assertEqual(result, expected_result)

    def test_single_dict(self):#case when there is the only 1 dict
        input_dicts = [{'a': 5, 'b': 10, 'c': 15}]

        expected_result = {'a': 5, 'b': 10, 'c': 15}

        result = generate_common_dict(input_dicts)
        self.assertEqual(result, expected_result)




if __name__ == "__main__":
    unittest.main()