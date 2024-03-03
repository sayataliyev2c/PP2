import re

def find_sequences(pattern, text):
    
    sequences = re.findall(pattern, text)
    return sequences

pattern = r'[A-Z][a-z]+'  


test_string = "This Is a Test String With Multiple Sequences Like This One or This One Too"

sequences_found = find_sequences(pattern, test_string)

if sequences_found:
    print("Sequences found:")
    for seq in sequences_found:
        print(seq)
else:
    print("No sequences found")