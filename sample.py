n = int(input("Please insert n : "))

for i in range(1,n+1):
    if  (i/3).is_integer():
        print(i//3, end="")
    else :
        x = i//3
        if x > 0:
            print(f"[{x}] {i%3}/3", end="")
        else :
            print(f"{i%3}/3", end="")
    print(" " if i==n else ", ", end="")
