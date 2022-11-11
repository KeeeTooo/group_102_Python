# words =[ "acc","1","hello"]
# print("".join(words))


# a="keti kargi gogoa"   #გვაქვს სტრინგი
# b=a.split()            # გადავაქციეთ სიად
# c=[]                   #ცარიელი სია
# for i in b:            #სიაში ციკლი
#     c.append(i)        #ცარიელ სიაში ჩამატება
# c.reverse()            #სიის დატრიალება
# print (" - ".join(c))  # სიის გასტრინგება და შუაში ტირეების ჩამატება


# a="ketevan"            #string-ის დატრიალება
# print(a[::-1])


sheep=5
b=[]
for i in range(1,sheep+1):
    if i ==0:
        continue
    b.append(str(i)+"sheep...")
print ("".join(b))


# sheep=5
# b=[]
# for i in range(5+1):
#     if i ==0:
#         continue
#     b.append(str(i)+"sheep...")
# print ("".join(b))