# my_name="keti"
# my_surname="liparteliani"
# my_age=26
# my_sentence= "saxeli {2} gvari {0} asaki {1}".format (my_surname,my_age,my_name)
# my_sentence= "saxeli {} gvari {} asaki {}".format (my_name,my_surname,my_age)

# print(my_sentence)

#_____________________________________________

# my_name="keti"
# if "e" in my_name:
#  print("ki")
# else : 
#  print("ara")

#____________________________________________
    

# my_name=input("enter your name: ") 
# my_surname=input("enter your surname: ")
# my_age= int(input("enter your age : "))
# #print("chemi saxelia"+" "+my_name+" "+ "chemi gvaria" +" "+my_surname+" "+"chemi asakia"+" "+my_age)
# my_sentence= "chemi saxelia {} chemi gvaria {} chemi asakia {}".format (my_name,my_surname,my_age)
# print(my_sentence)
# my_age +=3
# print("after 3 years i am {} years old" .format(my_age))

#___________________________________________________

# ricxvi1=input("daweret pirveli ricxvi: ")
# ricxvi2=input("daweret meore ricxvi: ")

# my_sentence= int(ricxvi1) * int(ricxvi2)

# if int (my_sentence) >100:
#  print(my_sentence)
# else:
#  print("shen waage")

#______________________________________________________________
#print(20%6)    #20:6=3 da nashti 2 gamoitans 2
#______________________________________________________________
num1=int(input("enter num1 :"))
num2=int(input("enter num2 :"))
num3=int(input("enter num3 :"))


if num1%2 > 0:
    a = num1
else:
    a = 0
if num2%2 > 0:
    b = num2
else:
    b = 0

if num3%2 > 0:
    c = num3
else:
    c = 0

print( a+b+c)
