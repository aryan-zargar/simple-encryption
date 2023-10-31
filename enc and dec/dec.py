from key import key
letters = (list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+?/|><=-"))
text = ''
enctext = input("Write the text you want to decrypt : ")
for i in list(enctext):
    index = key.index(i)
    text += letters[index-1]
print(f"encrypted text : {text}")