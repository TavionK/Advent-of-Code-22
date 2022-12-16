def checkDup_(tl):
	for elem in tl:
		if tl.count(elem) > 1:
			return True
	return False

def getFour_():
	count = 0
	for x in line:
		tl = []
		dup = True
		tl.append(line[count])
		tl.append(line[count+1])
		tl.append(line[count+2])
		tl.append(line[count+3])
		count += 1
		result = checkDup_(tl)
		if result is False:
			print(count+3)
			return

def get14_():
	count = 0
	for x in line:
		tl = []
		dup = True
		tl.append(line[count])
		tl.append(line[count+1])
		tl.append(line[count+2])
		tl.append(line[count+3])
		tl.append(line[count+4])
		tl.append(line[count+5])
		tl.append(line[count+6])
		tl.append(line[count+7])
		tl.append(line[count+8])
		tl.append(line[count+9])
		tl.append(line[count+10])
		tl.append(line[count+11])
		tl.append(line[count+12])
		tl.append(line[count+13])
		count += 1
		result = checkDup_(tl)
		if result is False:
			print(count+13)
			return

f = open("input.txt", "r")
original = f.readline()
line = list(original)
getFour_()
get14_()
