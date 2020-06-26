import re
import random
def invalidstr(s):
    ok=0
    if len(s)<=1:
        return 1
    s= s.lower()
    for char in s:
        if ord(char) - ord('a')>=0 and ord(char) - ord('a') <26 :
            continue
        else:
            ok=1
            break
    if ok == 1:
            return 1
    return 0


def invalidint(num):
    if num=="":
        return 1
    try:
        val = float(num)
        return 0
    except ValueError:
        return 1

def invalid_account_number(num):
    if num=="":
        return 1
    if invalidint(num):
        return 1
    if len(num)<9 or len(num)>18:
        return 1
    return 0

def invalidifsc(ifsc):
    if ifsc=="":
        return 1
    corr = re.search("^[A-Z]{4}0[A-Z0-9]{6}$",ifsc)
    if(corr):
        return 0
    else:
        return 1

def invaliddate(date):
    if date=="":
        return 1
    dd,mm,yy=date.split('/')
    dd=int(dd)
    mm=int(mm)
    yy=int(yy)
    if(mm==1 or mm==3 or mm==5 or mm==7 or mm==8 or mm==10 or mm==12):
        max1=31
    elif(mm==4 or mm==6 or mm==9 or mm==11):
        max1=30
    elif(yy%4==0 and yy%100!=0 or yy%400==0):
        max1=29
    else:
        max1=28
    if(mm<1 or mm>12):
        return 1
    elif(dd<1 or dd>max1):
        return 1
    return 0

def check_supplies(dict):
    for suppliers_count in range(int(dict["number_of_suppliers"])):
        if invaliddate(dict["suppliers"][suppliers_count]["date"]) or invalidint(dict["suppliers"][suppliers_count]["receipt_number"]) or invalidstr(dict["suppliers"][suppliers_count]["supplier_name"]) or invalidstr(dict["suppliers"][suppliers_count]["particulars"]) or invalidint(dict["suppliers"][suppliers_count]["amount"]) or invalidint(dict["suppliers"][suppliers_count]["stock_register"]):
            return 0
        return 1

def check_pending_advance_database(a,b):
    return random.randint(0,1)

def check_correct_advance_info_database(a,b):
    return random.randint(0,1)

def update_database_1(a,b):
   # update_database_
   return 1


def update_database_2(a,b):
    #update_database_
    return 1

def validate_request(dict):
#missing info unit test
    if dict["type"] == "R":
        if dict["name"]=="" or dict["designation"]==""  or dict["file_number"]=="" or dict["purpose"]=="" or dict["amount"]=="" or dict["sanction_number"]=="" or dict["budget_available"]=="" or dict["account_holder_name"]=="" or dict["account_number"]=="" or dict["branch_name"]=="" or dict["ifsc_code"]=="" or dict["date"]=="" or ( dict["from"]!="1" and dict["from"]!="2" and dict["from"]!="3" ) or ( dict["head"]!="1" and dict["head"]!="2" and dict["head"]!="3" and dict["head"]!="4" and dict["head"]!="5" ):
          return 0
#invalid/incorrect info
        if invalidstr(dict["name"]) or invalidstr(dict["designation"]) or invalidint(dict["file_number"]) or invalidstr(dict["purpose"]) or invalidstr(dict["from_specify"]) or invalidstr(dict["head_specify"]) or invalidint(dict["amount"]) or invalidint(dict["sanction_number"]) or invalidint(dict["budget_available"]) or invalidstr(dict["account_holder_name"]) or invalid_account_number(dict["account_number"]) or invalidstr(dict["bank_name"]) or invalidstr(dict["branch_name"]) or invalidifsc(dict["ifsc_code"]) or invaliddate(dict["date"]) :
            return 0
        if(check_pending_advance_database(dict["name"],dict["designation"])):
            return 0
        update_database_1(dict["name"],dict["designation"])
        return 1

    elif dict["type"] == "S":
       if invalidstr(dict["name"]) or invalidstr(dict["designation"])or invalidint(dict["file_number"])or invalidstr(dict["purpose"]) or invalidstr(dict["head_specify"]) or invalidint(dict["sanction_number"]) or invalidint(dict["amount"]) or invaliddate(dict["date"]) or invalidint(dict["total_expenditure"]) or invalidint(dict["excess"]) or invalidint(dict["number_of_suppliers"]) or invaliddate(dict["date"]) :
           print("1$")
           return 0
       if dict["total"]!=float(dict["total_expenditure"]):
           print("2$")
           return 0
       if check_supplies(dict)==0:
           print("3$")
           return 0
       if check_correct_advance_info_database(dict["name"],dict["designation"]):
           return 0
       update_database_2(dict["name"],dict["designation"])
       return 1


#31834212565

#request = {"type":"R","name":"kp","designation":"student","file_number":"1","purpose":"stationary","from":"1","from_specify":"Initialised","head":"1","head_specify":"Initialised","amount":"120","sanction_number":"1","budget_available":"12","account_holder_name":"kp","account_number":"31834212565","bank_name":"SBI","branch_name":"BORINGROAD","ifsc_code":"SBIN0014892","date":"09/02/2000"}
#print(validate_request(request))

#SBIN0014892
