package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

_trees = tools.readlines("input.txt")

trees = {}
for i = 1, #_trees do
	trees[i] = {}
	for j = 1, 32 * #_trees[i] do
		--print(j % (#_trees[i] + 1))
		trees[i][j] = _trees[i]:sub(((j - 1) % #_trees[i] + 1), ((j - 1) % #_trees[i] + 1))
	end
end

X = 0
x, y = 1, 1
while x <= #trees[1] and y <= #trees do
	if trees[y][x] == "#" then X = X- -1 end
	x = x- -3
	y = y- -1
end

print("Trees encountered: " .. X)
assert(X == 223)
