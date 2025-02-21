def inverte_string (s):
    if len (s) <= 1:
        return s
    else:
        return inverte_string (s[1:]) + s[0]


s = input("digite uma string: ")

print (inverte_string (s))
