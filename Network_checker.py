mtn=['0','6',"3"]
glo =["5","7"]
airtel = ["2","1","4"]
etisalat = ["8","9"]

print("#"*60)
print("#"*60)
print("#"*16, "WELCOME TO NETWORK-CHECKER", "#"*16)
print("#"*16, "WELCOME TO NETWORK-CHECKER", "#"*16)
print("#"*60)
print("#"*60)
while True:
    Phone_no = str(input("Enter phone number: "))
    
    if len(Phone_no) > 11 or len(Phone_no) < 11:
        print("Invalid Phone no, Try again")
        
    elif Phone_no[3] in mtn:
        print("This number is MTN")
    elif Phone_no[3] in glo:
        print("This number is GLO")
    elif Phone_no[3] in airtel:
        print("This number is AIRTEL")
    elif Phone_no[3] in etisalat:
        print("This number is ETISALAT")

    else:
        print("please input number")
    print("#"*60)
    print("#"*16, "WELCOME TO NETWORK-CHECKER", "#"*16)
    print("#"*60)
    





