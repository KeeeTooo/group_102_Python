# name="nikax"
# scores=[20,43,5,97,73]
# i=0

# for i in range(5):
#     print(str(name[i])+"-"+str(scores[i]))
# i+=1

#---------------------------------------------------------------

#ფუნქციონალური პროგრამირება

# def wish_a_good_day(name,day):
#     print(name+"karg dges gisurveb"+str(day))
# wish_a_good_day("keti",5)
#------------------------------------------------------------------

# def shekreba(num1,num2):
#     print(int(num1)+int(num2))
# shekreba(11,10)
#--------------------------------------------------------------
# def wish_a_good_day(name,day):
#  print(name+"karg dges gisurveb"+str(day))

# names=["keti","luka"]
# for char in names:
#     wish_a_good_day(char,5)
#-------------------------------------------------------------
# def pair_sum(list1,list2):
#     for i in range(min(len(list1),len(list2))):
#      print(list1[i]+list2[i])
# pair_sum([20,43,56,73,10,6,87,45,97],[11,55,23,1,10,6,87,45,79])
#-----------------------------------------------------------------



# def studentsF(students):

#  new_arr=[]
#  i=len(students)

#  while i>0:
#     new_arr.append(students[i-1])
#     i-=1
#  print(new_arr)

# studentsF(["nika","ana","mamuka","beqa", "dachi", "iva","farna"])
# #-----------------------------------------------------------------------
# def studentsF(students):

#  i=1
#  student_rev=[]
#  students=["nika","ana","mamuka","beqa", "dachi", "iva","farna"]
#  while i<=len(students):
#     for char in students:
#         student_rev.append(students[-i])
#         i+=1
#  print(student_rev)
# studentsF(["nika","ana","mamuka","beqa", "dachi", "iva","farna"])
#------------------------------------------------------------------------
def maxnumF(scores):
 max_num=scores[0]
 i=0
 while i<len(scores):
     if scores[i]>max_num:
         max_num=scores[i]
     i+=1
 print(max_num)
maxnumF=[20,43,56,73,10,6,87,45,97]


