def display(arg1=None, arg2=None, message="Hello World!"):
    """Displays message on the command-line"""
    print message

display(1, 2, "Hello, World!")
display(1, 2, 100)
display(1, 2, True)

variable = 3.14
display(1, 2, variable)

display(1, 2)

display(message="Yup")


def display2(*messages):
    """Displays message on the command-line"""
    for message in messages:
        print message,
    print

display2('a', 'b', 'c', 'd', 'e', 'f')
display2("Hi", 2, "The World!")
