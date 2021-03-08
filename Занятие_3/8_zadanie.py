print("Enter coefficients for the equation")
print("ax^2 + bx + c = 0:")

while True:
    a = input ("a = ")
    try:
        a = float(a)
        break
    except ValueError:
        print("You entered not a number")

while True:
    b = input ("b = ")
    try:
        b = float(b)
        break
    except ValueError:
        print("You entered not a number")

while True:
    c = input ("c = ")
    try:
        c = float(c)
        break
    except ValueError:
        print("You entered not a number")

if not a and not b and not c:
    print("x - either")
elif not a and not b and c:
    print("The equation is not correct:\nno solutions")
elif not a and b:
    x = -c / b
    print("x =", x)
else:
    discr = b ** 2 - 4 * a * c
    if (discr > 0):
        x1 = (-b + discr ** 0.5) / (2 * a)
        x2 = (-b - discr ** 0.5) / (2 * a)
        print("x1 =", x1)
        print("x2 =", x2)
    elif (discr == 0):
        print("x =", -b / (2 * a))
    elif (discr < 0):
        x1 = complex(-b + discr ** 0.5) / (2 * a)
        x2 = x1.conjugate()
        print(f"x1 = {x1:.3f}, x2 = {x2:.3f}")      
