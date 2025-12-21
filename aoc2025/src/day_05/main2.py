from itertools import combinations
from pathlib import Path

puzzle_input = (Path(__file__).parent / "puzzle_input.txt").read_text()
id_ranges, _ = puzzle_input.split("\n\n")

id_ranges = [[int(n) for n in r.split("-")] for r in id_ranges.splitlines()]


def ranges_overlap(r1, r2) -> bool:
    overlaps = r1[0] <= r2[1] and r1[1] >= r2[0]
    #print(f"{r1}, {r2}{' overlaps' if overlaps else ''}")
    return r1[0] <= r2[1] and r1[1] >= r2[0]

def compact_ranges(id_ranges:list[list[int]], r1, r2) -> list[int]:
    #print(f"Compacting {r1}, {r2} = {[min(r1[0], r2[0]), max(r1[1], r2[1])]}")
    id_ranges.pop(id_ranges.index(r1))
    id_ranges.pop(id_ranges.index(r2))
    new_range = [min(r1[0], r2[0]), max(r1[1], r2[1])]
    id_ranges.append(new_range)
    return id_ranges

# Compact ranges which overlap or are contained by other ranges
compacting = True
while compacting:
    for range_pair in combinations(id_ranges, 2):
        r1, r2 = range_pair
        if ranges_overlap(r1, r2):
            id_ranges = compact_ranges(id_ranges,r1, r2)
            break
    else:
        compacting = False

# Count all IDs in compacted non overlapping ranges
fresh_ids = 0
for r2 in id_ranges:
    fresh_ids += r2[1] - r2[0] + 1
print(f"Part 2: Fresh ID Count = {fresh_ids}")

