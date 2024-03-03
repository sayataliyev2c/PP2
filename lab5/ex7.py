def snake_to_camel(snake_case):
    
    words = snake_case.split('_')
    
   
    camel_case_words = [words[0]] + [word.capitalize() for word in words[1:]]
    
   
    camel_case = ''.join(camel_case_words)
    
    return camel_case


snake_string = "this_is_a_sample_snake_case_string"

camel_string = snake_to_camel(snake_string)
print("Camel case:", camel_string)