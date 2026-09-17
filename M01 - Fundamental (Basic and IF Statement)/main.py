# VARIABLE - USED TO STORE AN ITEM/MORE THAN ONE ITEM
# DATA TYPE :
# 1. INTEGER (int) - 1, 0, -1
# 2. FLOAT - 1.1, 1.0
# 3. BOOLEAN (bool) - TRUE/FALSE
# 4. STRING (str) - "WORD", "1"
# X = 1
# first_name = "John"
# age : int = 18
# birth_year = 2026 - age
# print("My first name is :", first_name,"age",birth_year, sep=" ")
# print(f"My first name is : {first_name} and age {2026 - age} years old")
n = 8
if n > 0:
    print("Pos")
elif n == 0:
    print("Zero")
elif n < 0:
    print("Negative")
else :
    print("Invalid!")

if (
        n%2 == 0 and
        n > 0
) : # TRUE and TRUE // TRUE
    print("Even")

j = int(input())
