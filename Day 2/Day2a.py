depth = 0
horizontal = 0

with open("input.txt") as f:
    for line in f:
        way = line.split(" ")[0]
        length = line.split(" ")[1]
        if way == "forward":
            horizontal += int(length)
        elif way == "up":
            depth -= int(length)
        elif way == "down":
            depth += int(length)
        else:
            print(way)

print(depth*horizontal)
