from itertools import combinations
from pathlib import Path

example_input = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

puzzle_input = (Path(__file__).parent / "puzzle_input.txt").read_text()
lines = puzzle_input.splitlines()
red_tiles = [[int(c) for c in t.split(",")] for t in lines]

print(red_tiles)


def area_of_rectangle(t1, t2) -> int:
    x = abs(t1[0] - t2[0]) + 1
    y = abs(t1[1] - t2[1]) + 1
    ...
    return x * y

max_area = 0
for tiles in combinations(red_tiles, 2):

    area = area_of_rectangle(*tiles)
    if area > max_area:
        max_area = area
    ...
print(f"Part 1: {max_area}")