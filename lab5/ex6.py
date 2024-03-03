import re

def replace_characters(text):
   
    modified_text = re.sub(r'[ ,.]', ':', text)
    return modified_text


sample_string = "This is a sample, string. With spaces and, commas."

modified_string = replace_characters(sample_string)
print("Modified string:", modified_string)