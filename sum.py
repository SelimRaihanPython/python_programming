#Program for Summation of all the Numbers Under the Input Value!
s=0
value = int (input ("The Numbers: "))
for i in range(1, value+1, 1):
	s +=i
print ("\n")
print ("sum is: ", s)