def request_form():
    dict={}
    dict["type"]="R"
    dict["name"]=input("Your Name:")
    dict["designation"]=input("Your Designation:")
    dict["file_number"]=input("Personal File Number:")
    dict["purpose"] = input("Purpose of advance: ")
    dict["from"]=input("Advance Required From:"+"\n1.Institute Budget"+"\n2.Department Budget"+"\n3.Other:")
    dict["from_specify"]="Initialised"
    if dict["from"]=="3":
        dict["from_specify"] = input("Please Specify: ")
    dict["head"] = input("Head of expenditure"+ "\n1.Contingency"+"\n2.Consumable"+"\n3.Non Consumable"+"\n4. CPDA"+"\n5. Other:")
    dict["head_specify"]="Initialised"
    if dict["head"]=="5":
        dict["head_specify"] = input("Please Specify: ")
    dict["amount"] = input("Enter Amount of advance:")
    dict["sanction_number"] = input("Enter Financial Sanction Number")
    dict["budget_available"]=input("Enter Budget Available: ")
    print("Bank Details for Fund Transfer: ")
    dict["account_holder_name"]=input("Name of Account Holder: ")
    dict["account_number"] = input("Account no:")
    dict["bank_name"] = input("Bank Name:")
    dict["branch_name"] = input("Branch Name:")
    dict["ifsc_code"] = input("IFSC Code:")
    dict["date"] = input("Enter Date(format = dd/mm/yy): ")
    return dict
