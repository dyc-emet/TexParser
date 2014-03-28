import re

def frac(object):
    object_searched = re.search(r'\\frac.*', object.origin)
    index_after_frac = 5
    while object_searched:
        string_to_search = object_searched.group(0)[index_after_frac:]
        up, string_to_search = object.bracket_balance(string_to_search)
        down, string_to_search = object.bracket_balance(string_to_search)
        string_to_be_substituded = '\\frac{' + up + '}{' + down + '}'
        if len(up) > 1:
            up = '(' + up + ')'
        if len(down) > 1:
            down = '(' + down + ')'
        string_to_substitude = up + ' / ' + down
        object.origin = object.origin.replace(string_to_be_substituded, string_to_substitude)
        #print(object.origin)
        object_searched = re.search(r'\\frac.*', object.origin)
