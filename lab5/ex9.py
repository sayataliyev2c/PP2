import re

def insert_spaces(input_string):
 
    modified_string = re.sub(r'([a-z])([A-Z])', r'\1 \2', input_string)
    return modified_string


sample_string = "ThisIsASampleStringWithCapitalWords"

modified_string = insert_spaces(sample_string)
print("Modified string:", modified_string)