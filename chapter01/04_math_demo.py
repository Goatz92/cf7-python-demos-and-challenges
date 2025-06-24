import math

name = "Alice"
age = 20

print("CF7")
print("PI:", math.pi)

print(name, "is", age, "years old")

print("-----String Concatenation-----")
# print(name + "is " + age " years old")
print(name + " is " + str(age) + " years old")

# Python2 Style
print()
print("Python2 style")
print("PI = %6.2f" %math.pi)
print("%s is %d years old" %(name, age))

print("\nPython3 Style")
print("Age is {0:2d}".format(age))
print("PI is {0:.3f}".format(math.pi))

print("PI = {0:.3f} and age = {1}".format(math.pi, age))

print()
print("{0} is {1} years old".format(name, age), end="**")
print()

# f strings
print(f"{name} is {age} years old.")