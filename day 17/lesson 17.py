# #my_students={"luka":18,
#              "nika":24,
#              "mzia":48,
#              "shako":[56,15]}
#              #kay:value
             
# print (my_students["nika"])

# # my_dict={0:"a",
# #          1:"b",
# #          5:"h"}

# # print(my_dict[5])

# my_students["erekle"]:50
# print(my_students)

# my_students["nika"]=5   #update
# print(my_students)


#print(my_students.get("mzia"))   #გამომიტანე მზიას მნიშვნელობა
#print(list(my_students.items()))  #გამომიტანე სიად ცხრილის კომპონენტების წყვილები
#print(list(my_students.items())[0][1]) #ლისტად გადაქცეულში 0,1 პოზიცია გამომიტანე
#print(my_students.keys())
# print(my_students.values())
#my_students.pop("shako")               #სიიდან ამომიშალე shako და მისი value
# print(my_students)

# list=[[1,1],[2,3],[5,8,2]]
# print(list[list[2][list[1][0]]])


# def rps(p1, p2):
#     winner_combo={"rock":"scissors",
#                   "scissors":"paper",
#                    "paper":"rock",}
#     if winner_combo[p1]==p2:
#         return "Player 1 won!"
#     if winner_combo[p2]==p1:
#         return "Player 2 won!"
#     return "Draw!"

# arr=[3,11,5,15,2]
# print(sum(sorted(arr)[1:-1]))

# c=range(1,10,3)
# print(c[0])
# print (list(c))


# x=["a","b","c","d"]  
# y=["keti","kristi","ana","eli"]
# z=["1","2","3","4"]

# v=zip(x,y,z)
# print(list(v))


# arr=(i for i in range(10))
# print (list(arr))

# arr=[i for i in range(10)]
# print (arr)


# x=["a","b","c","d"]  
# y=["keti","kristi","ana","eli"]
# z=["1","2","3","4"]

# c=(x,y,z)

# for i in range(min(len(x),len(y),len(z))):
#     print(x[i]+y[i]+z[i])




# def set_alarm(employed, vacation):
#     if employed and not vacation:
#         return False
#     else:
#         return True


# print(set_alarm(True, False))

# a="shavi datva"
# b="shishxina"


# c=[]
# d=[]

# for i in a.split():
#     c.append(i)

# for j in b.split():
#     d.append(j)

# if c[0][0] == d[0][0] and c[-1][-1]==d[-1][-1]:
#     print ("T")
# else:
#     print (False)


# arr=[1,2,3,4,6,7,8]
# a=[]

# for i in range(len(arr)-1):
#  if arr[i]+1 != arr[i+1]:
#     a.append(arr[i+1])
#  else:
#     continue
# if len(a)>0:
#     print(a[0])
# else :
#     print(None)



my_list = ['Hello', 'Goodbye', 'Hello Again','ketevan']
del(my_list[1::2])
print(my_list)

my_list = ['Hello', 'Goodbye', 'Hello Again','ketevan']
print(my_list[::2])

my_list = ['Hello', 'Goodbye', 'Hello Again','ketevan']
print(my_list[0::2])
