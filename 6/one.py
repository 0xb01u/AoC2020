print("Sum of answers: " + str(sum(map(lambda e: len({c for l in e.split("\n") for c in l}), open("input.txt").read().split("\n\n")[:-1]))))
assert sum(map(lambda e: len({c for l in e.split("\n") for c in l}), open("input.txt").read().split("\n\n")[:-1])) == 6625