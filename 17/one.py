# --- Advent of code 2020: Day 17 ---

# (File automatically generated by aocTool, developed by B0lu, 2020.)

init = open("input.txt").readlines()

active = {(i, j, 0) for i in range(len(init)) for j in range(len(init[0])) if init[i][j] == "#"}

#print(active)

activity = {}

for _ in range(6):
	for p in active:
		for di in (-1, 0, 1):
			for dj in (-1, 0, 1):
				for dk in (-1, 0, 1):
					if di or dj or dk:
						if (p[0] + di, p[1] + dj, p[2] + dk) in activity:
							activity[(p[0] + di, p[1] + dj, p[2] + dk)] -=- 1
						else:
							activity[(p[0] + di, p[1] + dj, p[2] + dk)] = 1
	#print(activity)

	next_active = set()
	for k, v in activity.items():
		if k in active:
			if v == 2 or v == 3:
				next_active.add(k)
		else:
			if v == 3:
				next_active.add(k)

	active = next_active
	activity = {}
	

print(f"# of active cubes: {len(active)}")
assert len(active) == 313