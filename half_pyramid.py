rows = int(input("Enter The Number of Lines: ")) #Program to print half pyramid a using numbers
for i in range(rows):
	for j in range(i+1):
		print(j+1, end="")

	print("\n")


rows = int (input("Enter Lines: ")) #Program to print half pyramid using alphabets
ascii_value = 65
for i in range(rows):
	for  j in range(i+1):
		alpahbet = chr(ascii_value)
		print(alpahbet, end=" ")
	ascii_value +=1
	print("\n")

rows = int (input("Enter The Lines You Want: ")) #Inverted half pyramid using *
for i in range(rows,0, -1):
	for j in range(0, i):
		print("* ", end="")
	print("\n")

rows = int (input("Enter The Lines")) #Inverted half pyramid using numbers
for i in range(rows,0, -1):
	for j in range(1,i+1):
		print(j, end="")
	print("\n")
