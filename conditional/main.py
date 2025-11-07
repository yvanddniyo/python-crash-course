temperature = 15
if temperature > 30:
    print("Drink water")
    print("It's warm")
elif temperature > 20:
    print("it's nice")
else:
    print("it's cold")
print("Done")

# ternal operator

age = 64
message = "Eligible" if age >= 18 else "Not Eligible"
print("message: ", message)

if 18 <= age < 65:
    print('your age is fine')


# logical operator

high_income = False
good_credit = True
student = True

if ((high_income or good_credit) and not student):
    print("Eligible for loan")
else:
    print("Not eligible for loan")

print("bag" > "apple")
