def main():
    my_cart = Cart()
class Cart:
    def __init__(self, cart, product, cart_list=[], product_list=[]):
        self.cart = cart
        self.cart_list = cart_list
        self.product = product.title()
        self.product_list = product_list

    def add_to_cart(self, product):
        self.product.append(product)    

        
    def clear_cart(self, product_list):
        self.product_list.clear(product_list)

         
    def show_cart(self):
        pass
    
    def remove_from_cart(self, product):
        self.product.remove(product)
        
class Product:
    def __init__(self, product_name,product_price):
        self.product_name = product_name
        self.product_price = product_price        
        
product1 = Product('bread', '2.33')
product2 = Product('milk', '1.44')
product3 = Product('eggs', '2.11')

