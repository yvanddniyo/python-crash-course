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

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break


words = ["cat", "windows", "defenestrate"]

for w in words:
    print("num", len(w))


users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
    print("user", user)
    print("status", status)
print("all", users)

# Strategy:  Create a new collection
active_user = {}
for user, status in users.items():
    if status == 'active':
        active_user[user] = status

print("->", users)

a = ['Mary', 'had', 'a', 'little', 'lamb']

for i in range(len(a)):
    print("->", a[i])


# Match in the python

def https_error(status):
    match status:
        case 400:
            return "Bad Request"
        case 401 | 402 | 403:
            return "Not allowed to perform this action."
        case 418:
            return "I'm a developer"
        case _:
            return "Something went wrong with your internet, please check your internet."


res = https_error(401)
print('res', res)

# call a method on each element

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
f = [weapon.strip() for weapon in freshfruit]
print("fresh", f)

# create a list of 2-tuples like (number, square)

t = [(x, x**2) for x in range(6)]
print('t', t)


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
z = list(zip(*matrix))
m = [[row[i] for row in matrix] for i in range(4)]
print("m", m)
print("z", z)

a = {x for x in 'abracadabra' if x not in 'abc'}
print('a', a)

# DICTIONARY

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
del tel['sape']
t = 'guido' in tel
print("t", t)
print('print', sorted(list(tel)))

dict = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("print", dict)

# In addition, dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:

build_dict = {x: x**2 for x in range(4)}
print("build_dict", build_dict)

# Looping Techniques

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
arr = []
for k,  v in knights.items():
    arr.append(v)
    print("-->", k, v)
print('arr', arr)


for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)

# ZIPPING

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {0} ? it is {1}.'.format(q, a))
