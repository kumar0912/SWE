from request_form import request_form
from settle_form import settle_form
from validate_request import validate_request

def generate_request():
    form_type = input("Whats the form type" + "\n"+ "Enter :"+ "\n1: Request Advance"+"\n2: Settle Advance")
    if form_type == "1":
        request = request_form()
    elif form_type == "2":
        request = settle_form()
    return request
