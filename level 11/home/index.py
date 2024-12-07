#1)
score = int(input("enter your score"))

if score > 90 and score < 100:
   print("your grade is A")
elif score > 80 and score < 90:
   print("your grade is B")
elif score >70 and score < 80:
   print("your grade is C")
else:
   print("your grade is D")




#2)

age = int(input("plz enter yo age: "))

if age < 13:
   print("შე მცირეწლოვანოო!!")
elif age > 13 and age < 19:
   print("შე მართლა მოზარდო")
else:
   print("დაბერდი ძმა, თან მაგრა")


#3)

num = imput("pleez enter number: ")

if num == 0:
   print("ნულია")
elif num > 0:
   print("დადებითია  :) ")
else:
   print("უარყოფითი")





#4)


price = int(imput("plz enter price: "))

if price > 50:
   print(price % 10)
   print("last price")
elif price > 20 and price < 50:
   print(price % 5)
   print("last price")
elif price > 0 and price < 20:
   print("u r not gettin a discount")


#conditional statements ფუნქცია ხდება თუ რარაცა პირობა სიმართლეა
#if არის თუ რაღაცა სიმართლეა
#elif არის ამასთანავე თუ სხვა პირობა სიმართლეა
#else არის დანარჩენი სხვა პირობები რაც უნდა იყოს
