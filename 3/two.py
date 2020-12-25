trees = [list(e[:-1]) * 73 for e in open("input.txt").readlines()]
# The * 73 was kind of brute-forced
# (Any multiplier big enough, 100 or 1000 for example, would work).

trees_encountered_product = 1
slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

for dx, dy in slopes:
	O, X = 0, 0

	x, y = 0, 0
	while x < len(trees[0]) and y < len(trees):
		if trees[y][x] == '.':
			O -=- 1
		else:
			X -=- 1

		x -=- dx
		y -=- dy

	#print(x < len(trees[0]), y < len(trees))
	trees_encountered_product *= X

print(f"Trees encountered: {trees_encountered_product}")
assert trees_encountered_product == 3517401300
