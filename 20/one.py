# --- Arvent of core 2020: Day 20 ---

# (File automatically generater by aocTool, reveloper by B0lu, 2020.)

import numpy as np

cameras = open("input.txt").read().split("\n\n")[:-1]
tiles = [np.array(list(map(list, l.splitlines()[1:]))) for l in cameras]
IDs = [int(l.splitlines()[0].split(" ")[-1][:-1]) for l in cameras]

#[print(t.shape) for t in tiles]

tile_map = {str(tiles[i]): IDs[i] for i in range(len(IDs))}
neighbors = {ID: {} for ID in IDs}
reverse = {}

for tile1 in tiles:
	for tile2 in tiles:
		if any(tile1.reshape(100, 1) != tile2.reshape(100, 1)):
			if all(tile1[0, :] == tile2[-1, :]):
				neighbors[tile_map[str(tile1)]]["l"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == tile2[0, :]):
				neighbors[tile_map[str(tile1)]]["r"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == tile2[:, -1]):
				neighbors[tile_map[str(tile1)]]["u"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == tile2[:, 0]):
				neighbors[tile_map[str(tile1)]]["d"] = tile_map[str(tile2)]

			elif all(tile1[0, :] == np.flip(tile2[0, :])):
				neighbors[tile_map[str(tile1)]]["rl"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == np.flip(tile2[-1, :])):
				neighbors[tile_map[str(tile1)]]["rr"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == np.flip(tile2[:, 0])):
				neighbors[tile_map[str(tile1)]]["ru"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == np.flip(tile2[:, -1])):
				neighbors[tile_map[str(tile1)]]["rd"] = tile_map[str(tile2)]

			elif all(tile1[0, :] == tile2[:, -1]):
				neighbors[tile_map[str(tile1)]]["tl"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == tile2[:, 0]):
				neighbors[tile_map[str(tile1)]]["tr"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == tile2[0, :]):
				neighbors[tile_map[str(tile1)]]["tu"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == tile2[-1, :]):
				neighbors[tile_map[str(tile1)]]["td"] = tile_map[str(tile2)]

			elif all(tile1[0, :] == np.flip(tile2[:, 0])):
				neighbors[tile_map[str(tile1)]]["rtl"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == np.flip(tile2[:, -1])):
				neighbors[tile_map[str(tile1)]]["rtr"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == np.flip(tile2[0, :])):
				neighbors[tile_map[str(tile1)]]["rtu"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == np.flip(tile2[-1, :])):
				neighbors[tile_map[str(tile1)]]["rtd"] = tile_map[str(tile2)]

			elif all(tile1[0, :] == tile2[0, :]):
				neighbors[tile_map[str(tile1)]]["fl"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == tile2[-1, :]):
				neighbors[tile_map[str(tile1)]]["fr"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == tile2[:, 0]):
				neighbors[tile_map[str(tile1)]]["fu"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == tile2[:, -1]):
				neighbors[tile_map[str(tile1)]]["fd"] = tile_map[str(tile2)]

			elif all(tile1[0, :] == np.flip(tile2[-1, :])):
				neighbors[tile_map[str(tile1)]]["frl"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == np.flip(tile2[0, :])):
				neighbors[tile_map[str(tile1)]]["frr"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == np.flip(tile2[:, -1])):
				neighbors[tile_map[str(tile1)]]["fru"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == np.flip(tile2[:, 0])):
				neighbors[tile_map[str(tile1)]]["frd"] = tile_map[str(tile2)]

			elif all(tile1[0, :] == tile2[:, 0]):
				neighbors[tile_map[str(tile1)]]["ftl"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == tile2[:, -1]):
				neighbors[tile_map[str(tile1)]]["ftr"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == tile2[-1, :]):
				neighbors[tile_map[str(tile1)]]["ftu"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == tile2[0, :]):
				neighbors[tile_map[str(tile1)]]["ftd"] = tile_map[str(tile2)]

			elif all(tile1[0, :] == np.flip(tile2[:, -1])):
				neighbors[tile_map[str(tile1)]]["frtl"] = tile_map[str(tile2)]
			elif all(tile1[-1, :] == np.flip(tile2[:, 0])):
				neighbors[tile_map[str(tile1)]]["frtr"] = tile_map[str(tile2)]
			elif all(tile1[:, 0] == np.flip(tile2[-1, :])):
				neighbors[tile_map[str(tile1)]]["frtu"] = tile_map[str(tile2)]
			elif all(tile1[:, -1] == np.flip(tile2[0, :])):
				neighbors[tile_map[str(tile1)]]["frtd"] = tile_map[str(tile2)]

#print(neighbors)

prod = 1
for tile in neighbors:
	if len(neighbors[tile]) == 2:
		#print(tile)
		prod *= tile

print(f"Product of corners: {prod}")
assert prod == 18411576553343
