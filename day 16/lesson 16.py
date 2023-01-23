# print (int(str(34.0//3)[:-2]))

# print(int(6//2.0))

# import random
# num1=random.randint(5,23)
# print(num1)
# num2=random.randrange(44)
# print(num2)

# list=["keti","nia","dato"]
# print(random.choice(list))

# name="ketevan"
# print(random.choice(name))

# my_arr=[5,6,4,3]
# def my_join(my_arr):
#     fstr=""
#     for i in my_arr:
#      fstr+=str(i)
#     return fstr
  
# print(my_join(my_arr))

# name="ketevan1"
# print(name[:-2])


# my_arr=[i for i in range(15,25) if i % 4==2]
# print(my_arr)

# friends={"dato":"14",
#         "luka":15,
#         "keti":"15",
#         "AND OTHERS":"?"}
# print(friends["luka"])
# print(friends["keti"])


# def twice_as_old(a,b):    # გადაეცემა ორი პარამეტრი 4  (47 და 14)
#     return abs(a-b*2)     # აბრუნებს a-b*2  ანუ 47-28  ანუ 19
# print (twice_as_old(47,14)*(33,2)) #დაპრინტოს 19 ჯერ (33 , 2)

# def never(arr):
#     i=0
#     while i<len(arr)-10:   #none
#         if arr[i+10]-arr[i]!=10:
#             return arr[i+10]
#         i+=10
# print(never([10,20,35,30,40,50]))

# arr=[1,2,"3"]
# arr1=[]
# s=0
# for i in arr:
#     arr1.append(int(i))
# for j in arr1:
#     s+=j
# print(s)

s="Ketevan !!!"
ss=""
for i in s:
    if i in "!":
        continue
    else:
        ss+=i
print(ss)
