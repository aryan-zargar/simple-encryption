from key import key
letters = (list(" abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+?/|><=-"))
text = input("Write the text you want to encrypt : ")
enctext = ''
for i in list(text):
    index = letters.index(i)
    enctext += key[index]
print(f"encrypted text : {enctext}")