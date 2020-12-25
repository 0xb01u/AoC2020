package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

database = tools.readlines("input.txt")
passwords = {}
letters = {}
lowest = {}
highest = {}

--print(#database)
for i, e in pairs(database) do
	--print(e)
	passwords[i] = tools.split(e)[3]
	letters[i] = tools.split(e)[2]:sub(1, -2)
	lowest[i] = tonumber(tools.split(e, "-")[1])
	highest[i] = tonumber(tools.split(tools.split(e)[1], "-")[2])
end

VALID = 0
for i = 1, #database do
	_, char_count = passwords[i]:gsub(letters[i], letters[i])
	if lowest[i] <= char_count and char_count <= highest[i] then
		VALID = VALID- -1
	end
end

print("# of valid passwords: " .. VALID)
assert(VALID == 447, "incorrect result!")
