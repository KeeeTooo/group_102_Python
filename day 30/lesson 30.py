# l=[1,2,'aasf','1','123',123,15]
# li=[]
# for i in l:
#     for j in str(i):
#         if str(j) in "0123456789":
#            li.append(i)
#         else:
#            continue
# print(list(li))





# l=[1, 2, 'a', 'b']
# li=[]
# for i in l:
#     if type(i)==int:
#         li.append(i)
# print(list(li))
        

# stset={"ketevan","ketevan","kristi","ani"}        # დუბლიკატებს აქრობს set რასაც მივუწერთ სიას
# print(stset) 

# stset=("kketevann")                                # string -ში  დუბლიკატები ამოვიღოთ
# a=set(list(stset))
# print(a)



# string="How can mirrors be real if our eyes aren't real"
# st=string.split()
# s=""
# #print(st)
# for i in st:
#     s+=str(i).capitalize() 
#     s+=" "
# print(s)


# s="abcd"
# ss=""
# for i in range(len(s)):
#     print(str(i)+s[i])
#     #ss+=s[i]*i


# dna="ATGC"
# dd=""
# d={"A":"T",
#    "T":"A",
#    "G":"C",
#    "C":"G"}
# for i in dna:
#     dd+=d[i]

# print(dd)


# a=[5, 8, 12, 18, 22]
# b=0
# b+=min(a)
# a.remove(min(a))
# b+=min(a)

# print (b)

# a=[5, 8, 12, 18, 22]
# b=(sorted(a))
# print(b[0]+b[1])



# a=-5
# b=-2

# c=min(a,b)
# #print(c)
# d=0
# for i in range(a,b+1):
#     d+=i
# print(d)

cc="4556364607935616"
c=""
for i in range(len(cc)-4):
    c+="#"
c+=cc[-4]
c+=cc[-3]
c+=cc[-2]
c+=cc[-1]
print(c)










