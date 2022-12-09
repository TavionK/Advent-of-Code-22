def getFrom_():
	x = line.split(" ")
	acc = x[3]
	res = ""
	if acc == "1":
		res = one
	elif acc == "2":
		res = two
	elif acc == "3":
		res = three
	elif acc == "4":
		res = four
	elif acc == "5":
		res = five
	elif acc == "6":
		res = six
	elif acc == "7":
		res = seven
	elif acc == "8":
		res = eight
	elif acc == "9":
		res = nine
	return(res)

def getTo_():
	x = line.split(" ")
	acc = x[5]
	res = ""
	if "1" in acc:
		res = one
	elif "2" in acc:
		res = two
	elif "3" in acc:
		res = three
	elif "4" in acc:
		res = four
	elif "5" in acc:
		res = five
	elif "6" in acc: 
		res = six
	elif "7" in acc:
		res = seven
	elif "8" in acc:
		res = eight
	elif "9" in acc:
		res = nine
	return(res)


def move_():
	x = line.split(" ")
	howMany = x[1]
	original = getFrom_()
	where = getTo_()
	stack = []
	count = 0
	#print(where)
	while count < int(howMany):
		where.append(original.pop())
		count += 1
	#print(where)
	# while count < int(howMany):
	#  	stack.append(original[count])
	#  	count += 1
	# for x in stack:
	# 	where.append(stack.pop())
	# print(where)

f = open("input.txt", "r")
lines = f.readlines()
one = ['R','S','L','F','Q']
two = ['N','Z','Q','G','P','T']
three = ['S','M','Q','B']
four = ['T','G','Z','J','H','C','B','Q']
five = ['P','H','M','B','N','F','S']
six = ['P','C','Q','N','S','L','V','G']
seven = ['W','C','F']
eight = ['Q','H','G','Z','W','V','P','M']
nine = ['G','Z','D','L','C','N','R']
count = 1
for line in lines:
	move_()
print(one.pop())
print(two.pop())
print(three.pop())
print(four.pop())
print(five.pop())
print(six.pop())
print(seven.pop())
print(eight.pop())
print(nine.pop())



























# 
	
