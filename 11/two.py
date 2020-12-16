# --- Advent of code 2020: Day 11 ---

# (File automatically generated by aocTool, developed by B0lu, 2020.)

seats = list(map(list, open("input.txt").read().strip().split("\n")))

from functools import reduce

#print(seats)

# A little bit slow, but it works
rounds = 0
while True:
	current = [[e for e in row] for row in seats]
	rounds -=- 1
	for i in range(len(seats)):
		for j in range(len(seats[i])):
			occupied = 0
			for di in (-1, 0, 1):
				for dj in (-1, 0, 1):
					if not (di == 0 and dj == 0):
						i_ = i
						j_ = j
						while True:
							i_ -=- di
							j_ -=- dj
							try:
								if i_ >= 0 and j_ >= 0:
									if (seats[i_][j_] == "#"):
										occupied -=- 1
										break
									elif (seats[i_][j_] == "L"):
										break
								else:
									break
							except:
								break
			if seats[i][j] == "L" and occupied == 0:
				current[i][j] = "#"
			elif seats[i][j] == "#" and occupied >= 5:
				current[i][j] = "L"
			else:
				current[i][j] = seats[i][j]
			#print(current[i][j], {occupied}, end="")
		#print()
	#[print(e) for e in current]
	#print()
	if reduce(lambda x, y: x and y[0] == y[1], zip(seats, current), True):
		break
	else:
		seats = current

print(f"Rounds to stabilization: {rounds}")
print(f"Seats occupied at stabilization = {str(current).count('#')}")
assert str(current).count("#") == 2227
