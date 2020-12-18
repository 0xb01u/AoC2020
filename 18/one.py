# --- Advent of code 2020: Day 18 ---

# (File automatically generated by aocTool, developed by B0lu, 2020.)

ops = open("input_mod1.txt").readlines()

class Num():
	def __init__(self, n):
		self.n = n

	def __add__(self, other):
		return Num(self.n + other.n)

	def __sub__(self, other):
		return Num(self.n * other.n)

r = []
for op in ops:
	#print(op)
	exec(f"r.append({op})")

int_r = [n.n for n in r]
print(sum(int_r))
