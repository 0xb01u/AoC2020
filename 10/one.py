# --- Advent of code 2020: Day 10 ---

# (File automatically generated by aocTool, developed by B0lu, 2020.)

output_joltage = list(sorted(map(int, open("input.txt").readlines())))
output_joltage.insert(0, 0)
output_joltage.append(max(output_joltage) + 3)

diffs = [output_joltage[e] - output_joltage[e - 1] for e in range(1, len(output_joltage))]

print(f"1-jolt differences * 3-jolt differences: {diffs.count(1) * diffs.count(3)}")
assert diffs.count(1) * diffs.count(3) == 2240