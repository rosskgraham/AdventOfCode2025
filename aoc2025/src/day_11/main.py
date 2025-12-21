from pathlib import Path

puzzle_input = [d.split(": ") for d in """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out""".splitlines()]



#puzzle_input = [d.split(": ") for d in (Path(__file__).parent / "puzzle_input.txt").read_text().splitlines()]

p = {device[0]: device[1].split() for device in puzzle_input}
stack = ["you"]
ways_out = 0

while stack:
    current_device = stack.pop()
    if current_device == "out":
        ways_out += 1
    else:
        stack.extend(p.get(current_device))
    print(stack)
print(ways_out)

# part 2
puzzle_input = [d.split(": ") for d in """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out""".splitlines()]
p = {device[0]: device[1].split() for device in puzzle_input}

stack = ["svr"]
ways_out = 0

while stack:
    current_device = stack.pop()
    #print(current_device)
    if current_device == "out":
        print(stack)
        if "dac" in stack and "fft" in stack:
            ways_out += 1
            print(ways_out)
        else:
            print("dac and fft not in stack")
    else:
        stack.extend(p.get(current_device))
    #print(stack)
print(ways_out)