# תרגיל 1 

def apply_to_all(numbers, action):
    temp = []
    for n in numbers:
        temp.append(action(n))
    return temp

# אפשר גם:
# return [action(n) for n in numbers]

print(apply_to_all([1, 2, 3], lambda n: n * 2))
print(apply_to_all([1, 2, 3], lambda n: n * n))
print(apply_to_all([1.6, 2.4], lambda n: round(n)))


# # # # #

# תרגיל 2

prices = [20, 75, 120, 45, 90]

filtered = list(filter(lambda p: p > 50, prices))
after_adding = list(map(lambda p: p + 10, filtered))

print(filtered)
print(after_adding)

# # # # #

# תרגיל 3

words = ["banana", "fig", "cherry", "kiwi"]
students = [("Dana", 92), ("Avi", 78), ('Noa', 85)]

sort_words = sorted(words, key=len)
print(sort_words[-1])
sort_students = sorted(students, key=lambda s: s[1], reverse=True)
print(list(map(lambda s: s[0], sort_students)))

# # # # #