import random
import string

char =   string.punctuation + string.ascii_letters + string.digits 
char = list(char)
key = char.copy()
random.shuffle(key)

# print(f"char: {char}")
# print(f"key: {key}")

#ENCRYPT
message = input("Enter a message to input: ")
cipher_text = " "
for letter in message:
    index = char.index(letter)
    cipher_text += key[index]
print(f"Orginal message: {message}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT

cipher_text = input("Enter an encrypted message to input: ")
message = " "
for letter in cipher_text:
    index =  key.index(letter)
    message += char[index]
print(f"Encrypted message: {cipher_text}")
print(f"Decrypted message: {message}")


