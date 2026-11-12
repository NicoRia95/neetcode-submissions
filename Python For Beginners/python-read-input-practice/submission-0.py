def add_two_numbers() -> int:
    line = input()
    numbers = line.split(",")
    total_sum = 0

    for s in numbers:
        total_sum += int(s)
    return total_sum



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
