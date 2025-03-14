import random
import string

#generate randon number of dictionaries
def generate_dictionaries(n,c):#n-number of dictionaries in the list, c-number of keys in dict
    num_dicts = random.randint(2, n)
    list_of_dicts = []
    print(num_dicts)

    # generate each dictionary
    for i in range(num_dicts):
        # generate random values
        num_keys = random.randint(1, c)
        new_dict = {}
        # generate random keys and values
        for k in range(num_keys):
            key = random.choice(string.ascii_lowercase) # random letter
            value = random.randint(0, 100) # random number [0,100]
            new_dict[key] = value
        list_of_dicts.append(new_dict)

    return list_of_dicts


def generate_common_dict(generate_dictionaries):
    final_dict = {}
    current_dict_number = 1
    result_dict={}
    for d in generate_dictionaries:
        for key, value in d.items():
            # if key is already in dict
            if key in final_dict:
                old_key, old_value, old_dict_number = final_dict[key]
                if value > old_value:
                    new_key = f"{key}_{current_dict_number}"
                    final_dict[key] = (new_key, value, current_dict_number)
            else:
                final_dict[key] = (key, value, current_dict_number)
        current_dict_number += 1

    # final dict
    result_dict = {}
    for key, (full_key, value, idx) in final_dict.items():
        # case key taken from 1 dict
        if full_key == key:
            result_dict[key] = value
        else:
            result_dict[full_key] = value

    return result_dict


if __name__ == "__main__":
    list_of_dictionaries = generate_dictionaries(4,2)
    print(list_of_dictionaries)
    common_dictionary = generate_common_dict(list_of_dictionaries)
    print(common_dictionary)
