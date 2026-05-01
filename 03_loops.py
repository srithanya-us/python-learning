# Example 1: simple loop

for i in range(1, 6):
    print("Number:", i)

# Example 2: loop through a list

skills = ["SQL", "Python", "Data Analysis"]

for skill in skills:
    print("Skill:", skill)

# Example 3: loop with condition

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(num, "is even")
    else:
        print(num, "is odd")