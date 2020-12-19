# --- Advent of code 2020: Day 19 ---

# (File automatically generated by aocTool, developed by B0lu, 2020.)

rules_, text = open("input.txt").read().split("\n\n")

import re

rules = {r.split(": ")[0]: r.split(": ")[1].split(" | ") for r in rules_.splitlines()}
symTab = {r: rf"({rules[r][0][1]})" for r in rules if '"' in rules[r][0]}
text = text.splitlines()

# Part 2:
#  New rule 8 can be expressed as a regex: (42)+,
#  so we just have to take that into account when it's the time
#  to expand rule 8.
#  Rule 11 cannot be expressed as a regex. It is a
#  context free grammar.

# FIRST PASS:
#  Express rule 11 as a regex that matches all the words that match
#  all the words that match the rule 11: (42)+ (31)+.
#  Thus, we will purge some results that we know for sure won't match
#  the actual rules, saving time on the second pass.

# Generate initial regexs for rules:
while "0" not in symTab:
	for r in rules.keys():
		if r not in symTab:	# Try to expand not expanded rules
			numbers = set([n for i in rules[r] for n in i.split(" ")])	# Rules used in this rule.

			if all([e in symTab for e in numbers]):	# If all the rules used are expanded:
				# Rule 11 will initially be (42)+ (31)+, which matches the valid words (and more).
				if r == "11":
					rules[r] = f"(({symTab['42']})+({symTab['31']})+)"
				elif r == "8":
					rules[r] = f"(({symTab['42']})+)"
				else:
					# Substitute in order the rule numbers with their definition:
					for n in sorted(numbers, key=int, reverse=True):
						regex = rules[r][0].replace(n, f"({symTab[n]})").replace(" ", "")
						if len(rules[r]) > 1:
							regex = f"({regex})|(" + rules[r][1].replace(n, f"({symTab[n]})").replace(" ", "") + ")"

						rules[r] = [regex]	# Needed so this for loop doesn't break on next iterations

					rules[r] = rules[r][0]
				symTab[r] = rules[r]

# Initial matches: contain false positives.
initial_matches = set()
m1 = {}
for t in text:
	# Rule 0 is always rule 8, then rule 11.
	match = re.match(rf"({rules['8']}){rules['11']}$", t)
	if match:
		initial_matches.add(t)
		m1[t] = match.group(1)


# SECOND PASS:
#  Similar to the first one, but
#  rule 11 is expanded to a huge lot of regexs, all containing
#  equal (and ordered) amounts of rules 42 and 31.
#  To estimate to how many of these regexs rule 11 has to expand,
#  we calculate:
#	- max_chars: the maximum number of chars in the initially
#	  matched words. We won't need to genereate regexs which contain
#	  more appearances of any rule (42 and 31, in this case)
#	  than this value, since there isn't any word with enough
#	  characters to match them (rules are non-null).
#	  It's the superior limit for the number of regexs generated.
#   - rule8_chars: minimum number of chars for all initially
#     matched words that were matched with rule 8. These number of
#	  chars can be subtracted form max_chars, since they are
#	  characters that won't match with rule 11.
#	- Since rule 11 can only expand to regexs that add rule
#	  appearences in pairs (each new regex will have one more rule
#	  42 and one more rule 31, so two more rules), we can divide
#	  max_chars by 2, saving a lot of regexs, and speeding up
#	  the process quite a lot. (Remember: rules will match at
#	  least one character).
#
#  All other rules will be expanded like in the first pass, since
#  they can be expressed with regexs.
#  This process is still quite slow, but has been reduced from
#  7min to 30s. That's quite a speed up!

max_chars = max(map(len, initial_matches))
rule8_chars = min(map(len, m1.values()))
#print(max_chars, rule8_chars)
max_chars +=- rule8_chars

# Reset data structures:
rules = {r.split(": ")[0]: r.split(": ")[1].split(" | ") for r in rules_.splitlines()}
symTab = {r: rf"({rules[r][0][1]})" for r in rules if '"' in rules[r][0]}

# Generate final regexs:
while "0" not in symTab:
	for r in rules.keys():
		if r not in symTab:	# Try to expand not expanded rules
			numbers = set([n for i in rules[r] for n in i.split(" ")])	# Rules used in this rule.

			if all([e in symTab for e in numbers]):	# If all the rules used are expanded:
				if r == "11":
					rx = f"((({symTab['42']})({symTab['31']})))"
					# Generate set of valid regexs:
					for i in range(1, max_chars // 2):	# Rules are added 2 by 2
						rx += f"|((({symTab['42']})" + f"({symTab['42']})"*i + f"({symTab['31']})"*i  + f"({symTab['31']})))"
					rules[r] = rx
				elif r == "8":
					rules[r] = f"(({symTab['42']})+)"
				else:
					# Substitute in order the rule numbers with their definition:
					for n in sorted(numbers, key=int, reverse=True):
						regex = rules[r][0].replace(n, f"({symTab[n]})").replace(" ", "")
						if len(rules[r]) > 1:
							regex = f"({regex})|(" + rules[r][1].replace(n, f"({symTab[n]})").replace(" ", "") + ")"

						rules[r] = [regex]	# Needed so this for loop doesn't break on next iterations

					rules[r] = rules[r][0]
				symTab[r] = rules[r]

# Final matches:
matches = 0
#m2 = {}
for t in initial_matches:
	if re.match(f"{rules['0']}$", t):
		matches -=- 1
	#else:
	#	m2[t] = t

print(f"Number of matches: {matches}")	# 421.4s lmao
										# 	EDIT: 163.8s after first improvement: 8 as regex and 2 passes.
										# 	EDIT 2: 125.1s after rule8_chars improvement.
										#	EDIT 3: 25.5s after I realized the range() generating all the
										#    rule 11 regexs could be divided by 2. GG.
assert matches == 237