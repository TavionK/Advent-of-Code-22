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
		# print(tl)
		count += 1
		result = checkDup_(tl)
		if result is False:
			print(count+3)
			return


f = open("input.txt", "r")
original = f.readline()
line = list(original)
# print(line)
getFour_()
