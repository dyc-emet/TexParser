import re

def balance_int_d(string_to_match):
    remain_unmatched = 1
    string_to_match = string_to_match[4:]
    content = '\\int'
    while remain_unmatched:
        try_to_match = re.match(r'\\int|d\w+', string_to_match)
        if try_to_match:
            if try_to_match.group(0) == '\\int':
                remain_unmatched += 1
                content += '\\int'
                string_to_match = string_to_match[4:]
            else:
                remain_unmatched -= 1
                content += try_to_match.group(0)
                string_to_match = string_to_match[try_to_match.span()[1]:]
        else :
            content += string_to_match[0]
            string_to_match = string_to_match[1:]
    return content

def integrate(object):
    object_searched = re.search(r'\\int.*d\w+', object.origin)
    index_after_int = 4
    while object_searched:
        complete_int =  balance_int_d(object_searched.group(0))
        if complete_int[index_after_int] == '^':  # \int^..._...
            string_cached = complete_int[index_after_int + 1:]
            if string_cached[0] == '{':
                (up, string_cached) = object.bracket_balance(string_cached)
            else :
                up = string_cached[0]
                string_cached = string_cached[1:]
            string_cached = string_cached[1:]
            if string_cached[0] == '{':
                (down, string_cached) = object.bracket_balance(string_cached)
            else :
                down = string_cached[0]
                string_cached = string_cached[1:]
            content_and_symbol = re.search(r'(.*)d(\w+)',string_cached)
            content = content_and_symbol.group(1)
            symbol = content_and_symbol.group(2)
            #print(further_search.group(0))
            string_to_substitude = 'integrate(' + content + ', (' + symbol + ',' + down + ',' + up + '))'
            #print(string_to_substitude)
            object.origin = object.origin.replace(complete_int, string_to_substitude)
        elif complete_int[index_after_int] == '_':  # \int_...^...
            string_cached = complete_int[index_after_int + 1:]
            if string_cached[0] == '{':
                (down, string_cached) = object.bracket_balance(string_cached)
            else :
                down = string_cached[0]
                string_cached = string_cached[1:]
            string_cached = string_cached[1:]
            if string_cached[0] == '{':
                (up, string_cached) = object.bracket_balance(string_cached)
            else :
                up = string_cached[0]
                string_cached = string_cached[1:]
            content_and_symbol = re.search(r'(.*)d(\w+)',string_cached)
            content = content_and_symbol.group(1)
            symbol = content_and_symbol.group(2)
            #print(further_search.group(0))
            string_to_substitude = 'integrate(' + content + ', (' + symbol + ',' + down + ',' + up + '))'
            #print(string_to_substitude)
            object.origin = object.origin.replace(complete_int, string_to_substitude)
        else:  # \int
            further_search = re.search(r'\\int(.*)d(\w+)', complete_int)
            content = further_search.group(1)
            symbol = further_search.group(2)
            #print(further_search.group(0))
            string_to_substitude = 'integrate(' + content + ',' + symbol + ')'
            #print(string_to_substitude)
            #print(object.origin)
            object.origin = object.origin.replace(further_search.group(0), string_to_substitude)
        object_searched = re.search(r'\\int.*d\w+', object.origin)

