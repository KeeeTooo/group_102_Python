# file1=open("day 27.txt","r") 
# readcont=file1.read()
# print(readcont)



# myfile=open("davaleba27.txt","r") 
# cont=myfile.readlines()
# print(cont)
# myfile.close()


# myfile=open("davaleba27.txt","r") 
# cont=myfile.readlines()[2][0]
# print(cont)
# myfile.close()


#5 რენდომ წინადადებაში დავთვალოთ ხმოვნები და დავპრინტოთ

myfile=open("davalebagasaketebeli.txt","r")
cont=myfile.readlines()
c=0
for i in  range(5):
    c=0
    for j in cont[i]:
        if j in "aeiou":
            c+=1
    print(cont[i])
    print(c)
myfile.close()
