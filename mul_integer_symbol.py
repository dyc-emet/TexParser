import re

def mul_integer_symbol(object):
    object_searched = re.search(r'([0-9]+)[ ]*([a-zA-Z])', object.origin)
    while object_searched:
        object.origin = object.origin.replace(object_searched.group(0), object_searched.group(1) + '*' + object_searched.group(2))
        #print(object.origin)
        object_searched = re.search(r'([0-9]+)[ ]*([a-zA-Z])', object.origin)

