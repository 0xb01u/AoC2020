print("Valid passports: " + str(len([e.replace("\n", " ").split(" ") for e in open("input.txt").read().split("\n\n") if "byr" in e and "iyr" in e and "eyr" in e and "hgt" in e and "hcl" in e and "ecl" in e and "pid" in e])))
assert len([e.replace("\n", " ").split(" ") for e in open("input.txt").read().split("\n\n") if "byr" in e and "iyr" in e and "eyr" in e and "hgt" in e and "hcl" in e and "ecl" in e and "pid" in e]) == 256