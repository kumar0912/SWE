import unittest
from validate_request import validate_request
from form_type import generate_request
class RequestTestCase(unittest.TestCase):

    request = {"type":"R","name":"kp","designation":"student","file_number":"1","purpose":"stationary","from":"1","from_specify":"Initialised","head":"1","head_specify":"Initialised","amount":"120","sanction_number":"1","budget_available":"12","account_holder_name":"kp","account_number":"31834212565","bank_name":"SBI","branch_name":"BORINGROAD","ifsc_code":"SBIN0014892","date":"09/02/2000"}

    #testing if any field is incorrectly filled
    def test_incorrect_info(self):
        #request = generate_request()
        request = {"type":"R","name":"kp","designation":"1","file_number":"1","purpose":"stationary","from":"1","from_specify":"Initialised","head":"1","head_specify":"Initialised","amount":"120","sanction_number":"1","budget_available":"12","account_holder_name":"kp","account_number":"31834212565","bank_name":"SBI","branch_name":"BORINGROAD","ifsc_code":"SBIN0014892","date":"09/02/2000"}

        result = validate_request(request)
        self.assertEqual(result,0)

    #testing if any field is empty
    def test_missing_info(self):
        #request = generate_request()
        request = {"type":"R","name":"","designation":"student","file_number":"1","purpose":"stationary","from":"1","from_specify":"Initialised","head":"1","head_specify":"Initialised","amount":"120","sanction_number":"1","budget_available":"12","account_holder_name":"kp","account_number":"31834212565","bank_name":"SBI","branch_name":"BORINGROAD","ifsc_code":"SBIN0014892","date":"09/02/2000"}

        result = validate_request(request)
        self.assertEqual(result,0)

    def test_correct_info(self):
        #request = generate_request()
        request = {"type":"R","name":"kp","designation":"student","file_number":"1","purpose":"stationary","from":"1","from_specify":"Initialised","head":"1","head_specify":"Initialised","amount":"120","sanction_number":"1","budget_available":"12","account_holder_name":"kp","account_number":"31834212565","bank_name":"SBI","branch_name":"BORINGROAD","ifsc_code":"SBIN0014892","date":"09/02/2000"}

        result = validate_request(request)
        print(result,"%")
        self.assertEqual(result,1)


class SettleTestCase(unittest.TestCase):

    request = {"type":"S","name":"kp","designation":"student","file_number":"1","purpose":"stationary","head":"1","head_specify":"Initialised","sanction_number":"1","amount":"120","date":"12/02/2000","total_expenditure":"120","excess":"0","number_of_suppliers":"1","total":0,"suppliers":[{"date":"12/02/1999","receipt_number":"1","supplier_name":"KHAITAN","particulars":"pen","amount":"120","stock_register":"1"}],"date":"09/02/2000"}
    #testing if any field is empty
    
    def test_missing_info(self):
        #request = generate_request()
        request = {"type":"S","name":"","designation":"student","file_number":"1","purpose":"stationary","head":"1","head_specify":"Initialised","sanction_number":"1","amount":"120","date":"12/02/2000","total_expenditure":"120","excess":"0","number_of_suppliers":"1","total":0,"suppliers":[{"date":"12/02/1999","receipt_number":"1","supplier_name":"KHAITAN","particulars":"pen","amount":"120","stock_register":"1"}],"date":"09/02/2000"}
        result = validate_request(request)
        self.assertEqual(result,0)

    #testing if any field is incorrectly filled
    def test_incorrect_info(self):
        #request = generate_request()
        request = {"type":"S","name":"1","designation":"student","file_number":"1","purpose":"stationary","head":"1","head_specify":"Initialised","sanction_number":"1","amount":"120","date":"12/02/2000","total_expenditure":"120","excess":"0","number_of_suppliers":"1","total":0,"suppliers":[{"date":"12/02/1999","receipt_number":"1","supplier_name":"KHAITAN","particulars":"pen","amount":"120","stock_register":"1"}],"date":"09/02/2000"}
        result = validate_request(request)
        self.assertEqual(result,0)

    def test_correct_info(self):
        #request = generate_request()
        request = {"type":"S","name":"kp","designation":"student","file_number":"1","purpose":"stationary","head":"1","head_specify":"Initialised","sanction_number":"1","amount":"120","date":"12/02/2000","total_expenditure":"120","excess":"0","number_of_suppliers":"1","total":120,"suppliers":[{"date":"12/02/1999","receipt_number":"1","supplier_name":"KHAITAN","particulars":"pen","amount":"120","stock_register":"1"}],"date":"09/02/2000"}
        result = validate_request(request)
        self.assertEqual(result,1)


if __name__ == '__main__':
    unittest.main()
