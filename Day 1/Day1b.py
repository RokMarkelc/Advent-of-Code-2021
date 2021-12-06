num_of_increases = 0

with open("input.txt") as f:
    contents = f.readlines()
    sums = []
    for i in range(2, len(contents)):
        sums.append(int(contents[i])+int(contents[i-1])+int(contents[i-2])) 
    pre_sum = 50000
    for sum in sums:
        if sum > pre_sum: num_of_increases += 1
        pre_sum = sum
    
print(num_of_increases)