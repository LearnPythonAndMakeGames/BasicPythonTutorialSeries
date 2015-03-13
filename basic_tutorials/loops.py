
condition = True
counter = 0

while(condition):
    if counter < 5:
        print counter
    else:
        print counter, "Hi"
    counter = counter + 1
    condition = counter < 10


for counter in ['a', 'b', 'c']:
    print counter
