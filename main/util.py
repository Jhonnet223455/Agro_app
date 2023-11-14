class ShoppingCart:
    def __init__(self, request):
        self.request = request
        self.session = request.session

        self.cart = self.session.get("cart")

        if not self.cart:
            self.cart = {}
            self.session["cart"] = self.cart

        
    def add(self, product):
        id = str(product.id)
        if id not in self.cart.keys():
            self.cart[id] = {
                "id" : int(product.id),  
                "name" : product.name,
                "price" : float(product.price),
                "stock" : product.stock,
                "accumulated" : float(product.price),
                "amount" : 1,
            }
        else:
            self.cart[id]["amount"] += 1
            self.cart[id]["accumulated"] += float(product.price)

        self.save()

    
    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def delete(self, product):
        id = str(product.id)

        if id in self.cart:
            del self.cart[id]
            self.save()

    def subtract(self, product):
        id = str(product.id)

        self.cart[id]["amount"] -= 1
        self.cart[id]["accumulated"] -= float(product.price)

        if self.cart[id]["amount"] <= 0:
            del self.cart[id]

        self.save()

    def clear(self):
        self.session["cart"] = {}
        self.session.modified = True
