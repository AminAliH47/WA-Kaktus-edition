import unittest
from main import Handler

obj = Handler()

class TestHandlerFunctions(unittest.TestCase):

    def test_url_checker(self):
        
        self.assertTrue(obj.url_handler("https://www.google.com"))
        self.assertFalse(obj.url_handler("https;//www.google.com"))
        self.assertTrue(obj.url_handler("google.com"))
        self.assertTrue(obj.url_handler("www.google.com"))
        
    def test_url_protocol(self):
        self.assertEqual("https", obj.check_protocol("https://www.google.com"))
        self.assertEqual("http", obj.check_protocol("http://www.google.com"))
        
if __name__ == '__main__':
    unittest.main()