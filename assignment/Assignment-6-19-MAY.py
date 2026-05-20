cart = {
    "Laptop": {"price": 50000, "qty": 1},
    "Mouse": {"price": 500, "qty": 2}
}

def updateQuantitiy(product,q):
    cart[product]["qty"] = q

def addProduct(product):
    for x in product:
        if (x in cart):
            updateQuantitiy(x,cart[x]['qty']+product[x]["qty"])
        else:
            cart[x] = product[x]

def removeProduct(product):
    if product.capitalize() in cart:
        cart.pop(product.capitalize())
    else:
        print("item doesn't exists")



def calculateTotalBill():
    total = 0
    for x in cart:
        total+=cart[x]['price'] * cart[x]['qty']
    if total>50000:
        return 0.9*total
    return total

# Find most expensive product
def findMostExpensiveProduct():
    max = -1e9
    ans = {}
    for x in cart:
        if (cart[x]['price']>max):
            ans = {x,cart[x]['price']}
            max = cart[x]['price']
    return ans


p1 = {"Laptop":{"price":2000,"qty":5}}
addProduct(p1)
print(calculateTotalBill())
print(findMostExpensiveProduct())
removeProduct('laptop')
print(cart)
