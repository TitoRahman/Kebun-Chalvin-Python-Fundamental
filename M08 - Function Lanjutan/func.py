# FUNCTION -> RECYCLE CODE
# *args > Memberikan argument lebih dari parameter yang ada
#
# FUNCTION UNWRITTEN RULE
# 1. function selalu diatas dari semua code/global scope code
# 2. wajib dibawah import
# 3. Semua yang ada di function tidak bisa keluar dari function
# 4. penamaan function usahakan tidak menimpa function lain kecuali dibutuhkan
import math

def sum_list(*numbers): # *args akan menerima/memiliki tipe data tuple
    tot = 0
    numbers = list(numbers) # convert tuple > list
    for num in numbers:
        tot += num
    return tot

def myFunc(param, *args, **kwargs):
    print(param, args, kwargs)

myFunc(
    "Nepnep",
    1,2,3,4,
    name="drey"
)

result = sum_list(1,2,3,4,5)
print(result)


# DICT > DICTIONARY adalah list yang memiliki nama di setiap value

siswa = {
    "name":["Wongwong", "gungil", "niko"],
    "grade":11,
    "school":"Sutomo 1 Medan"
}

for key in siswa.keys():
    print(siswa[key])

for name in siswa["name"]:
    print(name)



def youngest_person(*people):
    # TODO: IMPLEMENT THE CODE HERE!
    pass


person1 = {"name": "Alice", "age": 25}
person2 = {"name": "Bob", "age": 19}
person3 = {"name": "Charlie", "age": 30}

result = youngest_person(person1, person2, person3)

print(result)