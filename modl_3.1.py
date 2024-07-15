calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


# 'Jopa'.lower()  == 'JOPA'.lower()
def is_contains(string, string_list):
    count_calls()
    for item in string_list:
       if string.lower() == item.lower():
           return True
    return False


print(string_info('Salamandra'))
print(string_info('Jopolis'))
print(is_contains('Piska', ['ska', 'PiPiska', 'pISka']))
print(is_contains('jopa', ['jupan', 'jiraf']))
print(calls)


