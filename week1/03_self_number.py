non_self = []
for i in range(1, 10000):
    part_num = list(map(int, str(i)))
    new_num = i + sum(part_num)
    non_self.append(new_num)
    if i in non_self:
        continue
    else:
        print(i)


