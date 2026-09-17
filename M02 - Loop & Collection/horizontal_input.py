n = list(map(int, input().split())) # '5' -> 5
# print(n)
# x = int(n[0])
# y = int(n[1])
# print(n)
# print(x, y)

for i in range(n[0],  n[1]*n[0], n[0]): # 5 10 15 20 25 30
    print(i)