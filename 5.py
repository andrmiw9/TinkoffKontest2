# Sasha's tests
# l, r = map(int, input().split())


def count_digits(number) -> int:
    count = 0
    while number > 0:
        count = count + 1
        number //= 10
    return count


def check_digs_4_identity(number) -> bool:
    if len(set(str(number))) == 1:
        return True
    else:
        return False


# big_list = [x for x in range(abs(l), abs(r + 1)) if check_digs_4_identity(x)]
# print(len(big_list))

# v2

l, r = map(int, input().split())

big_l = []
for k in range(1, 10):
    x = 0
    while 10 * x + k < r + 1:
        x = 10 * x + k
        big_l.append(x)
        pass
big_l = [x for x in big_l if x > l - 1]
print(len(big_l))
