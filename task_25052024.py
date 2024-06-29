

def encrypt_text(txt):
    length = len(txt)
    i = -1
    while i < length-1:
        i += 1
        if txt[i] == "ё":
            txt = txt[:i] + 'ж' + txt[i+1:]
            continue
        if txt[i] == "Ё":
            txt = txt[:i] + "Ж" + txt[i+1:]
            continue
        if txt[i] == "е":
            txt = txt[:i] + "ё" + txt[i+1:]
            continue
        if txt[i] == "Е":
            txt = txt[:i] + "Ё" + txt[i+1:]
            continue
        if txt[i] == "я":
            txt = txt[:i] + "а" + txt[i+1:]
            continue
        if txt[i] == "Я":
            txt = txt[:i] + "А" + txt[i+1:]
            continue
        if txt[i] == "z":
            txt = txt[:i] + "a" + txt[i+1:]
            continue
        if txt[i] == "Z":
            txt = txt[:i] + "A" + txt[i+1:]
            continue
        if txt[i] >= "a" and txt[i] < "z" or txt[i] >= "A" and txt[i] < "Z" or txt[i] >= "а" and txt[i] < "я" or txt[i] >= "А" and txt[i] < "Я":
            txt = txt[:i] + chr(ord(txt[i])+1) + txt[i+1:]
            continue
    return txt


def decrypt_text(txt):
    length = len(txt)
    i = -1
    while i < length-1:
        i += 1
        if txt[i] == "ё":
            txt = txt[:i] + "е" + txt[i+1:]
            continue
        if txt[i] == "Ё":
            txt = txt[:i] + "Е" + txt[i+1:]
            continue
        if txt[i] == "ж":
            txt = txt[:i] + "ё" + txt[i+1:]
            continue
        if txt[i] == "Ж":
            txt = txt[:i] + "Ё" + txt[i+1:]
            continue
        if txt[i] == "а":
            txt = txt[:i] + "я" + txt[i+1:]
            continue
        if txt[i] == "А":
            txt = txt[:i] + "Я" + txt[i+1:]
            continue
        if txt[i] == "a":
            txt = txt[:i] + "z" + txt[i+1:]
            continue
        if txt[i] == "A":
            txt = txt[:i] + "Z" + txt[i+1:]
            continue
        if txt[i] > "a" and txt[i] <= "z" or txt[i] > "A" and txt[i] <= "Z" or txt[i] > "а" and txt[i] <= "я" or txt[i] > "А" and txt[i] <= "Я":
            txt = txt[:i] + chr(ord(txt[i])-1) + txt[i+1:]
            continue
    return txt


# text_test = "Строки в Python неизменяемы, поэтому для этой операции нет встроенного метода. Вам придётся создать новую строку на основе исходной.\nStrings in Python are immutable, so there is no built-in method for this operation. You will have to create a new string based on the original one."
# encrypted_text = encrypt_text(text_test)
# decrypted_text = decrypt_text(encrypted_text)
# print(f"{text_test} -> {encrypted_text}")
# print("*****************************")
# print(f"{encrypted_text} -> {decrypted_text}")

text_to_encrypt = input("Введите текст для шифрования:")
print("Зашифрованное сообщение:")
print(f"{encrypt_text(text_to_encrypt)}")
text_to_decrypt = input("Введите текст для дешифрования:")
print("Дешифрованное сообщение:")
print(f"{decrypt_text(text_to_decrypt)}")










