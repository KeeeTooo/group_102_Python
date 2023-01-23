


#კვადრატული ფრჩხილით შექმნილი კოლექცია არის List

#my_arr=["banana",11,True,10.5,[1,2,3],1,4]

#print(my_arr[-1])
#print(my_arr[1:3])
#print(my_arr[1:6:2])
#print(my_arr[:4])

# menu=["xinkali","mwvadi","lobiani","qababi","wyali"]
# if "lobiani" in menu:
#     print("lobiani gvaqvs")
#----------------------------------------

# menu[1]="BBQ"
# print(menu)
#_______________________________________
# menu[2:4]=["aa","bb","cc"]
# print(menu)
#---------------------------------------
# my_name="nikusha"
# new_name=""
# for i in range(len(my_name)):
#     if i==2 or i==3:
#         new_name+="x"
#     else:
#         new_name+=my_name[i]

# print(new_name)
#-------------------------------------------
# my_name="nikusha"
# print(my_name.replace("ku","qq"))
#რიფლეისი მარტო ასეთ დროს გამოიყენება, ისე პრობლემებს 
# ქმნის ხოლმე და სჯობს ახალი ცვლადის შექმნა და იქ გადატანა ახალი ინფორმაციის

#-------------------------------------

# menu=["xinkali","mwvadi","lobiani","qababi","wyali"]
# menu.insert(3,"nayini")
# print(menu)
#---------------------------------
# menu=["xinkali","mwvadi","lobiani","qababi","wyali"]
# menu.append("cecxli")
# print(menu)
#------------------------------------------------

#მომხმარებელს შემოატანინეთ 5 საჭმელი, სიაში ჩაამატეთ ის რომლებიც შეიცავენ 2 ა-ს

# menu=[]

# for i in range(5):
#     food=input("your food")
#     if food.count("a")>=2:
#      menu.append(food)
# print(menu)


#მეორე გზა 
# menu=[]

# for i in range(5):
#     food=input("your food")
#     amount_of_a=0
#     for char in food:
#         if char=="a":
#             amount_of_a+=1
#     if amount_of_a>=2:
#         menu.append(food)
#         amount_of_a==0
# print(menu)

#----------------------------------------------------

# menu=["xinkali","mwvadi","lobiani","qababi","wyali"]
# menu.remove("wyali")   თუ მინდა მეორე პოზიცია წავშალო, ანუ მივუთითო რიგითობა და არა მნიშვნელობა del menu[2]
# print(menu)
#-------------------------------------------------------
#წაშალეთ ის ელემენტებში რომლებსიც მეორე ასო არის a
# menu=["xinkali","mwvadi","lobiani","qababi","wyali"]
# new_menu=[]
# for i in menu:
#     if i[2]=="a":
#        new_menu.append(i)
# print(new_menu)

#____________________________________________________
# scores=[20,43,56,73,10,6,87,45,97]
# scores.sort()
# print(scores)
# scores.sort(reverse=True)
# print(scores)
#__________________________________________________________
#დავალება

 # sort მეთოდის და max  ფუნქციის გამოყენების გარეშე დამიბრუნეთ ყველაზე დიდი რიცხვი 
 # (while ციკლით სათითაოდ შეამოწმეთ ელემენტი და მის მარჯვნივ მდგომი.
# რომელიც უფრო დიდი იქნება დროებით მიანიჭეთ მაქსიმუმის მნიშვნელობა და შემდეგ შეადარეთ 
# მის მარჯვნივ მდგომს  )

#scores=[20,43,56,73,10,6,87,45,97]



#1  გზა
# scores=[20,43,56,73,10,6,87,45,97]

# print(max(scores))

#2 გზა
# scores=[20,43,56,73,10,6,87,45,97]
# scores.sort()
# print(scores[-1])

#3 გზა
# scores=[20,43,56,73,10,6,87,45,97]
# max_num=scores[0]
# for score in scores:
#     if score>max_num:
#         max_num=score
# print(max_num)

#4 გზა
# scores=[20,43,56,73,10,6,87,45,97]
# max_num=scores[0]
# i=0
# while i<len(scores):
#     if scores[i]>max_num:
#         max_num=scores[i]
#     i+=1
# print(max_num)

#შეატრიალეთ #students=["nika","ana","mamuka","beqa", "dachi", "iva","farna"] სია sort და reverse გარეშე

# i=1
# student_rev=[]
# students=["nika","ana","mamuka","beqa", "dachi", "iva","farna"]
# while i<=len(students):
#     for char in students:
#         student_rev.append(students[-i])
#         i+=1
# print(student_rev)

#2 გზა
# students=["nika","ana","mamuka","beqa", "dachi", "iva","farna"]
# new_arr=[]
# i=len(students)

# while i>0:
#     new_arr.append(students[i-1])
#     i-=1
# print(new_arr)