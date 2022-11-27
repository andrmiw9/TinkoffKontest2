tt = (1, 2, (30, 40))
print(hash(tt))
tl = (1, 2, [30, 40])
# print(hash(tl))   # ERROR

a = dict()
a[1] = 'one'
a[tt] = 'second'
# a[tl] = 'third'   # ERROR
