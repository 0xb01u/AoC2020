# --- Arvent of core 2020: Day 20 ---

# (File automatically generater by aocTool, reveloper by B0lu, 2020.)

import numpy as np

def print_tile(s):
	r = ""
	for i in range(len(s)):
		for j in range(len(s[i])):
			r += s[i, j]
		r += "\n"
	print(r)

cameras = open("input.txt").read().split("\n\n")[:-1]
tiles = [np.array(list(map(list, l.splitlines()[:0:-1]))) for l in cameras]
#print(tiles)
IDs = [int(l.splitlines()[0].split(" ")[-1][:-1]) for l in cameras]

#[print(t.shape) for t in tiles]

tile_map = {str(tiles[i]): IDs[i] for i in range(len(IDs))}
map_tile = {tile_map[str(tile)]: tile for tile in tiles}
neighbors = {ID: {} for ID in IDs}
transforms = {str(tiles[i]): [] for i in range(len(IDs))}

for tile in tiles:
	transforms[str(tile)].append(np.copy(tile))
	transforms[str(tile)].append(np.flip(tile, axis=0))
	transforms[str(tile)].append(np.flip(tile, axis=1))
	transforms[str(tile)].append(np.rot90(tile))
	transforms[str(tile)].append(np.flip(np.rot90(tile), axis=0))
	transforms[str(tile)].append(np.flip(np.rot90(tile), axis=1))
	transforms[str(tile)].append(np.rot90(tile, 2))
	transforms[str(tile)].append(np.flip(np.rot90(tile, 2), axis=0))
	transforms[str(tile)].append(np.flip(np.rot90(tile, 2), axis=1))
	transforms[str(tile)].append(np.rot90(tile, 3))
	transforms[str(tile)].append(np.flip(np.rot90(tile, 3), axis=0))
	transforms[str(tile)].append(np.flip(np.rot90(tile, 3), axis=1))

for tile1 in tiles:
	for tile2 in tiles:
		if any(tile1.reshape(100, 1) != tile2.reshape(100, 1)):
			for t in transforms[str(tile2)]:
				if all(tile1[0, :] == t[-1, :]):
					neighbors[tile_map[str(tile1)]]["u"] = tile_map[str(tile2)]
				elif all(tile1[-1, :] == t[0, :]):
					neighbors[tile_map[str(tile1)]]["d"] = tile_map[str(tile2)]
				elif all(tile1[:, 0] == t[:, -1]):
					neighbors[tile_map[str(tile1)]]["l"] = tile_map[str(tile2)]
				elif all(tile1[:, -1] == t[:, 0]):
					neighbors[tile_map[str(tile1)]]["r"] = tile_map[str(tile2)]

