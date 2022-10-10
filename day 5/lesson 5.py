#1)for loop ფორ ციკლი
#2)while loop ვაილ ციკლი
#______________________________


# for loop 

# i არის საიტერაციო ცვლადი
# for i in range (7):     #for ციკლი ჩატარდეს 7 ჯერ   range(7)= 0,1,2,3,4,5,6
#     print ("ketevan")

# for i in range(3,6) :    #3 დან 6 მდე ანუ range მიიღებს მნიშვნელობებს 3,4,5 და დაიპრინტება სამჯერ
#  print ("ketevan")

# for i in range (2,10,2):    #2 დან 10 მდე ყოველი მეორე ანუ 2,4,6,8
#     print(i,"ketevan")

#_______________________________________________________

#while loop
# full_name="ketevan liparteliani"

# i=0   # საიტერაციო ცვლადი 
# while i<len(full_name) : # while-სანამ . სანამ i ნაკლებია რაღაც რიცხვზე, იმდენჯერ დაპრინტე სახელი
#     print("ketevan")
# i+=1                     #უსასრულოდ როარ გაგრძელდეს ციკლი ვუდგენ ზედა ზღვარს, ანუ სახელის სიგრძე რადგან 20 ია მიაღწიოს ამ ოცს და მაგჰდენჯერ დაწეროს

# იგივე ოღონდ სიმბოლოებად:
# full_name="ketevan liparteliani"
# i=0
# while i<len(full_name):
#     print(full_name[i])
#     i+=1




# # a="qwerty"
# b="asdfgh"

# i=0

# while i<len(a) :
#     print(a[i]+b[i])
#     i+=1

# i=0
# while i<10: 
#  print(i)                         #while ფუნქციის დამუხრუჭება რაიმე მნიშვნელობამდე
#  i+=1
#  if i ==5:
#    break




# letters = ["a", "b", "c"]               #დაემატოს ჩამონათვალში რაიმე ინფორმაცია ბოლოში
# letters.append("d")
# print(len(letters))

# nums = [9, 8, 7, 6, 5]
# nums.append(4)
# nums.insert(2, 11)                          #დაამატოს მესამე პოზიციაზე 11
# print(nums)

# i = 3
# while i>=0:
#    print(i)
#    i = i - 1

# i = 5
# while True:
#   print(i)
#   i = i - 1
#   if i <= 2:
#     break

# list=[3,4,9, 8, 7, 6, 5]
# for x in list:
#    if(x%2==1 and x>4):
#       print(x)
#       break

# nums = list(range(3, 15, 3))
# print(nums[2])


# i=5
# while i<20 :
#    print(i)
#    i+=1
#    if i==10:
#       continue  ketevan



name=input("enter your name")
i=0
for char in name:
   i+=1
   if char in "aeiou":
      print(i,char)

