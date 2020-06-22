from request_form import request_form
from settle_form import settle_form
from validate_request import validate_request

form_type = input("Whats the form type" + "\n"+ "Enter :"+ "\n1: Request Advance"+"\n2: Settle Advance")
print(form_type)
if form_type == "1":
    print("abc")
    request = request_form()
    print(request)
elif form_type == "2":
    request = settle_form()
    print(request)
validate_request(request)
