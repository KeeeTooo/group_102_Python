@@ -1,45 +1,54 @@
print ("this is lesson 2")
print(len("keti"))
print("this is lesson 2 homework")

print (len("ketevan liparteliani"))    #დაითვალოს სიმბოლოების ოდენობა

my_sentence="""გამარჯობა, მე ვარ ქეთევან ლიპარტელიანი,ჩემი 
მიზანია ვიყო ყველაზე ყველაზე  """
print (my_sentence)

my_sentence="""მე ვარ ქეთევან ლიპარტელიანი, 
ჩემი მისამართია ანაპის დივიზიის 414"""""


if 10>5:                     #indentation   tab საშუალებით
 print("hello")
if 7>5 :                           #indentation პირობის დროს ორწერტილი და
 print("sworia")                   #გამოსატანი ინფორმაციის Tab ით დაწერა


 full_name="nika keshelava"
 print(len(full_name))
 #yvela stringi SegviZlia miviCnioT siad
 print(full_name[0])

 print ("Z" in full_name)
full_name= "ketevan liparteliani"
print (len(full_name))
# ყველა სტრინგი შეგვიძლია მივიჩნიოთ სიად, დავნომროთ და გამოვიტანოთ

 print("k" not in full_name)
 print( full_name [2:7])
 print( full_name [2:7:2])   #start:finish:step
print( full_name [:7])
print (full_name[0])   # 0 გამოაქვს პირველი სიმბოლო ბრჭყალების მერე

print ("z" in full_name)

print("k" not in full_name)

print( full_name [2:7])

print( full_name [2:7:2])   #start:finish:step

print( full_name [:6])      #ყველაფერი მეექვსე სიმბოლომდე
print( full_name [8:])      #ყველაფერი მერვე სიმბოლოდან

full_name = "ketevan liparteliani"
print (full_name)

print( full_name [-1])
print( full_name [-4])
print( full_name [-5])
print( full_name [-1:-6:-1])
print( full_name [-1:-6:-2])

#სტრინგბს აქვთ მეთოდები
#STRING.UPPER()
#LEN(STRING)
 #სტრინგბს აქვთ მეთოდები
 #STRING.UPPER()
 #string.strip()
 #LEN(STRING)
print (full_name.upper())
print (full_name.lower())

name2="          keti"
print(name2.strip())


print(name2.replace("","#"))

print(name2.replace("i","#"))
print(name2.replace("i","#"))
