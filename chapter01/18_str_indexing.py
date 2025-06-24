message = "Coding Factory"

print(message[0])
print(message[1])
print(message[2])
print(message[3])
print(message[4])
print(message[5])

# message[0] = 'c'
# message = 'New message'

print(f"Length of {message} = {len(message)}")

for char in message:
    print(char, end=" ")
print()

# Enhanced for
for i in range(10 + 1):
    print(i)

print("-" * 10)
print(i)

# for indexing based
message = "Coding Factory"

for i in range(len(message)):
    print(message[i], end="")

my_num = 123456789

str_num = str(my_num)
first_num = int(str_num[0])
last_num = int(str_num[-1])

result = first_num + last_num
print()
print(result)

print(f"Result = {int(str_num[0]) + int(str_num[-1])}")