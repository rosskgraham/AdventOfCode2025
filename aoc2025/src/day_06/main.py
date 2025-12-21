from pathlib import Path

puzzle_input = (Path(__file__).parent / "puzzle_input.txt").read_text().splitlines()

problems = [line.split() for line in puzzle_input]

# part 1
transposed = list(zip(*problems))

grand_total = 0
for problem in transposed:
    operator = problem[-1]
    numbers = [int(n) for n in problem[:-1]]
    if operator == "+":
        tot = 0
        for num in numbers:
            tot += num
    elif operator == "*":
        tot = 1
        for num in numbers:
            tot *= num
    grand_total += tot
print(grand_total)

# part 2
# tranpose grid characters instead of whole numbers

numbers = [[c for c in line] for line in puzzle_input[:-1]]
operators = [c for c in puzzle_input[-1] if c != " "]
transposed = ["".join(n).strip() for n in list(zip(*numbers))]
grand_total = 0

number_group_index = 0
number_groups = [[] for _ in range(len(operators))]
for n in transposed:
    if n != "":
        number_groups[number_group_index].append(int(n))
    else:
        number_group_index += 1

for ix, numbers in enumerate(number_groups):
    operator = operators[ix]
    if operator == "+":
        tot = 0
        for num in numbers:
            tot += num
    elif operator == "*":
        tot = 1
        for num in numbers:
            tot *= num
    grand_total += tot
print(grand_total)
