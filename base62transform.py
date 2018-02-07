import math
import unittest

BASE = 62
TINYURL_LEN = 6

def my_ord(char):
    """
    Get my order of character in {0-9},{A-Z},{a-z}.
    input type: char
    return type: int
    """
    assert(isinstance(char, str))
    if char.isdigit():
        return ord(char) - ord('0')
    elif 'A' <= char <= 'Z':    
        return ord(char) - ord('A') + 10    # 0-10
    elif 'a' <= char <= 'z':
        return ord(char) - ord('a') + 36    # 0-10, A-Z
    else:
        raise ValueError

def my_chr(number):
    """
    Get character of index in {0-9},{A-Z},{a-z}.
    input type: int
    return type: char
    """

    # input type check
    assert(isinstance(number, int))

    # number boundry check
    assert(0 <= number <= 61)

    return '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'[number]

def str_to_number(s, BASE=62):
    """
    Transform string to number.
    input type: str
    output type: int
    """
    assert(isinstance(s, str))
    res = 0
    for idx, ch in enumerate(reversed(s)):
        res += (my_ord(ch)) * int(math.pow(BASE, idx))
    return res

def number_to_str(number, BASE=62):
    """
    Transform number to string.
    input type: int
    output type: str
    """
    assert(isinstance(number, int))
    if number == 0:
        return '0'

    char_list = []  # last digit in front, need to reverse later
    while number:
        remainder = number % BASE
        char_list.append(my_chr(remainder))
        number /= BASE
    return ''.join(map(str,char_list[::-1]))

class MyTest(unittest.TestCase):
    '''
    testing for each functions
    '''
    def test_my_chr(self):
        self.assertEqual(my_chr(5), '5')
        self.assertEqual(my_chr(43), 'h')
        self.assertEqual(my_chr(61), 'z')

    def test_my_ord(self):
        self.assertEqual(my_ord('4'), 4)
        self.assertEqual(my_ord('A'), 10) # 10 - 1
        self.assertEqual(my_ord('a'), 36) # 10 + 26 - 1

    def test_str_to_number(self):
        self.assertEqual(str_to_number('zzzzzz'), BASE ** TINYURL_LEN - 1)

    def test_number_to_str(self):
        self.assertEqual(number_to_str(62**6-1), 'zzzzzz')
        self.assertEqual(number_to_str(0),       '0')

    def test_inverse_of_single_digit_and_char(self):
        for n in xrange(62):
            self.assertEqual(n, my_ord(my_chr(n)))

    def test_inverse_of_string_and_number(self):
        for n in xrange(5000):
            self.assertEqual(n, str_to_number(number_to_str(n)))

if __name__ == '__main__':
    unittest.main()
    # print number_to_str(62)
    # print str_to_number('10')
