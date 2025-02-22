demostr = " Welcome to Topic on Strings"

count =0

for i in demostr:
    if(
         i=="A" or i=="a" or i=="E" or i=="e"
         or i=="I" or i=="i" or i=="O" or i=="o"
         or i=="U" or i=="u"

      ):
        count+=1

print("No of vowels in strings : ", count)