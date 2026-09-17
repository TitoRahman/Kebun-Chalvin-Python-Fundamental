# LOOP - REPEATING A SEQUENCE OR A SET OF AN INSTRUCTION
# FOR - WE ALREADY WHEN WILL IT STOP
# WHILE - WE DONNO WHEN WILL IT STOP

# for [loop variable] in [collection]
# n = int(input("Enter a number: "))
# for i in range(1,n,2):
#     print(i)

list_n = [80,20, 30, 100]

for i in range(0, len(list_n)): # range(0, 4, 1)
    print(f"current index is {i} : {list_n[i]}")
    if list_n[i] % 30 == 0:
        continue
    if list_n[i] == 20:
        print("Twenty")
        break
    else :
        print(list_n[i])

print("==========")
for i in list_n:
    print(i)

x = True
while x:
    print("STILL LOOPING")
    stop = input("y to stop : ")
    if stop == "y":
        break



