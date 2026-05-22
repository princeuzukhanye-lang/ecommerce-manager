from manager import view_products, update_price, update_stock

print("🛒 E-commerce Manager System\n")

view_products()

print("\nUpdating price and stock...\n")

print(update_price(1, 25))
print(update_stock(2, 8))

print("\nUpdated Products:\n")
view_products()
