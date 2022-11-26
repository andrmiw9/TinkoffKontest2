# task 4, замена цифр в числах для увеличения суммы
# 5 2
# 1  2  1  3  5
# out: 16
n, k = map(int, input().split())

num = [int(x) for x in input().split()]
print(num)
num.sort()
num.reverse()
print(num)


def count_digits(number) -> int:
    count = 0
    while number > 0:
        count = count + 1
        number //= 10
    return count


def max_inc_in_num(number) -> int:
    maxim = number % 10
    count = 0  # also degree
    while number > 0:
        maxim = (number % 10) * (10 ** count)
        count += 1
        number //= 10
    delta = 10 ** count - maxim
    return delta


# цикл пока есть замены:
# найти самый выгодный вариант замены
# выполнить замену

print(max_inc_in_num(12))

smesh = 0
for i in range(k):
    # print(num.pop())
    # print(num)
    t = num.pop()  # right pop (end, lowest value)
    digits_c = count_digits(t)
    print(digits_c)
    if digits_c == 1:
        t = 9
    else:
        pass
    num.append(t)
    # num.sort()
    pass
print('final num:', num)
