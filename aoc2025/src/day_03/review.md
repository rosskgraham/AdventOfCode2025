# Day 3 Solution Review

## Overview
Your solution works and produces the correct answer, but there are several areas for improvement in terms of efficiency, correctness, and code quality.

## Issues Identified

### 1. Part 1 - Inefficient O(n²) Approach
**Current approach**: You're checking all pairs of batteries with nested loops.

**Problem**: This is unnecessarily slow for large inputs.

**Better approach**: Use a greedy O(n) algorithm:
- Find the leftmost maximum digit
- Then find the maximum digit to the right of it
- This guarantees the largest 2-digit number while maintaining order

### 2. Part 2 - Algorithm Correctness Concerns
**Current approach**: Your algorithm tries to iteratively swap/remove elements by moving larger digits left.

**Problem**: While it may work for your specific input, this approach doesn't guarantee the optimal solution for all cases. The algorithm doesn't have a clear termination proof and might fail on edge cases.

**Better approach**: Use the standard "select k items from n to maximize number" greedy algorithm:

For each position `i` in your k-digit result (where k=12):
1. You need `k - i` total digits remaining (including current position)
2. Calculate the search window: you can look at the leftmost `n - k + i + 1` digits from your current position
3. Pick the maximum digit from that window
4. Continue from the position immediately after the selected digit

This guarantees optimality because:
- You maximize from left to right (most significant digits first)
- The window calculation ensures you always have enough digits remaining
- It's a proven greedy algorithm for this class of problems

**Example**: For "987654321111111" (15 digits), selecting 12:
- Position 0: Can search first 4 digits (15-12+0+1=4), pick '9' at index 0
- Position 1: Can search first 4 of remaining, pick '8' at index 1
- Continue this process...

### 3. Function Signature Bug
**Issue**: `get_max_joltage_part_one(bank: list[int])` takes a parameter `bank` but immediately loops over the global `banks` variable, completely ignoring the parameter.

**Fix**: Either remove the unused parameter or refactor to process a single bank and call it from a loop.

### 4. Repeated Code Pattern
Both functions loop over `banks` and convert strings to digit lists. This could be extracted to reduce duplication.

## Recommended Refactoring

```python
def get_max_two_digit_joltage(bank: str) -> int:
    """Find maximum 2-digit number from bank maintaining order."""
    digits = [int(d) for d in bank]
    n = len(digits)
    max_joltage = 0
    
    for i in range(n - 1):
        # For each starting digit, find max digit after it
        remaining_max = max(digits[i+1:])
        joltage = digits[i] * 10 + remaining_max
        max_joltage = max(max_joltage, joltage)
    
    return max_joltage

def get_max_k_digit_joltage(bank: str, k: int) -> int:
    """Find maximum k-digit number from bank maintaining order."""
    digits = [int(d) for d in bank]
    n = len(digits)
    
    if n == k:
        return int(bank)
    
    result = []
    start = 0
    
    for i in range(k):
        # Calculate how many positions we can search
        remaining_needed = k - i
        search_end = n - remaining_needed + 1
        
        # Find max digit in valid window
        max_digit = max(digits[start:search_end])
        max_idx = digits.index(max_digit, start)
        
        result.append(max_digit)
        start = max_idx + 1
    
    return int(''.join(map(str, result)))

def solve():
    input_file = Path(__file__).parent / "puzzle_input.txt"
    banks = input_file.read_text().splitlines()
    
    part1 = sum(get_max_two_digit_joltage(bank) for bank in banks)
    part2 = sum(get_max_k_digit_joltage(bank, 12) for bank in banks)
    
    print(f"Total output joltage part 1: {part1}")
    print(f"Total output joltage part 2: {part2}")
```

## Summary
- **Part 1**: Can be optimized from O(n²) to O(n²) in worst case but with better average performance using greedy selection
- **Part 2**: Current algorithm works but lacks theoretical soundness; use proven greedy algorithm
- **Code quality**: Fix parameter usage, reduce duplication, improve clarity
- **Correctness**: While your solution works for the given input, the Part 2 algorithm may fail on edge cases
