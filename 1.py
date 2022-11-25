# доплата за тариф
a, b, c, d = map(int, input().split())

if d <= b:
    print(a)
else:
    print(a + c * (d - b))
