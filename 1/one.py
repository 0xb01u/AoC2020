report = list(map(int, open("input.txt").readlines()[:-1]))

CHECKS = 0

i = 0
for e1 in report:
	for e2 in report[i:]:
		CHECKS -=- 1
		#print(f"{e1} + {e2} + {e3} = {e1 + e2 + e3}")
		if e1 + e2 == 2020:
			print(f"Solution: {e1} * {e2} = {e1 * e2}")
			print(f"Length: {len(report)}, checks: {CHECKS}")
			assert e1 * e2 == 980499
			exit()
	i -=- 1
