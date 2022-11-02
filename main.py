with open(file='data.txt') as file:
    data = [int(val) for val in file.read().split("\n")]


def part_one(measurements):
    output = 0
    previous_number = measurements[0]
    for curr_number in measurements:
        if curr_number > previous_number:
            output += 1

        previous_number = curr_number
    
    return print(output)


def part_two(measurements):
    output = 0
    start = 0  # start of window
    previous_sum = sum(measurements[:3])
    for end, val in enumerate(measurements):  # end = end of window
        if end - start + 1 == 3:
            curr_sum = sum(measurements[start:end+1])
            if curr_sum > previous_sum:
                output += 1

            start += 1
            previous_sum = curr_sum

    return print(output)


part_one(data)
part_two(data)
