# demo code

# for i in range(1, 21, 2):
#     print(i, end=' ')
# print()

# task a

# for i in range(0, 101, 10):
#     print(i, end=' ')
# print()

# task b

# for i in range(20, 0, -1):
#     print(i, end=' ')
# print()

# task c
# number_of_stars = int(input("Enter number of stars: "))
# for i in range(amount_of_stars):
#     print("*", end='')
# print()

# task d
number_of_lines = int(input("Enter number of lines: "))
for i in range(number_of_lines):
    for j in range(i + 1):
        print("*", end='')
    print()
    