# num1=int(input("enter num1 :" ))
# num2=int(input("enter num2 :" ))
# num3=int(input("enter num3 :" ))

# #შევქმნათ საინკრემენტაციო ცვლადი

# my_sum=0

# #13,10,7
# if num1 % 2==1:
#     my_sum+=num1
# if num2 % 2==1:
#     my_sum+=num2
# if num3 % 2==1:
#     my_sum+=num3

# print("the sum of odd numbers is {}".format(my_sum))



#__________________________________________________

# my_name="ketevan"
# for char in my_name:
#     print(char)
#__________________________________________________
# name1=input("name")
# name2=input("name")
# #შევქმნათ ორი საინკრემენტაციო ცვლადი
# amount_of_vowels_in_name1=0
# amount_of_vowels_in_name2=0

# for char in name1:
#     if char in "aeiou":
#         amount_of_vowels_in_name1+=1

# for char in name2:
#     if char in "aeiou":
#         amount_of_vowels_in_name2+=1

# if amount_of_vowels_in_name1>amount_of_vowels_in_name2:
#     print ("amount of vowels in name1 is more and it contains {} vowels".format(amount_of_vowels_in_name1) )
# elif amount_of_vowels_in_name1<amount_of_vowels_in_name2:
#     print ("amount of vowels in name2 is more and it contains {} vowels".format(amount_of_vowels_in_name2) )
# else :
#     print ("tolia")

#_______________________________________________________________________________________

# # my_sentence=input("შეიყვანეთ წინადადება")
# # Symbol_a=0

# # for char in my_sentence:
# #     if char == "a":
# #        Symbol_a+=1
# # print(Symbol_a)


# ** ახარისხება   5**2=25
# // რამდენჯერ შედის ერთი რიცხვი მეორეში 10//3=3
# 25**(1/2)   ფესვი 25 დან 



# a=float(0.1*(2**30))
# b=100000.0

# if a>b:
#     print("აირჩიე ვარიანტი a")
# else:
#     print("აირჩიე ვარიანტი b")
#    print("spam"*3)



#მომხმარებელს შემოატანინეთ ორი სახელი და ის დაპრინტეთ რომელშიც მეტი თანხმოვანია

name1=input("enter your name1")
name2=input("enter your name2")


consonant_value_name1=0
consonant_value_name2=0

for char in name1:
    if char not in "aeiou":
        consonant_value_name1+=1
for char in name2:
     if char not in "aeiou":
        consonant_value_name2+=1

if consonant_value_name1>consonant_value_name2:
    print ("amount of consonant in name 1 is more and it contains {}".format(consonant_value_name1) )
else:
     print ("amount of consonant in name 2 is more and it contains {}".format(consonant_value_name2) )