import unittest

def concatenate_strings(str1, str2):
    # Concatenates two strings
    return str1 + str2

class MyStringTestClass(unittest.TestCase):
    def test_concatenate_strings(self):
        # Checks if the concatenation of two strings is as expected
        result = concatenate_strings("Hello", "World")
        self.assertEqual(result, "HelloWorld", "Should be 'HelloWorld'")

if __name__ == '__main__':
    # Main module
    unittest.main()