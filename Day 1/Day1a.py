num_of_increases = 0

with open("input.txt") as f:
    pre_line = 50000
    for line in f:
        if line > pre_line:
            num_of_increases += 1
        pre_line = line

print(num_of_increases)