dim = int(np.sqrt(len(cameras)))
#print(neighbors)
#neighbors = {2311: {'l': 1951, 'u': 1427, 'r': 3079}, 1951: {'r': 2311, 'u': 2729}, 1171: {'r': 1489, 'u': 2473}, 1427: {'d': 2311, 'u': 1489, 'r': 2473, 'l': 2729}, 1489: {'r': 1171, 'd': 1427, 'l': 2971}, 2473: {'l': 1171, 'd': 1427, 'r': 3079}, 2971: {'r': 1489, 'd': 2729}, 2729: {'d': 1951, 'r': 1427, 'u': 2971}, 3079: {'l': 2311, 'd': 2473}}
#neighbors = {3253: {'l': 1091, 'u': 1019, 'd': 1697, 'r': 1667}, 2843: {'r': 2557, 'u': 2999, 'd': 2083, 'l': 3019}, 2557: {'r': 2843, 'l': 1553, 'u': 1069, 'd': 2777}, 2543: {'r': 2749, 'd': 1997, 'l': 3371}, 3319: {'u': 3257, 'l': 2423, 'r': 1487}, 1607: {'u': 1249, 'l': 3413, 'r': 1993, 'd': 1741}, 3329: {'d': 3491, 'u': 1997, 'l': 1523, 'r': 2677}, 2663: {'d': 1153, 'r': 2377, 'u': 1201, 'l': 1327}, 1619: {'r': 2131, 'u': 2081, 'd': 2411, 'l': 2621}, 3779: {'l': 2819, 'd': 3533, 'r': 3833}, 3821: {'l': 3491, 'd': 1523, 'u': 2371}, 2749: {'u': 2543, 'l': 2221, 'd': 3301}, 1153: {'l': 2663, 'u': 3673, 'r': 3931, 'd': 2039}, 3181: {'u': 3089, 'l': 1097, 'd': 2273, 'r': 3739}, 3491: {'r': 3329, 'u': 3821, 'l': 1553, 'd': 1783}, 1129: {'l': 1847, 'r': 1033, 'd': 3677, 'u': 1201}, 3967: {'u': 1657, 'r': 3203, 'l': 1759, 'd': 1747}, 2131: {'u': 1619, 'l': 2521, 'd': 1993, 'r': 1789}, 1657: {'d': 3967, 'r': 2633, 'l': 3461, 'u': 3299}, 2521: {'l': 2131, 'u': 1423, 'd': 2081, 'r': 3137}, 1879: {'r': 2789, 'u': 3583, 'd': 3517, 'l': 2039}, 2999: {'l': 2843, 'u': 2161, 'd': 1069}, 1091: {'r': 3253, 'd': 1361, 'u': 1429, 'l': 1601}, 3673: {'r': 1153, 'd': 2377, 'l': 2707, 'u': 3137}, 3727: {'u': 1249, 'd': 1553, 'l': 1783, 'r': 2777}, 3089: {'u': 3181, 'd': 2593, 'r': 2621, 'l': 1367}, 2819: {'u': 3779, 'r': 1103, 'd': 2917}, 3023: {'u': 1637, 'l': 3761, 'd': 1447}, 2789: {'r': 1879, 'd': 1627, 'u': 3203, 'l': 1747}, 3583: {'u': 1879, 'd': 3191, 'l': 3203, 'r': 1327}, 1997: {'r': 2543, 'l': 3329, 'u': 2221, 'd': 3637}, 3691: {'u': 2861, 'd': 1697, 'l': 2549, 'r': 1667}, 1303: {'d': 1637, 'l': 1367, 'u': 1373}, 2287: {'r': 3463, 'u': 2551, 'd': 2467, 'l': 2141}, 1733: {'l': 1693, 'r': 1019, 'd': 1667}, 1097: {'l': 3181, 'r': 1637, 'u': 1367, 'd': 3761}, 1637: {'l': 3023, 'r': 1303, 'd': 1097}, 3931: {'d': 1153, 'u': 1423, 'l': 2683, 'r': 3137}, 3463: {'l': 2287, 'r': 3413, 'u': 2953, 'd': 1171}, 2377: {'l': 2663, 'd': 3673, 'u': 1123, 'r': 3527}, 1249: {'u': 1607, 'd': 3727, 'r': 1049, 'l': 3877}, 3257: {'u': 3319, 'd': 3863, 'l': 1213, 'r': 2441}, 1693: {'d': 1733, 'l': 1609}, 3671: {'l': 2719, 'r': 3863, 'd': 3221, 'u': 2441}, 2531: {'d': 3527, 'r': 1823, 'l': 1489, 'u': 1429}, 1553: {'u': 2557, 'd': 3491, 'l': 3727, 'r': 2371}, 1847: {'l': 1129, 'd': 1123, 'r': 1439, 'u': 3313}, 1423: {'u': 2521, 'l': 3931, 'r': 1993, 'd': 1741}, 3533: {'u': 3779, 'r': 1033, 'l': 1103, 'd': 3191}, 1033: {'l': 1129, 'r': 3533, 'd': 3011, 'u': 3833}, 3413: {'l': 1607, 'r': 3463, 'u': 3659, 'd': 3877}, 1123: {'d': 2377, 'u': 1847, 'l': 3467, 'r': 1201}, 2551: {'d': 2287, 'r': 1171, 'u': 2897, 'l': 1061}, 3677: {'u': 1129, 'l': 3313, 'r': 3833}, 3659: {'u': 3413, 'r': 1171, 'l': 1741, 'd': 3517}, 1103: {'d': 2819, 'r': 3533, 'u': 3461, 'l': 3299}, 1361: {'r': 1091, 'u': 1019, 'd': 1447}, 3527: {'r': 2377, 'l': 2531, 'd': 3467, 'u': 2707}, 1823: {'l': 2531, 'r': 1193, 'd': 2707, 'u': 2699}, 1559: {'l': 3881, 'r': 3863, 'd': 1213, 'u': 2969}, 2161: {'u': 2999, 'd': 2423, 'r': 3019}, 2633: {'u': 1657, 'l': 2207, 'r': 1759}, 2593: {'r': 3089, 'l': 3863, 'd': 2969, 'u': 3221}, 2917: {'l': 2819, 'r': 2909, 'u': 3299}, 3881: {'l': 1559, 'd': 2411, 'r': 2083, 'u': 3019}, 1193: {'d': 1823, 'r': 2273, 'l': 2617, 'u': 3739}, 2467: {'d': 2287, 'r': 2953, 'u': 2221, 'l': 3301}, 2273: {'d': 3181, 'r': 1193, 'u': 2699, 'l': 3761}, 3191: {'d': 3583, 'u': 3533, 'r': 3461, 'l': 3011}, 2423: {'r': 3319, 'l': 2161, 'd': 1213}, 2719: {'d': 3671, 'r': 1181, 'l': 1373}, 3467: {'l': 1123, 'd': 3527, 'r': 1489, 'u': 1439}, 3461: {'d': 1657, 'l': 1103, 'u': 3191, 'r': 3203}, 1109: {'d': 1487, 'r': 1181}, 2953: {'d': 3463, 'l': 2467, 'u': 2677, 'r': 3877}, 2081: {'l': 1619, 'd': 2521, 'r': 2617, 'u': 3739}, 2141: {'d': 2287, 'l': 3301, 'r': 1061}, 1523: {'d': 3329, 'l': 3821, 'r': 3637}, 2411: {'r': 1619, 'l': 3881, 'd': 1789, 'u': 2969}, 1627: {'d': 2789, 'u': 1171, 'r': 3517, 'l': 2897}, 1489: {'d': 2531, 'r': 3467, 'l': 1697, 'u': 2549}, 2371: {'d': 3821, 'r': 1553, 'u': 1069}, 2221: {'l': 2749, 'd': 1997, 'u': 2467, 'r': 2677}, 2861: {'l': 3691, 'u': 1609, 'd': 1867}, 2707: {'u': 3673, 'r': 3527, 'd': 1823, 'l': 2617}, 2083: {'r': 2843, 'u': 3881, 'l': 1789, 'd': 2777}, 2621: {'r': 1619, 'l': 3089, 'd': 2969, 'u': 3739}, 1993: {'u': 1607, 'd': 2131, 'r': 1423, 'l': 1049}, 1439: {'l': 1847, 'd': 3467, 'u': 3229, 'r': 2549}, 3863: {'l': 3257, 'd': 3671, 'u': 1559, 'r': 2593}, 3203: {'l': 3967, 'd': 2789, 'r': 3583, 'u': 3461}, 2677: {'l': 3329, 'r': 2953, 'd': 2221, 'u': 1783}, 1069: {'u': 2557, 'r': 2999, 'l': 2371}, 1171: {'l': 3463, 'u': 2551, 'd': 3659, 'r': 1627}, 1049: {'l': 1249, 'd': 1993, 'r': 1789, 'u': 2777}, 2683: {'r': 3931, 'u': 1741, 'l': 3517, 'd': 2039}, 1213: {'d': 3257, 'r': 1559, 'l': 2423, 'u': 3019}, 1597: {'u': 2459, 'r': 2897, 'd': 1061}, 2909: {'d': 2917, 'l': 2207}, 1429: {'u': 1091, 'd': 2531, 'r': 2699, 'l': 1697}, 3877: {'u': 1249, 'l': 3413, 'd': 2953, 'r': 1783}, 1019: {'l': 3253, 'd': 1733, 'u': 1361}, 3637: {'l': 1997, 'u': 1523, 'd': 3371}, 3301: {'l': 2749, 'u': 2467, 'r': 2141}, 2459: {'r': 1597, 'l': 1759, 'u': 1747}, 1741: {'d': 1607, 'r': 1423, 'l': 3659, 'u': 2683}, 3019: {'r': 2843, 'u': 2161, 'd': 3881, 'l': 1213}, 1789: {'r': 2131, 'd': 2411, 'l': 2083, 'u': 1049}, 2207: {'u': 2633, 'd': 2909, 'l': 3299}, 1783: {'l': 3491, 'd': 3727, 'u': 2677, 'r': 3877}, 1609: {'d': 1693, 'u': 2861, 'l': 1667}, 3011: {'u': 1033, 'l': 3191, 'r': 1201, 'd': 1327}, 3517: {'r': 1879, 'l': 3659, 'd': 1627, 'u': 2683}, 2969: {'u': 1559, 'r': 2593, 'l': 2411, 'd': 2621}, 1487: {'l': 3319, 'r': 1109, 'u': 2441}, 1201: {'d': 2663, 'u': 1129, 'r': 1123, 'l': 3011}, 3371: {'l': 2543, 'u': 3637}, 1367: {'d': 3089, 'u': 1303, 'r': 1097, 'l': 3221}, 2699: {'d': 1823, 'l': 2273, 'r': 1429, 'u': 1601}, 3761: {'d': 3023, 'l': 1097, 'u': 2273, 'r': 1601}, 1697: {'d': 3253, 'r': 3691, 'u': 1489, 'l': 1429}, 3221: {'u': 3671, 'l': 2593, 'd': 1367, 'r': 1373}, 1181: {'r': 2719, 'l': 1109, 'u': 2441}, 2617: {'u': 1193, 'l': 2081, 'r': 2707, 'd': 3137}, 3739: {'r': 3181, 'd': 1193, 'l': 2081, 'u': 2621}, 1867: {'r': 2861, 'l': 3229, 'd': 2549}, 2777: {'u': 2557, 'r': 3727, 'l': 2083, 'd': 1049}, 2039: {'l': 1153, 'r': 1879, 'u': 2683, 'd': 1327}, 3229: {'d': 1439, 'l': 1867, 'r': 3313}, 1447: {'u': 3023, 'd': 1361, 'r': 1601}, 1601: {'d': 1091, 'r': 2699, 'u': 3761, 'l': 1447}, 2897: {'d': 2551, 'l': 1627, 'r': 1597, 'u': 1747}, 2549: {'d': 3691, 'l': 1489, 'u': 1439, 'r': 1867}, 1667: {'d': 3253, 'r': 3691, 'l': 1733, 'u': 1609}, 1327: {'u': 2663, 'd': 3583, 'r': 3011, 'l': 2039}, 3137: {'u': 2521, 'd': 3673, 'r': 3931, 'l': 2617}, 1759: {'l': 3967, 'd': 2633, 'u': 2459}, 1747: {'u': 3967, 'l': 2789, 'r': 2459, 'd': 2897}, 1373: {'d': 1303, 'u': 2719, 'l': 3221}, 3313: {'l': 1847, 'd': 3677, 'u': 3229}, 2441: {'d': 3257, 'r': 3671, 'l': 1487, 'u': 1181}, 3299: {'r': 1657, 'u': 1103, 'l': 2917, 'd': 2207}, 1061: {'u': 2551, 'l': 2141, 'r': 1597}, 3833: {'r': 3779, 'd': 1033, 'l': 3677}}
image = np.zeros((dim * (len(tiles[0]) - 2), dim * (len(tiles[0]) - 2)), dtype="<U1")

