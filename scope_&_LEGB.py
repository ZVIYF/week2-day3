# תרגיל 1

"""
def welcome(name):
    message = "Welcome " + name # נוצר משתנה לוקאלי
    return message

print(welcome("Dana"))
print(message) # שגיאה - המשתנה נוצר לוקאלית בפונקציה, לא מזוהה בחוץ
"""
# אם המשתנה message יהיה מוגדר מחוץ לפונקציה,
# תהיה אפשרות להדפיס אותו

"""
לדוגמה:
message = "Welcome "

def welcome(name):
    return message + name # כיון שלא קיים לוקאלי המערכת משתמש בגלובלי

print(welcome("Dana"))
print(message) # הפעם המשתנה גלובלי ואפשר להדפיס

"""

# # # # #

# תרגיל 2

"""
x = "global"
def first():
    x = "local in first"
    print("1:", x)

def second():
    print("2:", x)

first()
# ידפיס "local in first"
# הסיבה היא שההדפסה מתרחשת בתוך הפונקציה, שבה יש דריסה של המשתנה

second()
# ידפיס "global"
# אין דריסה של המשתנה בפונקציה, ולכן פונה למשתנה גלובלי

print("3:", x)
# ידפיס "global"
# ההדפסה מתרחשת ברמה גלובלית
"""

# # # # #

# תרגיל 3

"""
count = 0

def add_one():
    count = count + 1

add_one()
"""
# השגיאה היא UnBoundLocalError
# היא תופיע כיון שהמשתנה לא מוגדר בפונקציה,
# ולכן נוצרת השמה של משתנה כזה,
# בעוד שמיד לאחר מכן מנסים לקרוא למשתנה הגלובלי

# פתרון:
"""
count = 0

def add_one(count):
    return count + 1

count = add_one(count)
"""