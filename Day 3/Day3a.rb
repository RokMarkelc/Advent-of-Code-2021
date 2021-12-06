
input_file = "input.txt"

def most_common_bits(file)
    array = Array.new(12, 0)
    IO.foreach(file) do |line|
        for i in 0..11
            if line[i] == "1"
                array[i] += 1
            else
                array[i] -= 1
            end
        end
    end
    return array
end

gamma_array = most_common_bits(input_file)
gamma = ""
epsilon = ""

for x in gamma_array
    if x > 0
        gamma += "1"
        epsilon += "0"
    else
        gamma += "0"
        epsilon += "1"
    end
end

puts gamma.to_i(2) * epsilon.to_i(2)