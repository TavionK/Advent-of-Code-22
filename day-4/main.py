def getOverlap_():
	# split line by the ","
	# split the two by the lines by the -
	# convert to ints
	res = 0
	x = line.split(",")
	first = x[0]
	second = x[1]
	one = first.split("-")
	two = second.split("-")
	if int(one[0]) >= int(two[0]) and int(one[1]) <= int(two[1]):
		res = 1
	elif int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[1]):
		res = 1
	return(res)

def getRangeOverlap_():
	res = 0
	x = line.split(",")
	first = x[0]
	second = x[1]
	one = first.split("-")
	two = second.split("-")
	if int(one[0]) <= int(two[0]) and int(one[1]) >= int(two[0]):
		res = 1
	elif int(two[0]) <= int(one[0]) and int(two[1]) >= int(one[0]):
		res = 1
	return(res)

f = open("input.txt", "r")
lines = f.readlines()
overlap = 0
rangeOverlap = 0
count = 0
for line in lines:
	count += 1
	overlap += getOverlap_()
count = 0
for line in lines:
	count += 1
	rangeOverlap += getRangeOverlap_()

print(overlap)
print(rangeOverlap)