import re

def match_string(pattern, text):
    
    match = re.search(pattern, text)
    if match:
        print("Match found:", match.group())
    else:
        print("No match found")

pattern = r'ab*' 

test_strings = ["abc", "ac", "abbbc", "aab", "bcd"]

for test_str in test_strings:
    print("Testing with string:", test_str)
    match_string(pattern, test_str)