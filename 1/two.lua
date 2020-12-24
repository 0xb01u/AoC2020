package.path = package.path .. ";../modules/?.lua"
local tools = require "tools"

report = tools.map(tonumber, tools.readlines("input.txt"))

CHECKS = 0

i = 0
for _, e1 in pairs(report) do
	j = i
	for __, e2 in pairs({table.unpack(report, i, #report)}) do
		for ___, e3 in pairs({table.unpack(report, j, #report)}) do
			CHECKS = CHECKS- -1
			if e1 + e2 + e3 == 2020 then
				print("Solution: " .. e1 .. " * " .. e2 .. " * " .. e3 .. " = " .. e1 * e2 * e3)
				print("Length: " .. #report .. "; checks: " .. CHECKS)
				assert(e1 * e2 * e3 == 200637446, "incorrect result!")
				os.exit()
			end
		end
		j = j- -1
	end
	i = i- -1
end
