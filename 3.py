# lifts

n, t = map(int, input().split())
sotr = input().split()
sotr = [int(x) for x in sotr]
leaven = int(input())
root = sotr[leaven - 1]


# print(root)


def counter(seq: list) -> int:
    counter = 0
    for i in range(len(seq) - 1):
        counter += abs(seq[i] - seq[i + 1])
    return counter


def gen(root) -> []:
    if root == sotr[0]:
        return sotr
    elif root == sotr[-1]:  # проверка на существование поддеревьев
        return reversed(sotr)
    else:  # на этом моменте у нас точно 2 поддерева
        exp1 = abs(root - sotr[0])  # левое
        exp2 = abs(root - sotr[-1])  # правое
        if t > exp1:  # если покрывает всё левое поддерево, то имеет смысл идти, иначе нет
            return sotr
        elif t > exp2:
            return reversed(sotr)
        else:  # если не покрывает ни одно поддерево, то идём сначала в корень, потом в сторону меньшего поддерева
            # (тк двойной путь (туда и обратно) в этом случае будет меньше)
            outp = []
            outp.append(root)
            if exp1 <= exp2:  # левое меньше или = правому
                outp.extend(reversed(sotr[:leaven - 1]))

                outp.extend(sotr)
            else:  # правое меньше
                outp.extend(sotr[leaven:])

                outp.extend(sotr[::-1])
            return outp


res = gen(root)
# print(*res)
print(counter(res))
