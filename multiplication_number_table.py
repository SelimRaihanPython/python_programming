#Program to get any Multiplication Number Table of Any Entry, It takes a Input and Gives Multiplication of the Number
number = int(input("Enter The number: "))
print (number)
for i in range (1, 11, 1):
	product = number * i
	print ("The Product Is: ", product)