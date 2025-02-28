import random
import string

#generate randon number of dictionaries
def generate_dictionaries(n,c):#n-number of dictionaries in the list, c-number of keys in dict
    num_dicts = random.randint(2, n)
    list_of_dicts = []

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
    result_dict={}
    for i, d in enumerate(generate_dictionaries[0:],2):
        for k, v in d.items():
            new_key = f"{k}_{i-1}"  # add prefix to key with max value
            if k in result_dict:#if key is already in result dict
                if v > result_dict[k]: #and value this key > key in result dict
                    result_dict[k] = v  #then assign bigger value to this key
                    result_dict[new_key] = v #write key with prefix to result dict
            else:
                result_dict[k] = v #otherwise just add new pair to result dict
    return dict(sorted(result_dict.items()))


list_of_dictionaries = generate_dictionaries(4,2)
print(list_of_dictionaries)
common_dictionary = generate_common_dict(list_of_dictionaries)
print(common_dictionary)
