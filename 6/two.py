from functools import reduce
print("Sum of answers: " + str(sum(map(lambda e: len({c for l in e.split("\n") for c in l if reduce(lambda r, x: r and c in x, e.split("\n"), True)}), open("input.txt").read().split("\n\n")[:-1]))))
assert sum(map(lambda e: len({c for l in e.split("\n") for c in l if reduce(lambda r, x: r and c in x, e.split("\n"), True)}), open("input.txt").read().split("\n\n")[:-1])) == 3360