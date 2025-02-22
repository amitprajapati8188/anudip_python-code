str = "App dev using pyhton !! 2025"
print("my string:",str)

upr,lwr,num,spl = 0,0,0,0

for i in range(len(str)):
    if str[i]>='A' and str[i]<='Z':
        upr+=1
    elif str[i]>='a' and str[i]<='z':
        lwr+=1
    elif str[i]>='0' and str[i]<='9':
        num+=1
    else:
        spl+=1


print("Uppercase letters : ",upr)
print("Lowercase letters : ",lwr)
print("Numbers : ",num)
print("Special chacters ",spl)