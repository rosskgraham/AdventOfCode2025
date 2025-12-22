from pathlib import Path

puzzle_input = (Path(__file__).parent / "example_input.txt").read_text().splitlines()
lights = [
    {
        "lights": [1 if l == "#" else 0 for l in j[0] if l not in ["[", "]"]],
        "buttons": [[int(c) for c in l[1:-1].split(",")] for l in j[1:-1]],
        "joltage": [],
    }
    for j in [i.split() for i in puzzle_input]
]

for line in lights:
    print(line)
