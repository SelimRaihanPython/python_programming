number = 41
flag = False
if number > 1:
	for i in range(2,number):
		if (number % i) == 0:
			flag = True
			break
if flag:
	print("It's not a Prime Number")
else:
	print("It's a Prime Number")


start = 25
end = 50
print("Prime Numbers Between", start , "and", end)

for number in range(start, end + 1):
	if number > 1:
		for i in range(2, number):
			if number % i == 0:
				break
		else:
			print(number)
