enter = 26


def plus_cycle(value):
    count = 1
    numbers = list(map(int,str(value)))
    number_sum = sum(numbers) % 10
    new_num = (numbers[1] * 10) + number_sum
    while value != new_num:
        numbers = list(map(int, str(new_num)))
        number_sum = sum(numbers) % 10
        new_num = (numbers[1] * 10) + number_sum
        count += 1
    return count

result = plus_cycle(enter)
print(result)
