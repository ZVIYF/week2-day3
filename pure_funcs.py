# תרגיל 1

"""
def square(n):
    return n * n

# פונקציה טהורה
    

def log_square(n):
    print("squaring", n)
    return n * n

# לא טהורה - מדפיסה באמצע החישוב
    

def add_item(cart, item):
    cart.append(item)
    return cart

# לא טהורה - כיוון שרשימה ניתנת לשינוי, והאובייקט שבחוץ משתנה

def with_item(cart, item):
    return cart + [item]

# טהורה - מחזיר צירוף של הרשימה הקיימת
# עם האייטם הנוסף מבלי לבצע שינוי ברשימה
"""

# # # # #

# תרגיל 2

total = 0

def add_price(total, price):
    return total + price

total = add_price(total, 10)
total = add_price(total, 10)
print(total)    

print(add_price(0, 10))
print(add_price(0, 10))

# # # # #

# תרגיל 3

TAX = 1.17

def apply_tax(prices):
    return [p * TAX for p in prices]

prices = [100, 50]
with_tax = apply_tax(prices)
print(prices)
print(with_tax)

# # # # # 

