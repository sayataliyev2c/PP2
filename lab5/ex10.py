def camel_to_snake(camel_case):
    snake_case = ''
    for i, char in enumerate(camel_case):
        if i > 0 and char.isupper():
            snake_case += '_'
        snake_case += char.lower()
    return snake_case


camel_string = "ThisIsASampleCamelCaseString"

snake_string = camel_to_snake(camel_string)
print("Snake case:", snake_string)