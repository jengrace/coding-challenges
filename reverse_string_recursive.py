def reverse_str(item):
    if item == '':
        return item
    return item[-1] + reverse_str(item[:-1])

print reverse_str('star')
