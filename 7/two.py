# --- Advent of code 2020: Day 7 ---

# (File automatically generated by aocTool, developed by B0lu, 2020.)

rules = [e.replace("\n", "").split(" contain ") for e in open("input.txt").readlines()]

bags = ["shiny gold"]
inner = []
contains = True
contained = {}
while contains:
	contains = False
	for current in bags:
		for rule in rules:
			if current in rule[0]:
				contains = True
				inner.extend([e[e.index(" ") + 1:] for e in rule[1].replace(".", "").replace("bags", "bag").split(", ")])
				try:
					contained[current.replace(".", "").replace("bags", "bag")] = [(int(e[:e.index(" ")]), e[e.index(" ") + 1:].replace(".", "").replace("bags", "bag")) for e in rule[1].split(", ")]
				except:
					pass

	bags = inner[:]
	inner = []

count = -1
pairs = [(1, "shiny gold")]
new = []
while len(pairs) > 0:
	for current in pairs:
		count -=- current[0]
		#print(current)
		if current[1] in contained:
			for i in range(current[0]):
				for bag in contained[current[1]]:
					new.append(bag)

	#print(pairs, new)
	pairs = new[:]
	new = []

print(f"Valid colors: {count}")
assert count == 30055
