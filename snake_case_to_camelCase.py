'''Given a variable name in snake_case, return a string with that
variable name written in camelCase'''

#snake_to_camel("hi_balloonicorn")
# >>> 'hiBalloonicorn'


def snake_to_camel(snake_case):
    """ Return a string that was originally in snake case to camel case """

    i = 0
    snake_case_lst = list(snake_case)
    while i < len(snake_case_lst):
        if snake_case_lst[i] == '_':
            snake_case_lst = snake_case_lst[0:i] + snake_case_lst[i+1:]
            snake_case_lst[i] = snake_case_lst[i].capitalize()
        i += 1
    return ''.join(snake_case_lst)


def test():
    assert snake_to_camel('hi_balloonicorn') == 'hiBalloonicorn'
    assert snake_to_camel('cat_dog') == 'catDog'
    assert snake_to_camel('cat_dog_bird') == 'catDogBird'
    print 'Tests passed'

test()