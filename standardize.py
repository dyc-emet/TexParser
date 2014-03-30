import re

def standardize(object):
    list_found = re.findall(r'\^[0-9a-zA-Z]', object.origin)
    for element in list_found:
        object.origin = object.origin.replace(element, '^{' + element[-1] + '}')
    list_found = re.findall(r'_[0-9a-zA-Z]', object.origin)
    for element in list_found:
        object.origin = object.origin.replace(element, '_{' + element[-1] + '}')
    list_found = re.findall(r' {2,}', object.origin)
    for element in list_found:
        object.origin = object.origin.replace(element, ' ')
