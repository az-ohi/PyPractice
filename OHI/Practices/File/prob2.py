words = ["Donkey", "bad", "nasty"]

with open("new_donkey.txt", "r")as f:
    content = f.read()

for word in words:
     content = content.replace(word, "#"*len(word))

with open("new_donkey.txt", "w")as f:
    f.write(content)