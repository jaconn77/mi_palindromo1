
def palindromo_correcto(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False

print(palindromo_correcto("ana"))