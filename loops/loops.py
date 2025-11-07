# for number in range(3):
# print("attempt", number, (number) * ".")

successfully = False

for number in range(3):
    print("Attempt")
    if successfully:
        print("successfully")
        break
else:
    print("Attempted 3 times and failed.")

# Nested loop
arr = []
for x in range(5):
    for y in range(3):
        if (x == y):
            arr.append(x)
            print(f"matched value are {x}, {arr}")
        print(f"({x}, {y})")
print("arr", arr)

# Itelable

# for name in "yvan":
# print('name', name)

# while loop

number = 100

while number > 0:
    print(number)
    number //= 2


# mini buildin terminal python
# command = "" we dont need this

while True:
    command = input(">")
    print("ECHO", command)
    if command.lower() == "quit":
        break
