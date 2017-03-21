'''Given a variable name in snake_case, return a string with that
variable name written in camelCase'''

#snake_to_camel("hi_balloonicorn")
# >>> 'hiBalloonicorn'


def snake_to_camel(snake_case):
    i = 0
    snake_case_lst = list(snake_case)
    while i < len(snake_case_lst):
        if snake_case_lst[i] == '_':
            snake_case_lst = snake_case_lst[0:i] + snake_case_lst[i+1:]
            snake_case_lst[i] = snake_case_lst[i].capitalize()
        i += 1
    print ''.join(snake_case_lst)

snake_to_camel('hi_balloonicorn')
snake_to_camel('cat_dog')
snake_to_camel('cat_dog_bird')
