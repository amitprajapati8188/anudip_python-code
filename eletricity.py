print("1.household purpose\n2.Small Business purpose \n3.Industrial purpose :")
user_type=int(input("Enter the option:"))
e_unit=int(input("Consumption unit in a month:"))
print("Eletricity bill...")
if(user_type==1):
    bill=(2*e_unit)
    print("your bill is:",bill)
elif(user_type==2):
    bill=(5*e_unit)
    print("your bill is:",bill)
elif(user_type==3):
    bill=(10*e_unit)
    print("your bill is:",bill)
