import unittest
from base62transform import number_to_str, str_to_number, my_ord, my_chr

TINYURL_LEN = 6

def generate_hash_code(url, tinyurl_length=TINYURL_LEN):
    """Generate hashcode using Horner's method and mod by MAX_RANGE of our url shortener service.
    
    Ex:
    s = "call"
    hashcode = s.generate_hash_code()
             = 99 * 31^3 + 97 * 31^2 + 108 * 31^1 + 108 * 31^0 
             = 108 + 31 * (108 + 31 * (97 + 31 * (99)))
             = 3045982
    return hashcode % 62**6

    Since 62**5 is almost 1 billion, collision rate would be very low.
    """

    # strip protocal titles
    clean_url = url.lstrip('http://').lstrip('https://').lstrip('ftp://')
    hash = 0
    for ch in clean_url:
        hash = ord(ch) + (31 * hash)

    return int(hash % (62 ** 5))

class MyTest(unittest.TestCase):
    '''
    testing for each functions
    '''
    urls = ['http://google.com',
            'https://abc.com',
            'http://zh-google-styleguide.readthedocs.io/en/latest/google-python-styleguide/python_style_rules/#comments'
            ]
    def test_generate_hash_code(self):
        for url in self.urls:
            self.assertTrue(0 <= generate_hash_code(url) <= 62 ** TINYURL_LEN - 1)

if __name__ == '__main__':
    # print number_to_str(62**6 - 1)
    unittest.main()