opposite = {"u": "d", "d": "u", "l": "r", "r": "l"}

def border(tile, d):
	if d == "u":
		return tile[0, :]
	if d == "d":
		return tile[-1, :]
	if d == "l":
		return tile[:, 0]
	if d == "r":
		return tile[:, -1]

skip = 0
for tile in list(neighbors.keys()):
	if len(neighbors[tile]) == 2:
		if skip > 0:
			skip -= 1
			continue
		corner = map_tile[tile]
		break
#print(corner, neighbors[corner])

right = "r"
up = "u"

# Check right
right_border = border(corner, right)
found = False
for tile in tiles:
	if any(corner.reshape(100, 1) != tile.reshape(100, 1)):
		for t in transforms[str(tile)]:
			if all(right_border == border(t, opposite[right])):
				found = True
				break
		if found:
			break
if not found:
	right = opposite[right]

# Check up
up_border = border(corner, up)
found = False
for tile in tiles:
	if any(corner.reshape(100, 1) != tile.reshape(100, 1)):
		for t in transforms[str(tile)]:
			if all(up_border == border(t, opposite[up])):
				found = True
				break
		if found:
			break
if not found:
	up = opposite[up]

#print(right, up)

def remove_from_list(tile):
	for i in range(len(tiles)):
		if np.array_equal(tiles[i], tile):
			tiles.pop(i)
			return

