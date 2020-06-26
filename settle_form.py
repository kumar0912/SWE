def settle_form():
    dict={}
    dict["type"]="S"
    dict["name"]=input("Your Name:")
    dict["designation"]=input("Your Designation:")
    dict["file_number"]=input("Personal File Number:")
    dict["purpose"] = input("Purpose of advance: ")
    dict["head"] = input("Head of expenditure"+ "\n1.Contingency"+"\n2.Consumable"+"\n3.Non Consumable"+"\n4. CPDA"+"\n5. Other:")
    dict["head_specify"]="Initialised"
    if dict["head"]=="5":
        dict["head_specify"] = input("Please Specify: ")
    dict["sanction_number"] = input("Enter Financial Sanction Number")
    dict["amount"] = input("Enter Amount of advance:")
    dict["date"] = input("Enter Date of advance taken(format = dd/mm/yy): ")
    dict["total_expenditure"] = input("Enter Total expenditure: ")
    dict["excess"] = input("Excess amount claimed/Balance deposited(+/-):")
    dict["number_of_suppliers"]=input("Enter number of suppliers: ")
    dict["suppliers"]=[]
    dict["total"]=0
    for suppliers in range(int(dict["number_of_suppliers"])):
        detail={}
        print("Enter details of supplier %d :" % (suppliers+1))
        detail["date"]=input("Date(format = dd/mm/yy): ")
        detail["receipt_number"] = input("Cash Memo/Receipt Number: ")
        detail["supplier_name"] = input("Supplier's Name: ")
        detail["particulars"] = input("Particulars: ")
        detail["amount"] = input("Amount: ")
        dict["total"]+=float(detail["amount"])
        detail["stock_register"] = input("Stock Register: ")
        dict["suppliers"].append(detail)
    dict["date"] = input("Today's Date(format = dd/mm/yy): ")
    return dict
