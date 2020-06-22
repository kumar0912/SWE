import unittest
from validate_request import validate_request
from form_type import generate_request
class RequestTestCase(unittest.TestCase):

    #testing if any field is empty
    def test_missing_info(self):
        request = generate_request()
        result = validate_request(request)
        self.assertEqual(result,0)
    #testing if any field is incorrectly filled
    def incorrect_info(self):
        request = generate_request()
        result = validate_request(request)
        self.assertEqual(result,0)


class SettleTestCase(unittest.TestCase):

    #testing if any field is empty
    def test_missing_info(self):
        request = generate_request()
        result = validate_request(request)
        self.assertEqual(result,0)

    #testing if any field is incorrectly filled
    def incorrect_info(self):
        request = generate_request()
        result = validate_request(request)
        self.assertEqual(result,0)
    

if __name__ == '__main__':
    unittest.main()
