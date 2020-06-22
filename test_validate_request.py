import unittest
from validate_request import validate_request

class RequestTestCase(unittest.TestCase):
#left is just to make the request objects and rest is done
    def test_missing_info(self):
        result = validate_request(request)
        self.assertEqual(result,0)
    def incorrect_info(self):
        result = validate_request(request)
        self.assertEqual(result,0)

class SettleTestCase(unittest.TestCase):
#left is just to make the request objects and rest is done
    def test_missing_info(self):
        result = validate_request(request)
        self.assertEqual(result,0)
    def incorrect_info(self):
        result = validate_request(request)
        self.assertEqual(result,0)


if __name__ == '__main__':
    unittest.main()
