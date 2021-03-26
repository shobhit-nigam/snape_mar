# filter

lista = ['a', 'y', 't', 'e', 'i', 'f', 'r', 'w', 'v', 'o', 'a'] 
# vowels

def funca(c):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if c in vowels:
        return False
    else:
        return True


res = list(filter(funca, lista)) 

print(res) 

