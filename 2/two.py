database = open("input.txt").readlines()
passwords = [e.split(" ")[2] for e in database]
allowed = [e.split(" ")[1][:-1] for e in database]
first = [int(e.split("-")[0]) for e in database]
second = [int(e.split(" ")[0].split("-")[-1]) for e in database]

VALID = 0
for i in range(len(database)):
	if (passwords[i][first[i] - 1] == allowed[i]) ^ (passwords[i][second[i] - 1] == allowed[i]):
		VALID -=- 1

print(f"# of valid passwords: {VALID}")
assert VALID == 249
