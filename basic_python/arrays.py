# list  # mutable
# tuple  # immutable

# String
x = "Hello, World!"
x[0] == "H"
x[-1] == "!"
x[0:4] == "Hell"

# List
y = [0, 1, 2, 3]
y[0] == 0
y[1] == 1
y[-1] == 3

y[0:3] == [0, 1, 2]


z = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o']
z[0] == "H"
z[-1] == "!"
z[0:4] == "Hell"


w = ['H', 0, 3.14, True, [0, 1, 3]]
w[0] == "H"
w[1] == 0
w[2] == 3.14

w[-1] == [0, 1, 3]

m = list(0, 1, 3) == [0, 1, 3]

l = tuple(0, 1, 3)
