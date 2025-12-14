from pathlib import Path

input_file = Path(__file__).parent / "puzzle_input.txt"
banks = input_file.read_text().splitlines()


def get_max_joltage_part_one(bank: list[int]) -> int:
    total_output_joltage = 0
    for bank in banks:
        bank = [int(b) for b in bank]
        bank_length = len(bank)
        max_joltage = 0
        for batt1 in range(bank_length - 1):
            for batt2 in range(batt1 + 1, bank_length):
                if (joltage := (int(f"{bank[batt1]}{bank[batt2]}"))) > max_joltage:
                    max_joltage = joltage
        total_output_joltage += max_joltage
    return total_output_joltage


def get_max_joltage_part_two(bank: list[int]) -> int:
    total_output_joltage = 0
    for bank in banks:
        bank_list = [int(x) for x in bank]

        # Move more significant batteries to the left
        processing = True
        while processing and len(bank_list) > 12:
            for ix, pair in enumerate(zip(bank_list, bank_list[1:])):
                left, right = pair
                if left < right:
                    bank_list.pop(ix)
                    break
            else:
                processing = False

        # Remove least significant batteries from the right
        processing = True
        while processing and len(bank_list) > 12:
            for e in list(enumerate(zip(bank_list, bank_list[1:])))[::-1]:
                ix, pair = e
                left, right = pair
                if left >= right:
                    bank_list.pop(ix + 1)
                    break
            else:
                processing = False

        total_output_joltage += int("".join([str(x) for x in bank_list]))
    return total_output_joltage


print(f"Total output joltage part 1: {get_max_joltage_part_one(banks)}")


print(f"Total output joltage part 2: {get_max_joltage_part_two(banks)}")
