
condition = False
another_condition = True

# True, True --> "Hello", "Sup", "Last Line"
# True, False --> "Hello", "Last Line"
# False, * -->  "Bye", "Last Line"

if(condition):
    print "Hello, World!"
    if(another_condition):
        print "Sup, World!"
else:
    print "Bye, World!"

print "Last Line."

