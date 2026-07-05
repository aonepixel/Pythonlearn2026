# # # a=int(input("Enter your name: "))
# # # b=int(input("Enter your age: "))
# # # c=int(input("Enter your profession: "))
# # # print(a+b+c)
# # # print(155>=50)



# # # print('where are you',end="! ")
# # # print ('are you blind')
# # # print('my school code is',5512,'.')
# # # print(type(False))

# # # Print the text "I am" and the number 25 in one print statement
# # print("I am", end=" ")

# # print (25)
# # print("I am", 25)

# # x= str(5)
# # y=int(5)
# # z=float(5)
# # a=bool(0)
# # print(x, y, z, a)
# # X, Y, Z = "Apple", "Banana", "Mango"
# # print (X)
# # print(Y)
# # print(Z)

# # names = ("manish", 'asma','manish')
# # A, B, C = names
# # print(B)

# # x="developer"
# # def myfun(): print("I am a " + x)
# # myfun()

# x=5
# y=x
# z="Hello"
# print(type(y))

# m=5e2
# print(m)

# n=int(5)
# g=bool(n)
# print(g)

# import random
# print (random.randrange(0, 10))


# Create a variable x and assign it the integer 5
# Create a variable y and assign it the float 3.14
# Create a variable z and assign it the complex number 2+3j
# Print the type of each variable using type()
# x=str(5)
# y=float(3.14)
# z=complex(2+3j)

# print(type(x))
# print(type(y))
# print(type(z))

# a="abcdefghijklm"
# print(a[2:5])
# print(a[2:5:2])

# b="0123456789"
# print (b[4:7])
# c="mohammad afzal"
# print(c[::-1])

# k=["afzal", "salman", "don", "designer", "developer", "content writer"]
# # for names in (k): print(k)
# print(k[1:5])

# m=12,13,14,15,16,17,18,19,20
# a=45,15
# print(m[2:8])
# print(a)
# p=str("this is paragraph")
# print(type(k))

# x=20
# for x in range(20): print(x)

# fruits=["Apple", "Banana", "Mango", "Grapes"]
# for fal in fruits:
#     print(fal)

#     number = 1
#     while number:
#     print(number)
#     number +=2

# slogan='''My name is Developer but I don't know about development, Still learnig. by "Unknown" '''
# if "KA" not in slogan: print("You are not developer")
# if "Developer" in slogan: print ("You are developer.")
# name=input("Who is developer: ")


#Slicing
# slice="School"
# print(slice[4:5])

# slice2="01234567890"
# print(slice2[3:8])

# slice3="Crystal"
# print(slice3[3:5])

# slice4="anidam"
# print(slice4[::-1])

#Python - Modify Strings

#Upper Case
# name1="mohammad afzal is designer."
# print(name1.upper())

# #Lower Case
# name2 = "MOHAMMAD AFZAL IS DESIGNER."
# print(name2.lower())

# #Remove Whitespace
# #The strip() method removes any whitespace from the beginning or the end:
# name3="   Python is the easiest language in the world."
# print(name3.strip())

# #Replace String
# name4=name3
# print(name4.replace("Python", "Sigma"))

# #The split() method returns a list where the text between the specified separator becomes the list items.
# split="Mohammad Afzal"
# print(split.split(" "))

#String Concatenation : To concatenate, or combine, two strings you can use the + operator.
# #To add a space between them, add a " ":
# a1="Mohammad"
# a2="Afzal"
# c= a1+a2
# print(c)
# d=a1+(" ")+("To")+(" ")+a2
# print(d)



#F-Strings
age = 20
name1 = "Mohammad Afzal"
student1=f"My name is Python and I am {age} year old."
print(student1)

price="10$"
des=f"Now apple price is {price}. This is too much"
print(des)

poor="Aone"
des2=f"5KG apples price is {5*10} & {price}. This is too much for {poor} people."
print(des2)

#Escape Character

tex1="Hanny is very bad person but he is \"mad.\""
print(tex1)
tex2= "Jony Jony Yes Papa! \nEating suger No Papa!"
print(tex2)
