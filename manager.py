from products import products

def view_products():
    for product in products:
        print(product)

def update_price(product_id, new_price):
    for product in products:
        if product["id"] == product_id:
            product["price"] = new_price
            return f"Price updated for {product['name']}"

def update_stock(product_id, new_stock):
    for product in products:
        if product["id"] == product_id:
            product["stock"] = new_stock
            return f"Stock updated for {product['name']}"
