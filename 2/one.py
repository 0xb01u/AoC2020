database = open("input.txt").readlines()
passwords = [e.split(" ")[2] for e in database]
letters = [e.split(" ")[1][:-1] for e in database]
lowest = [int(e.split("-")[0]) for e in database]
highest = [int(e.split(" ")[0].split("-")[-1]) for e in database]

VALID = 0
for i in range(len(database)):
	if lowest[i] <= passwords[i].count(letters[i]) and passwords[i].count(letters[i]) <= highest[i]:
		VALID -=- 1

print(f"# of valid passwords: {VALID}")
assert VALID == 447
