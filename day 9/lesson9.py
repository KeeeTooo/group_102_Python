# def compare_scores(p1_score,p2_score):
#     if p1_score>p2_score:
#         print("{}  metia  {}-ze,{} qulit".format(p1_score,p2_score,p1_score-p2_score))
#     else:
#         print("{}  metia  {}- ze, {}  qulit".format(p2_score,p1_score,p2_score-p1_score))


# compare_scores(11,5)
#---------------------------------------------------------------------------------


# def multiply(a,b):
#  return (a*b)

#  print(multiply(10,20))


# def even_or_odd(number):
#  if number %2==0 :
#   print("Even")
#  else:
#     print("Odd")
#---------------------------------------------------------------------------------

# def reverse_arr(list):
 
#  i=len(list)
#  list1=[]
#  while i>0:
#      list1.append(list[i-1])
#      i-=1
#  print (list1)
#---------------------------------------------------------------------------------
# def scores_comp(score1,score2):
#  if score1>score2 :
#   print("{} >{} ,{} qulit".format(score1,score2,score1-score2))
#  elif score2>score1 :
#   print("{} >{} ,{} qulit".format(score2,score1,score2-score1))

#---------------------------------------------------------------------------------

#  student_rev=[]
#  students=["nika","ana","mamuka","beqa", "dachi", "iva","farna"]
#  while i<=len(students):
#     for char in students:
#         student_rev.append(students[-i])
#         i+=1
#  print(student_rev)
# studentsF(["nika","ana","mamuka","beqa", "dachi", "iva","farna"])

#---------------------------------------------------------------------------------

# mytxt=("ketevan")
# i=0
# while i>-len(mytxt):
#  print (mytxt[i-1])
#  i-=1
#---------------------------------------------------------------------------------

def positive_sum(arr):
    arr1 = 0
    for i in arr:
        if i > 0:
            arr1 = arr1 + i
    
    return arr1