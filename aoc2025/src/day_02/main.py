from pydantic import BaseModel


class IdRange(BaseModel):
    first: int
    last: int

    @classmethod
    def from_string(cls, s: str):
        first, last = s.split("-")
        return cls(first=int(first), last=int(last))

    def ids(self):
        return (x for x in range(self.first, self.last + 1))

    def invalid_ids_part1(self):
        return (
            x
            for x in range(self.first, self.last + 1)
            if len(str(x)) % 2 == 0
            and int(f"{str(x)[:len(str(x))//2]}{str(x)[:len(str(x))//2]}") == x
        )

    def invalid_ids_part2(self):
        a = {
            2: [1],
            3: [1],
            4: [1, 2],
            5: [1],
            6: [1, 2, 3],
            7: [1],
            8: [1, 2, 4],
            9: [1, 3],
            10: [1, 2, 5],
        }
        for pattern_lengths in a[len(str(self.))]
        for i in range(1, (len(str(self.last)) // 2) + 1):
            print(i)
        return []


puzzle_input = "12077-25471,4343258-4520548,53-81,43661-93348,6077-11830,2121124544-2121279534,631383-666113,5204516-5270916,411268-591930,783-1147,7575717634-7575795422,8613757494-8613800013,4-19,573518173-573624458,134794-312366,18345305-18402485,109442-132958,59361146-59451093,1171-2793,736409-927243,27424-41933,93-216,22119318-22282041,2854-4778,318142-398442,9477235089-9477417488,679497-734823,28-49,968753-1053291,267179606-267355722,326-780,1533294120-1533349219"
sample_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

id_ranges = [IdRange.from_string(rng) for rng in sample_input.split(",")]

# print(id_ranges)
id_sum = 0
for id_range in id_ranges:
    for id in id_range.invalid_ids_part1():
        # print(id)
        id_sum += id

print(f"Part 1: {id_sum}")

id_sum = 0
for id_range in id_ranges:
    print(id_range)
    for id in id_range.invalid_ids_part2():
        # print(id)
        id_sum += id

print(f"Part 2: {id_sum}")
