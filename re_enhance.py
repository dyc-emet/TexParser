import re

def bracket_balance(string_to_search):
    #print(string_to_search)
    result = ''
    main_bracket = string_to_search[0]
    bracket_dictionary = {'(' : ')', '[' : ']', '{' : '}'}
    bracket_list = []
    bracket_list.append(main_bracket)
    index = 1
    result += main_bracket
    while bracket_list:
        if string_to_search[index] == bracket_dictionary[main_bracket]:
            bracket_list.pop()
            #if bracket_list:
                #result += string_to_search[index]
        elif string_to_search[index] == main_bracket:
                bracket_list.append(main_bracket)
                #result += main_bracket
        #else :
            #result += string_to_search[index]
        result += string_to_search[index]
        index += 1
    return (result, string_to_search[index:])

def transform_origin_to_regx(string):
    #print(string)
    list_of_extraordinary = ['(', ')', '[', ']', '{', '}', '*', '.']
    for element in list_of_extraordinary:
        string = string.replace(element, '\\' + element)
    return string
        
def re_bracket_balance(pattern, string):
    bracket_list = ['(', '[', '{']
    balance_need_searched = re.search(r'\(\.\.\.\)', pattern)
    while balance_need_searched:
        pattern_origin = pattern
        string_to_change_pattern = string
        begin_of_balance_in_pattern = balance_need_searched.span()[0]
        end_of_balance_in_pattern = balance_need_searched.span()[1]
        #print(balance_need_searched.group(0))
        #print(begin_of_balance_in_pattern)
        #print(end_of_balance_in_pattern)
        string_before_balance_in_pattern = pattern[:begin_of_balance_in_pattern]
        string_searched = re.search(string_before_balance_in_pattern, string_to_change_pattern)
        while string_searched:
            begin_of_balance_in_string = string_searched.span()[1]
            if string_to_change_pattern[begin_of_balance_in_string] in bracket_list:
                result, string_after_balance_in_string = bracket_balance(string[begin_of_balance_in_string:])
                #print(result)
                #end_of_balance_in_string = begin_of_balance_in_string + len(result)
                result = transform_origin_to_regx(result)
                #print(result)
                pattern = pattern[:begin_of_balance_in_pattern] + result + pattern[end_of_balance_in_pattern:]
                #print(pattern)
                break
            else:
                string_to_change_pattern = string_to_change_pattern[begin_of_balance_in_string:]
                string_searched = re.search(string_before_balance_in_pattern, string_to_change_pattern)
        #print(pattern)
        if pattern == pattern_origin:
            return None
        balance_need_searched = re.search(r'\(\.\.\.\)', pattern)
    #print(pattern)
    #print(string)
    return re.search(pattern, string)

def one_or_bracket(pattern, string):
    bracket_list = ['(', '[', '{']
    balance_need_searched = re.search(r'\(\.\.\.\)', pattern)
    while balance_need_searched:
        pattern_origin = pattern
        string_to_change_pattern = string
        begin_of_balance_in_pattern = balance_need_searched.span()[0]
        end_of_balance_in_pattern = balance_need_searched.span()[1]
        #print(balance_need_searched.group(0))
        #print(begin_of_balance_in_pattern)
        #print(end_of_balance_in_pattern)
        string_before_balance_in_pattern = pattern[:begin_of_balance_in_pattern]
        string_searched = re.search(string_before_balance_in_pattern, string_to_change_pattern)
        while string_searched:
            begin_of_balance_in_string = string_searched.span()[1]
            if string_to_change_pattern[begin_of_balance_in_string] in bracket_list:
                result, string_after_balance_in_string = bracket_balance(string[begin_of_balance_in_string:])
                #print(result)
                #end_of_balance_in_string = begin_of_balance_in_string + len(result)
                result = transform_origin_to_regx(result)
                #print(result)
                pattern = pattern[:begin_of_balance_in_pattern] + result + pattern[end_of_balance_in_pattern:]
                #print(pattern)
                break
            elif string_to_change_pattern[begin_of_balance_in_string] == ' ':
                one_pattern_string = string_to_change_pattern[begin_of_balance_in_string:]
                one_pattern_matched = re.match(r' [a-zA-Z0-9]+ *', one_pattern_string)
                if one_pattern_matched:
                    result = one_pattern_matched.group(0)
                    pattern = pattern[:begin_of_balance_in_pattern] + result + pattern[end_of_balance_in_pattern:]
                    break
            else:
                string_to_change_pattern = string_to_change_pattern[begin_of_balance_in_string:]
                string_searched = re.search(string_before_balance_in_pattern, string_to_change_pattern)
        #print(pattern)
        if pattern == pattern_origin:
            return None
        balance_need_searched = re.search(r'\(\.\.\.\)', pattern)
    #print(pattern)
    #print(string)
    return re.search(pattern, string)

if __name__ == '__main__':
    line = '\\partial^{2.3} x / \\partial x^{2}'
    line_searched = re_bracket_balance(r'\\partial\^(...).*?/ \\partial', line)
    line_one_searched = one_or_bracket(r'\\partial\^(...)(...)/ \\partial(...)', line)
    if line_searched:
        print(line_searched.group(0))
    if line_one_searched:
        print(line_one_searched.group(0))