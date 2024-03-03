import re

def split_at_uppercase(input_string):
    

    split_strings = re.findall(r'[A-Z][^A-Z]*', input_string)
    return split_strings


sample_string = "ThisIsASampleStringWithUppercaseLetters"

split_strings = split_at_uppercase(sample_string)
print("Split strings:", split_strings)