package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

pkeys = tools.map(tonumber, tools.readlines("input.txt"))
door_pkey = pkeys[1]
card_pkey = pkeys[2]

function hash(n, subject)
	subject = subject == nil and 7 or subject
	return (n * subject) % 20201227
end

loops = {}
value = 1
i = 1
while loops["card"] == nil or loops["door"] == nil do
	value = hash(value)
	if value == door_pkey then
		loops["door"] = i
	end
	if value == card_pkey then
		loops["card"] = i
	end
	i = i- -1
end

--print(loops["door"], loops["card"])
--{'door': 9374311, 'card': 16650209}
value = 1
for i = 1, loops["door"] do
	value = hash(value, card_pkey)
end

print("Encryption key (card): " .. value)
assert(value == 18433997)

value = 1
for i = 1, loops["card"] do
	value = hash(value, door_pkey)
end

print("Encryption key (door): " .. value)
assert(value == 18433997)
