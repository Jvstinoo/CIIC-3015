def groceries(items, budget, tax):
    total = 0
    tax = tax/100

    for item in items:
        item = (item*tax + item)
        if(item + total < budget):

            total += item

    return round(total, 2)


print(groceries([5.5, 7, 2.3], 7, 0))
print(groceries([20, 7, 5, 2, 3], 75, 11.5))
print(groceries([15.5, 7.5, 2.3], 35, 1.5))