remove_from_list(corner)
current = corner
row_first = corner
if right == "r" and up == "d":
	for i in range(dim):
		for j in range(dim):
			for di in range(1, len(current) - 1):
				for dj in range(1, len(current) - 1):
					#print(len(current), i, j)
					image[(len(current) - 2)*i + di - 1, (len(current) - 2)*j + dj - 1] = current[di, dj]

			# Next tile:
			if j != dim - 1:
				found = False
				for tile in tiles:
					for t in transforms[str(tile)]:
						if all(border(current, right) == border(t, opposite[right])):
							current = t
							found = True
							remove_from_list(tile)
							break
					if found:
						break

		# Next row:
		if i != dim - 1:
			found = False
			for tile in tiles:
				for t in transforms[str(tile)]:
					if all(border(row_first, up) == border(t, opposite[up])):
						current = t
						row_first = current
						found = True
						remove_from_list(tile)
						break
				if found:
					break

elif right == "r" and up == "u":
	for i in range(dim)[::-1]:
		for j in range(dim):
			for di in range(1, len(current) - 1):
				for dj in range(1, len(current) - 1):
					#print(len(current), i, j)
					image[(len(current) - 2)*i + di - 1, (len(current) - 2)*j + dj - 1] = current[di, dj]

			# Next tile:
			if j != dim - 1:
				found = False
				for tile in tiles:
					for t in transforms[str(tile)]:
						if all(border(current, right) == border(t, opposite[right])):
							current = t
							found = True
							remove_from_list(tile)
							break
					if found:
						break

		# Next row:
		if i != 0:
			found = False
			for tile in tiles:
				for t in transforms[str(tile)]:
					if all(border(row_first, up) == border(t, opposite[up])):
						current = t
						row_first = current
						found = True
						remove_from_list(tile)
						break
				if found:
					break

