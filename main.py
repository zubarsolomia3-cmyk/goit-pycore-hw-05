git add .
git commit -m "Initial project structure"
git push origin main

cart = [
    {'name': 'Ноутбук', 'price': 32000, 'has_discount': False},
    {'name': 'Миша', 'price': 1200, 'has_discount': True},
    {'name': 'Клавіатура', 'price': 2100, 'has_discount': False}
]
all_prices_valid = all(item['price'] > 0 for item in cart)
print(f"Всі ціни валідні: {all_prices_valid}")

