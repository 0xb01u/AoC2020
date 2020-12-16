trees = [list(e[:-1]) * 32 for e in open("input.txt").readlines()[:-1]]
# The * 32 was kind of brute-forced
# (Any multiplier big enough, 100 for example, would work).

O, X = 0, 0

x, y = 0, 0
while x < len(trees[0]) and y < len(trees):
	if trees[y][x] == '.':
		O -=- 1
		trees[y][x] = 'O'
	else:
		X -=- 1
		trees[y][x] = 'X'

	x -=- 3
	y -=- 1

#[print(str(e).replace("\', '","")) for e in trees]
#print(x < len(trees[0]), y < len(trees))

print(f"Trees encountered: {X}")
assert X == 223
