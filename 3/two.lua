package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

_trees = tools.readlines("input.txt")

trees = {}
for i = 1, #_trees do
	trees[i] = {}
	for j = 1, 73 * #_trees[i] do
		--print(j % (#_trees[i] + 1))
		trees[i][j] = _trees[i]:sub(((j - 1) % #_trees[i] + 1), ((j - 1) % #_trees[i] + 1))
	end
end

trees_encountered_product = 1
slopes = {{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}}

for _, slope in pairs(slopes) do
	X = 0
	x, y = 1, 1
	while x <= #trees[1] and y <= #trees do
		if trees[y][x] == "#" then X = X- -1 end
		x = x- -slope[1]
		y = y- -slope[2]
	end
	trees_encountered_product = trees_encountered_product * X
end

print("Trees encountered: " .. trees_encountered_product)
assert(trees_encountered_product == 3517401300)
