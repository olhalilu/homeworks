import pytest
from homeworks.homework4_1 import generate_dictionaries, generate_common_dict

def  test_correct_number_of_dicts():
    result = generate_dictionaries(5,3)
    assert  len(result) in range(2,6),"incorrect dict number"

def test_correct_number_keys():
    result = generate_dictionaries(5, 3)
    for dictionary in result:
        assert 1<=len(dictionary)<=3, "incorrect keys number in dict"

def test_keys_and_values():
    #result = generate_dictionaries(5, 3)
    result=[{"a":2,"b":3}]
    for dictionary in result:
        for key, value in dictionary.items():

            assert isinstance(key,str), "key is not string"
            assert key.islower() is True, " key is not lower"
            assert isinstance(value,int),"value in dict is not int"
            assert 1<=value<=100, "incorrect value"

def test_dicts_repeated_keys():
    input_dicts = [
        {'a': 5, 'b': 10},
        {'b': 20, 'c': 15},
        {'a': 25, 'c': 5,'b':15},
    ]

    expected_result = {
        'a_3': 25,
        'b_2': 20,
        'c': 15,
    }

    result = generate_common_dict(input_dicts)
    assert result == expected_result, "incorrect defined biggest value"

def test_dicts_no_repeated_keys():
    input_dicts = [
        {'a': 5, 'b': 10,'d':50},
        {'e': 20, 'c': 15},
        {'k': 25, 'n': 5},
    ]

    expected_result = {
        'a': 5,
        'b': 10,
        'd':50,
        'e': 20,
        'c': 15,
        'k': 25,
        'n': 5
    }
    result = generate_common_dict(input_dicts)
    assert result == expected_result,"incorrect defined when no repeated values in dicts"

def test_single_dict():
    input_dicts = [{'a': 5, 'b': 10, 'c': 15}]
    expected_result = {'a': 5, 'b': 10, 'c': 15}
    result = generate_common_dict(input_dicts)
    assert result == expected_result


