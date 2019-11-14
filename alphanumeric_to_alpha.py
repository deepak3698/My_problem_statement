'''

Question- you have been given a alphanumeric string , and what you have to do that you have to convert that

into alpha format.

for example-
input:- 2h3k4p

output:- HHKKKPPPP


'''
string1=input("Enter Your String :")
sum1=""
sum2=0
for i in string1:
    try:
        if(i.isalpha()):
            if(sum2==0):
                sum2=1
            sum1=sum1+(sum2*i.upper())
            sum2=0
        else:
            sum2=int(str(sum2)+str(i))
    except:
        pass
print(f"The Format in which you  want to print is : {sum1}")