elif right == "l" and up == "d":
	for i in range(dim):
		for j in range(dim)[::-1]:
			for di in range(1, len(current) - 1):
				for dj in range(1, len(current) - 1):
					#print(len(current), i, j)
					image[(len(current) - 2)*i + di - 1, (len(current) - 2)*j + dj - 1] = current[di, dj]

			# Next tile:
			if j != 0:
				found = False
				for tile in tiles:
					for t in transforms[str(tile)]:
						if all(border(current, right) == border(t, opposite[right])):
							current = t
							found = True
							remove_from_list(tile)
							break
					if found:
						break

		# Next row:
		if i != dim - 1:
			found = False
			for tile in tiles:
				for t in transforms[str(tile)]:
					if all(border(row_first, up) == border(t, opposite[up])):
						current = t
						row_first = current
						found = True
						remove_from_list(tile)
						break
				if found:
					break

elif right == "l" and up == "u":
	for i in range(dim)[::-1]:
		for j in range(dim)[::-1]:
			for di in range(1, len(current) - 1):
				for dj in range(1, len(current) - 1):
					#print(len(current), i, j)
					image[(len(current) - 2)*i + di - 1, (len(current) - 2)*j + dj - 1] = current[di, dj]

			# Next tile:
			if j != 0:
				found = False
				for tile in tiles:
					for t in transforms[str(tile)]:
						if all(border(current, right) == border(t, opposite[right])):
							current = t
							found = True
							remove_from_list(tile)
							break
					if found:
						break

		# Next row:
		if i != 0:
			found = False
			for tile in tiles:
				for t in transforms[str(tile)]:
					if all(border(row_first, up) == border(t, opposite[up])):
						current = t
						row_first = current
						found = True
						remove_from_list(tile)
						break
				if found:
					break


#print_tile(image)

# Monster haunter
monster = np.array(
	[list("                  # "),
	 list("#    ##    ##    ###"),
 	 list(" #  #  #  #  #  #   ")]
)

monsters = []
monsters.append(np.copy(monster))
monsters.append(np.flip(monster, axis=0))
monsters.append(np.flip(monster, axis=1))
monsters.append(np.flip(np.flip(monster, axis=0), axis=1))
monsters.append(np.rot90(monster))
monsters.append(np.flip(np.rot90(monster), axis=0))
monsters.append(np.flip(np.rot90(monster), axis=1))
monsters.append(np.flip(np.flip(np.rot90(monster), axis=0), axis=1))

n_monsters = 0
matched_shape = False
for m in monsters:
	for i in range(len(image) - len(m)):
		for j in range(len(image[0]) - len(m[0])):
			is_monster = True
			for di in range(len(m)):
				for dj in range(len(m[0])):
					#print(i + di, j + dj, di, dj, m[di][dj], image[i + di][j + dj])
					if m[di, dj] == "#" and image[i + di, j + dj] != "#":
						is_monster = False
						break
				if not is_monster:
					break
			if is_monster:
				matched_shape = True
				#print(m)
				n_monsters -=- 1
	if matched_shape:
		break

print(f"Monsters: {n_monsters}")
print(f"'#' not from monsters: {np.count_nonzero(np.array(image) == '#') - n_monsters * np.count_nonzero(monster == '#')}")
assert n_monsters == 43 and np.count_nonzero(np.array(image) == '#') - n_monsters * np.count_nonzero(monster == '#') == 2002
