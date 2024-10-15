# Remove an element from a list

def rem(L,word):
    for item in L:
        L.remove(word)
        return L

L = ["Ohi", "Oli", "Abbu", "Ammu", "Ohu", "hu"]
print(rem(L, "hu"))

# strip in list

def rem(L,word):
    n = []
    for item in L:
        if not(item==word):
            n.append(item.strip(word))
    return n

L = ["Ohi", "Oli", "Abbu", "Ammu", "Ohu", "hu"]
print(rem(L, "hu"))



