import numpy as np

cameras = open("input.txt").read().split("\n\n")[:-1]
tiles = [np.array(list(map(list, l.splitlines()[1:]))) for l in cameras]
IDs = [int(l.splitlines()[0].split(" ")[-1][:-1]) for l in cameras]

tile_map = {str(tiles[i]): IDs[i] for i in range(len(IDs))}
map_tile = {tile_map[str(tile)]: tile for tile in tiles}

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

	transforms[str(tile)].append(np.flip(np.flip(tile, axis=0), axis=1))
	transforms[str(tile)].append(np.rot90(np.flip(np.flip(tile, axis=0), axis=1), 1))
	transforms[str(tile)].append(np.rot90(np.flip(np.flip(tile, axis=0), axis=1), 2))
	transforms[str(tile)].append(np.rot90(np.flip(np.flip(tile, axis=0), axis=1), 3))

from os import system

while True:
	tile = map_tile[int(input("Tile number: "))]

	system("clear")
	for t in transforms[str(tile)]:
		s = ""
		for i in range(len(t)):
			for j in range(len(t)):
				s += t[i, j]
			s += "\n"
		print(s)
		print()
