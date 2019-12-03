# Problem:- User will take the input in integer format and the output
# will be in string format
# for example input:- 1,output:-one . input:-123, output:-onetwothree

list_of_charnum=['zero','one','two','three','four','five','six','seven','eight','nine']

def check(n):
    return list_of_charnum[n]

try:
    a=int(input("Enter your number "))
    list1=list(str(a))
    for i in list1:
        print(check(int(i)),end="")
except:
    print("!!!!!!!!!!!!!!!! Something Went Wrong !!!!!!!!!!!!")
    print("------------Type in right format-----------")


