# find how many vowels & consonant  in a sring  with their char value and number of char value

vowels=['a','e','i','o','u']
var1=input("Enter your String or character !")

no_of_vowels=0
no_of_cons=0

char_of_vowels=""
char_of_cons=""

for i in var1:
    if i.lower() in vowels:
        char_of_vowels=char_of_vowels+i
        no_of_vowels=no_of_vowels+1
    else:
        if(i==" "):
            continue
        char_of_cons=char_of_cons+i
        no_of_cons=no_of_cons+1

print(f"You have {no_of_vowels} vowels in your string that is {char_of_vowels} ")
print(f"You have {no_of_cons} vowels in your string that is {char_of_cons} ")



