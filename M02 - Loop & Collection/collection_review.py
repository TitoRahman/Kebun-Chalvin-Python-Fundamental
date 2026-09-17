# COLLECTION - DATA TYPE THAT CAN HOLD MORE THAN ONE ITEM
# TYPE OF COLLECTION :
# 1. LIST -> [...]
# 2. TUPLE -> (...) -> SAME LIKE LIST BUT NOT DYNAMIC AND VALUE IS FIXED
# 3. SET -> {...} -> COLLECTION THAT DOESN'T HAVE DUPLICATE VALUE
# 4. STRING -> "..." -> STRING IS USED TO STORE MULTIPLE CHARACTERS
# 5. DICTIONARY -> {[key]:[value]}
# [10, 15, 20, 30] # INDEX IS THE LOCATION OF EACH ITEM INSIDE A COLLECTION START FROM 0
#   0   1   2   3
#  -4  -3  -2  -1

list_n = list()
list_n_2 = []
list_n_3 = [1,2,3,4]

# FUNCTION IN LIST
list_n.append(10) # FUNCTION TO PUSH AN ITEM TO THE BACK OF THE LIST
list_n.append(15)
list_n.append(20)
list_n.append(30)
print(list_n)

list_n.insert(0, 80) # FUNCTION TO ADD A VALUE TO ANY INDEX
print(list_n)

list_n.pop() # REMOVE THE LAST ITEM FROM A COLLECTION
list_n.pop(1)
print(list_n)

removed = list_n.pop()

print(f"Removing {removed} from {list_n}")
print(list_n)

list_n.append(80) # [80, 15, 80]

list_n = list(set(list_n))
print(list_n)
list_n.append(15) # [80, 15, 15]

list_n.extend(list_n_3)
print(list_n)

index_of_value = list_n.index(15)
print(index_of_value)

print(list_n.count(15))

list_n.sort(reverse=True)
print(list_n)

# list_n.remove(80) # [15, 80]
# print(list_n)

print(f"index 5 of the list is {list_n[5]}")

list_n[0] = 100
print(list_n)


tuple_a = ("a", "b", "c")
print(tuple_a[0])


str_name = "John-Doe"
print(str_name[2:4]) # [ start : stop : step ] # [ 0 : end of collection : 1]
print(str_name[0:4])
print(str_name[::2])
print(str_name[::-1])

print(str_name.upper())
print(str_name.lower())

phone_number = input("Enter your phone number: ").strip()
print(phone_number)

if phone_number.isdigit():
    print("You have entered a valid phone number")
else :
    print("You have entered an invalid phone number")

print(f"the length of the phone number is {len(phone_number)}")