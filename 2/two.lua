package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

database = tools.readlines("input.txt")
table.remove(database, #database)
passwords = {}
allowed = {}
first = {}
last = {}

--print(#database)
for i, e in pairs(database) do
	--print(e)
	passwords[i] = tools.split(e)[3]
	allowed[i] = tools.split(e)[2]:sub(1, -2)
	first[i] = tonumber(tools.split(e, "-")[1])
	last[i] = tonumber(tools.split(tools.split(e)[1], "-")[2])
end

VALID = 0
for i = 1,#database do
	if (passwords[i]:sub(first[i], first[i]) == allowed[i])
		~= (passwords[i]:sub(last[i], last[i]) == allowed[i]) then
		VALID = VALID- -1
	end
end

print("# of valid passwords: " .. VALID)
assert(VALID == 249, "incorrect result!")
