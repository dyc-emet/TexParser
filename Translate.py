#! /usr/bin/python3.4

import re

from integrate import integrate
from partial import partial
from frac import frac
from convert_integer import convert_integer
from mul_integer_symbol import mul_integer_symbol

class TexInput:
    def __init__(self, origin):
        self.origin = origin
        self.set_of_tex = set(re.findall(r'\\[a-zA-Z]+', origin))

    def bracket_balance(self, string_to_search):
        result = ''
        main_bracket = string_to_search[0]
        bracket_dictionary = {'(' : ')', '[' : ']', '{' : '}'}
        bracket_list = []
        bracket_list.append(main_bracket)
        index = 1
        while bracket_list:
            if string_to_search[index] == bracket_dictionary[main_bracket]:
                bracket_list.pop()
                if bracket_list:
                    result += string_to_search[index]
            elif string_to_search[index] == main_bracket:
                    bracket_list.append(main_bracket)
                    result += main_bracket
            else :
                result += string_to_search[index]
            index += 1
        return (result, string_to_search[index:])
    
    def translate(self):
        order_of_function = ['\\frac', '\\int', '\\partial']  #The order is very important!, which still needs more consideration
        directory_of_function = {'\\frac' : frac, '\\int' : integrate, '\\partial' : partial}
        for function in order_of_function:
            if function in self.set_of_tex:
                directory_of_function[function](self)
        mul_integer_symbol(self)
        convert_integer(self)
        return self.origin
 
if __name__ == '__main__':
    #origin = input()
    origin = '\\frac{a + \\int^{2 Pi}_{0.2} \\int_{(a + 2) * 3}^4 x dy dx}{\\int^{2 * Pi}_0 theta dtheta} + \\frac{1}{2}'
    texinput = TexInput(origin)
    print(texinput.translate())
