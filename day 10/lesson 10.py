# surname="liparteliani"
# print(surname[1:5])


# def greet():
#     return "hello world!"

# print(greet)


# num=123654
# arr=[]
# for i in str(num):
#     arr.append(int(i))
# arr.reverse()
# print(arr)
#---------------------------------------------------------------------


# name="ketevan liparteliani"

# print(str(name.split(' ')[0][0]).upper() + '.' + str(name.split(' ')[1][0]).upper())


# txt = "ketevan liparteliani"

# x = txt.split()
# a=str(x[0][0])
# b=str(x[1][0])
# print(a.upper()+"."+b.upper())


# list =["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# i=0
# for char in list:
#     if char in "needle":
#       print("found the needle at position {}".format(i))
#     i+=1

#list =["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]
# print(list.index("needle"))

# my_str="nika 11 keshelava"
# print(my_str[5]+my_str[6]+"4")
# --------------------------------------------------------------------------

# 1)დაბეჭდოს 6
# m_str=[]
# for i in my_str:
#     m_str.append(i)
# print(int(m_str[5])+int(m_str[6])+4)

# 2)დაბეჭდოს 15
# m_str=[]
# for i in my_str:
#     m_str.append(i)
# print(int(m_str[5])+int(m_str[6])+13)
# -----------------------------------------------------------------------

# 
# arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# a=0
# b=0
# if arr==[]:
#     print([])
# elif arr==[0,0]:
#     print([])
# else:
#     for i in arr:
#         if i >0:
#            a+=1
#         elif i<0:
#          b+=i
        
#     print(a,b)
#---------------------------------------------------------------------------

# n=15
# x=3
# y=5


# if n%x==0 and n%y==0:
#     print("true because {} is divisible by {} and {}".format(n,x,y))
# elif n%x!=0 and n%y!=0:
#     print ( "false because {} is neither divisible by {} nor {}".format(n,x,y))
# elif n%x!=0 and n%y==0:
#     print("false because {} is not divisible by {}".format(n,x)  )
# elif n%x==0 and n%y!=0:
#     print ( "false because {} is not divisible by {}".format(n,y))