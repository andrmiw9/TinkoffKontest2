# task 4, замена цифр в числах для увеличения суммы
# 5 2
# 1  2  1  3  5
# out: 16
n, k = map(int, input().split())

num = [int(x) for x in input().split()]
# print(num)
num.sort()
num.reverse()


# print(num)


def count_digits(number) -> int:
    count = 0
    while number > 0:
        count = count + 1
        number //= 10
    return count


def max_inc_in_num(number) -> int:
    maxim = -1
    count = 0  # also degree
    max_delta = -1
    while number > 0:
        maxim = (number % 10) * (10 ** count)
        count += 1
        delta = (10 ** count - 10 ** (count - 1)) - maxim
        if delta > max_delta:
            max_delta = delta

        number //= 10

    return max_delta


def find_max_delta() -> None:
    maxim_ = 0
    ind = -1
    for j in range(len(num)):
        rr = max_inc_in_num(num[j])
        if rr > maxim_:
            maxim_ = rr
            ind = j
    return maxim_, ind


# цикл пока есть замены:
# найти самый выгодный вариант замены
# выполнить замену

# print(max_inc_in_num(12))
# print(max_inc_in_num(512))
# print(max_inc_in_num(6))

global_delta = 0
for i in range(k):
    if num:
        res = find_max_delta()
    else:
        break
    if not res:
        break
    num[res[1]] += res[0]
    global_delta += res[0]

# print('final num:', num)
# print('delta:', global_delta)
print(global_delta)

# 2 10
# 912 994
