import re

def match_string(pattern, text):
    
    match = re.search(pattern, text)
    if match:
        print("Match found:", match.group())
    else:
        print("No match found")

pattern = r'a.*b$'  

test_strings = ["acb", "aabcdb", "aefghijb", "ab", "bcd", "abc"]

for test_str in test_strings:
    print("Testing with string:", test_str)
    match_string(pattern, test_str)