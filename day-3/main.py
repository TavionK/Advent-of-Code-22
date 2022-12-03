def getPriority_():
	matches = []
	p = 0
	firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
	for x in firstpart:
		for y in secondpart:
			if x == y:
				if y not in matches:
					matches.append(y)
	for z in matches:
		p += letters.index(z)+1
	return(p)

def newPriority_():
	matches = []
	p = 0
	for x in first:
		for y in second:
			for z in third:
				if x == y and x == z:
					if z not in matches:
						if z in letters:
							matches.append(z)

	for n in matches:
		p += letters.index(n)+1
	return(p)

letters = ["a", "b", "c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

f = open("input.txt", "r")
lines = f.readlines()
priority = 0
count = 0
for line in lines:
	count += 1
	current = getPriority_()
	priority += current

solution = 0
start = 0
end = len(lines)
step = 3
for i in range(start, end, step):
	x = i
	first = lines[x]
	second = lines[x+1]
	third = lines[x+2]
	current = newPriority_()
	solution += current

print(priority)
print(solution)