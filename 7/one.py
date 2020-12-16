# --- Advent of code 2020: Day 7 ---

# (File automatically generated by aocTool, developed by B0lu, 2020.)

rules = [e.split("contain") for e in open("input.txt").readlines()]

bags = ["shiny gold"]
outer = []
contained = True
VALID = set()
while contained:
	contained = False
	for current in bags:
		for rule in rules:
			if current in rule[1]:
				#print(current, rule)
				contained = True
				outer.append(rule[0].split(" contain")[0][:-2])
				VALID.add(rule[0].split(" contain")[0][:-2])

	bags = outer[:]
	outer = []

print(f"Valid colors: {len(VALID)}")
assert len(VALID) == 289