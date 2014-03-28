import re

def convert_integer(object):
    object_searched = re.search(r'[^S][^0-9\.]([0-9]+)[^0-9\.]', object.origin)
    while object_searched:
        begin_integer = object_searched.span()[0] + 2
        end_integer = begin_integer + len(object_searched.group(1))
        object.origin = object.origin[:begin_integer] + 'S(' + object_searched.group(1) + ')' + object.origin[end_integer:]
        print(object.origin)
        object_searched = re.search(r'[^S][^0-9\.]([0-9]+)[^0-9\.]', object.origin)
    object_searched = re.search(r'[^S][^0-9\.]([0-9]+)$', object.origin)
    if object_searched:
        begin_integer = object_searched.span()[0] + 2
        end_integer = begin_integer + len(object_searched.group(1))
        object.origin = object.origin[:begin_integer] + 'S(' + object_searched.group(1) + ')' + object.origin[end_integer:]
