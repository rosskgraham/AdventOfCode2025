from pathlib import Path

input_file = Path(__file__).parent / "puzzle_input.txt"

grid = [[c for c in r] for r in input_file.read_text().splitlines()]

offsets: list[tuple[int, int]] = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def in_grid(grid, row, col) -> bool:
    """Returns True if a row,col postion is within the extents of the grid."""
    height, width = len(grid), len(grid[0])
    return 0 <= row < height and 0 <= col < width


accessible_paper_rolls = 0
for row_num, row in enumerate(grid):
    for col_num, content in enumerate(row):
        if content == "@":
            adjacent_paper_rolls = 0
            for r, c in offsets:
                neighbour = row_num + r, col_num + c
                if in_grid(grid, nr := row_num + r, nc := col_num + c):
                    if grid[nr][nc] == "@":
                        adjacent_paper_rolls += 1
            if adjacent_paper_rolls < 4:
                accessible_paper_rolls += 1
print(f"Part 1: {accessible_paper_rolls}")

accessible_rolls = True
rolls_to_remove = []
while accessible_rolls:
    accessible_rolls = False
    for row_num, row in enumerate(grid):
        for col_num, content in enumerate(row):
            if content == "@":
                adjacent_paper_rolls = 0
                for r, c in offsets:
                    neighbour = row_num + r, col_num + c
                    if in_grid(grid, nr := row_num + r, nc := col_num + c):
                        if grid[nr][nc] == "@":
                            adjacent_paper_rolls += 1
                if adjacent_paper_rolls < 4:
                    accessible_paper_rolls += 1
                    accessible_rolls = True
                    rolls_to_remove.append((row_num, col_num))

    for r, c in rolls_to_remove:
        grid[r][c] = "."

print(f"Part 2: {len(rolls_to_remove)}")

# print("\n".join(["".join(r) for r in grid]))
# print("")
