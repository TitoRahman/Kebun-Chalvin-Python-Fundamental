word_a = input("Enter a word: ").lower()
word_b = input("Enter another word: ").lower()

count_word_a = [0]*26
count_word_b = [0]*26

for word in word_a:
    i_word = ord(word)-ord('a') # Ubah dalam bentuk angka ord(word)-ord('a') > 97 (jika word adalah a) - 97 = 0
    count_word_a[i_word] += 1

for word in word_b:
    i_word = ord(word) - ord('a')  # Ubah dalam bentuk angka ord(word)-ord('a') > 97 (jika word adalah a) - 97 = 0
    count_word_a[i_word] += 1

if count_word_a == count_word_b:
    print("Anagrams")
else :
    print("Not Anagrams")