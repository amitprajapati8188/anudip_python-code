'''def div(x,y):
    print(x/y)

a = int(input("Enter the the first number:"))
b = int(input("Enter the the second number:"))

div(a,b)

c=int(input("Enter a number"))
d=int(input("Enter another number"))

div(c,d)

def square(first):
    print(first*first)

demo=int(input("Enter a number"))
square(demo)                            #function call    

def cube(second):
    print(second*second*second)

demo1 = int(input("Enter a number"))
cube(demo1)                             #function call


print("Maximum of 4,12,43,19 and 100  is : ",end="")
print(max(4,12,43,19,100))

print("Minimum of 4,12,43,19 and 100  is : ",end="")
print(min(4,12,43,19,100))

def fact(x):
    result=1
    for y in range(1,x+1):
        result=result*y
    print(result)

num1=int(input("Enter a number:"))

fact(num1)'''

num=int(input("Enter a number to reverse"))
temp = num
reverse =0

# 234-->   4--> seperate --> 100  3--> seperate--> 10  --> seperate 2--> 1

while(num>0):
    digit = num%10              #4,  3  , 2234
    reverse=(reverse*10)+digit    #  reverse-->432
    num=int(num/10)
print(reverse)

if(reverse==temp):
    print("Palindrome number")
else:
    print("Not a palindrome number")