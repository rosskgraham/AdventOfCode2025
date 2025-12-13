from pathlib import Path

example = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

puzzle_input = (Path(__file__).parent / "puzzle_input.txt").read_text()


def move_dial(start_position: int, direction: str, distance: int) -> tuple[int, int]:
    dial_position = start_position
    zeroes = 0
    for _ in range(distance):
        if direction == "R":
            dial_position+=1
            if dial_position == 100:
                dial_position = 0
        elif direction == "L":
            dial_position-=1
            if dial_position == -1:
                dial_position = 99
        if dial_position == 0:
            zeroes += 1
    return dial_position, zeroes


def main():
    dial_position = 50
    moves = [(move[0], int(move[1:])) for move in puzzle_input.splitlines()]
    dial_stop_on_zero = 0
    dial_click_on_zero = 0
    for direction, distance in moves:
        dial_position, clicks_on_zero = move_dial(dial_position, direction, distance)
        dial_click_on_zero+= clicks_on_zero
        if dial_position == 0:
            dial_stop_on_zero += 1
    print(f"{dial_stop_on_zero=}")
    print(f"{dial_click_on_zero=}")


if __name__ == "__main__":
    main()
