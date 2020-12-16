all_fields = [e.replace("\n", " ").split(" ") for e in open("input.txt").read().split("\n\n") if "byr" in e and "iyr" in e and "eyr" in e and "hgt" in e and "hcl" in e and "ecl" in e and "pid" in e]
all_fields[-1].pop()

VALID = 0
for e in all_fields:
	valid = True
	for k, v in map(lambda x: x.split(":"), e):
		if k == "byr":
			_valid = len(v) == 4 and v.isdigit() and int(v) >= 1920 and int(v) <= 2002
		elif k == "iyr":
			_valid = len(v) == 4 and v.isdigit() and int(v) >= 2010 and int(v) <= 2020
		elif k =="eyr":
			_valid = len(v) == 4 and v.isdigit() and int(v) >= 2020 and int(v) <= 2030
		elif k == "hgt":
			_valid = (v[-2:] == "cm" and v[:-2].isdigit() and int(v[:-2]) >= 150 and int(v[:-2]) <= 193) or (v[-2:] == "in" and v[:-2].isdigit() and int(v[:-2]) >= 59 and int(v[:-2]) <= 76)
		elif k == "hcl":
			_valid = v[0] == "#" and len([e for e in v[1:] if ord(e) in range(ord("0"), ord("9") + 1) or ord(e) in range(ord("a"), ord("f") + 1)]) == 6
		elif k == "ecl":
			_valid = v == "amb" or v == "blu" or v == "brn" or v == "gry" or v == "grn" or v == "hzl" or v == "oth"
		elif k == "pid":
			_valid = len(v) == 9 and v.isdigit()
		else:
			_valid = True

		valid = valid and _valid
		#print(k, v, _valid)

	#print(valid)
	VALID -=- valid

print(f"True valid passports: {VALID}")
# I'm dumb dumb and I don't know Python regex.
assert VALID == 198
