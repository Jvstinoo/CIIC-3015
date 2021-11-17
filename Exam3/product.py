def Product(cont):
    if len(cont) == 1:
        return cont[0]
    return cont[0] * Product(cont[1:])


print(Product((2, 3, 5)))
