seats = open("input.txt").readlines()
rows = [seat[:7] for seat in seats]
columns = [seat[7:-1] for seat in seats]

ids = []
for row in rows:
	lo = 0
	hi = 127
	for char in row:
		#print(row, char)
		m = (lo + hi) // 2
		if char == "F":
			hi = m
		elif char == "B":
			lo = m + 1
		#print(char, m, lo, hi)

	m = lo if char == "F" else hi
	ids.append(m*8)

i = 0
for col in columns:
	lo = 0
	hi = 7
	for char in col:
		#print(col, char)
		m = (lo + hi) // 2
		if char == "L":
			hi = m
		elif char == "R":
			lo = m + 1
		#print(char, m, lo, hi)

	m = hi if char == "R" else lo
	ids[i] += m
	i -=- 1

ids.sort()

for i in ids[:-1]:
	if i + 1 not in ids:
		print(f"Your seat ID is {i + 1}")
		assert i + 1 == 669
