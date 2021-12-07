with open("input_day2.txt", "r") as f:
    line = f.readlines()

horizontal = 0
depth = 0
aim = 0

def extract(line):
    for c in line:
        if c.isdigit():
            return int(c)


for line in line:
    buffer = extract(line)
    if line.find("forward") != -1:
        horizontal += buffer
        depth += aim * buffer

    elif line.find("down") != -1:
        aim += buffer
    elif line.find("up") != -1:
        aim -= buffer

print(depth * horizontal)
