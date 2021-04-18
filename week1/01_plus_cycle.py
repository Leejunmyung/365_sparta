enter = 26


def plus_cycle(value):
    count = 1
    left_num = value // 10
    right_num = value % 10
    plus_right_num = (left_num + right_num) % 10
    new_num = (right_num * 10) + plus_right_num
    while value != new_num:
        left_num = new_num // 10
        right_num = new_num % 10
        plus_right_num = (left_num + right_num) % 10
        new_num = (right_num * 10) + plus_right_num
        count += 1
        if value == new_num:
            return count

result = plus_cycle(enter)
print(result)
