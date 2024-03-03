import re

def find_sequences(pattern, text):
    
    sequences = re.findall(pattern, text)
    return sequences

pattern = r'[a-z]+_[a-z]+'  


test_string = "This_is_a_test_string_with_multiple_sequences_like_this_one_or_this_one_too"

sequences_found = find_sequences(pattern, test_string)

if sequences_found:
    print("Sequences found:")
    for seq in sequences_found:
        print(seq)
else:
    print("No sequences found")