def rps_():
	res = 0
	if 'X' in x[1]:
		if 'A' in x[0]:
			res = 3
		elif 'B' in x[0]:
			res = 0
		elif 'C' in x[0]:
			res = 6
	elif 'Y' in x[1]:
		if 'A' in x[0]:
			res = 6
		elif 'B' in x[0]:
			res = 3
		elif 'C' in x[0]:
			res = 0
	elif 'Z' in x[1]:
		if 'A' in x[0]:
			res = 0
		elif 'B' in x[0]:
			res = 6
		elif 'C' in x[0]:
			res = 3
	return(res)

def auto_():
	res = 0
	if 'X' in x[1]:
		res = 1
	elif 'Y' in x[1]:
		res = 2
	elif 'Z' in x[1]:
		res = 3
	return(res)

def outcome_():
	res = 0
	if 'X' in x[1]:
		res = 0
	elif 'Y' in x[1]:
		res = 3
	elif 'Z' in x[1]:
		res = 6
	return(res)

def forced_():
	res = 0
	if 'X' in x[1]:
		if 'A' in x[0]:
			res = 3
		elif 'B' in x[0]:
			res = 1
		elif 'C' in x[0]:
			res = 2
	elif 'Y' in x[1]:
		if 'A' in x[0]:
			res = 1
		elif 'B' in x[0]:
			res = 2
		elif 'C' in x[0]:
			res = 3
	elif 'Z' in x[1]:
		if 'A' in x[0]:
			res = 2
		elif 'B' in x[0]:
			res = 3
		elif 'C' in x[0]:
			res = 1
	return(res)

lines = []
f = open("input.txt", "r")
lines = f.readlines()
score = 0
second = 0
count = 0

for line in lines:
	count += 1
	current = 0
	x = line.split(" ")
	current = auto_() + rps_()
	score = score + current

	new = forced_() + outcome_()
	second = second + new
print("Answer to part one: " + str(score))
print("Answer to part two: " + str(second))
















