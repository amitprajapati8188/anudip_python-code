num1=221
num2=44
num3=51

if(num1>num2) and (num1>num3):
    greatest = num1
elif(num2>num3) and (num2>num1):
    greatest=num2
else:
    greatest=num3

print("The greatest no. is :", greatest)



if(num1>num2):
    if(num1>num3):
        print("Greatest no: ", num1)
    else:
        print("Greatest no:",num3)
else:
    if(num2>num3):
        print("Greatest no: ", num2)
    else:
        print("Greatest no:",num3)