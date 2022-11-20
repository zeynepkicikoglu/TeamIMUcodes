#faktöriyel hesabı yapan recursive bir fonksiyon yazın

def recursivefaktoriyel(sayi):

    if (sayi == 1 or sayi == 0):
        return 1
    else:
        return (sayi * recursivefaktoriyel(sayi - 1))

print(recursivefaktoriyel(5))


