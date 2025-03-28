# List Comprehension
l = [1, 2, 3, 4]
l2 = [x for x in l if x % 2 == 0]
# l2 = [x * 2 for x in l]
print(l2)

# Nested Conditional
a = 5
b = 6

# Single level of conditions
if a == 5:
    print("Scenario A")
elif a == 6:
    print("Scenario B")
else:
    print("Scenario C")

# Nested; BUT still could be written as if-elif-else
if a == 5:
    print("Scenario A")
else:
    if a == 6:
        print("Scenario B")
    else:
        print("Scenario C")

# Nested; use this
if a == 5:
    if b == 6:
        print("Scenario A")
    else:
        print("Scenario B")
else:
    print("Scenario C")