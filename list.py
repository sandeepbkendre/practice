numbers = [10, 20, 35, 40, 55, 60, 75]

def minimum():
    minimum_number = numbers[0]
    for number in numbers:
        if minimum_number < number:
            minimum_number = number
    return minimum_number

def maximum():
    maximum_number = numbers[0]
    for number in numbers:
        if maximum_number > number:
            maximum_number = number
    return maximum_number


def mean():
    count = 0
    sum_numbers = 0
    for number in numbers:
        sum_numbers += number
        count += 1
    return sum_numbers / count

def median():
    count = 0
    for number in numbers:
        count += 1
    return numbers[int(count / 2)]

print(minimum())
print(maximum())
print(mean())
print(median())
