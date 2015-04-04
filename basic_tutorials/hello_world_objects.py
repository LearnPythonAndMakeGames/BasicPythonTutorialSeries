
def display(message):
    """Standard way to print a message"""
    print message


class HelloWorld(object):

    """Describes your function... display a message"""

    def __init__(self, message):
        self.message = message

    def display(self):
        """Display a message"""
        print self.message


hello_world_object_01 = HelloWorld("hi")
hello_world_object_02 = HelloWorld("Hello, World!")
hello_world_object_03 = HelloWorld("Yo, sup!")

hello_world_object_01.display()
hello_world_object_02.display()
hello_world_object_03.display()

display("hi")
display("Hello, World!")
display("Yo, sup!")
