verifyNumber = [0]*9
# [1,1,0,0,0,1,0,0,0,0]
phoneNumber = input()

for i in range(0, len(phoneNumber)):
    if phoneNumber[i].isdigit():
        verifyNumber[i] = 1

print(verifyNumber.count(0))

for i in range(9):
    if verifyNumber[i] == 0:
        print(i, end= " ")


