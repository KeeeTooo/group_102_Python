print ("this is lesson 2")
print(len("keti"))


my_sentence="""გამარჯობა, მე ვარ ქეთევან ლიპარტელიანი,ჩემი 
მიზანია ვიყო ყველაზე ყველაზე  """
print (my_sentence)



if 10>5:                     #indentation   tab საშუალებით
 print("hello")


 full_name="nika keshelava"
 print(len(full_name))
 #yvela stringi SegviZlia miviCnioT siad
 print(full_name[0])

 print ("Z" in full_name)

 print("k" not in full_name)
 print( full_name [2:7])
 print( full_name [2:7:2])   #start:finish:step
print( full_name [:7])

full_name = "ketevan liparteliani"
print (full_name)

print( full_name [-1])
print( full_name [-4])
print( full_name [-1:-6:-1])

#სტრინგბს აქვთ მეთოდები
#STRING.UPPER()
#LEN(STRING)
print (full_name.upper())

name2="          keti"
print(name2.strip())


print(name2.replace("","#"))

print(name2.replace("i","#"))