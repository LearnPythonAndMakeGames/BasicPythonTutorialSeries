#!/usr/bin/env python


class HelloWorld(object):
    """Our first class"""

    def __init__(self, message):
        self.message = message

    def display(self):
        print self.message


our_first_object = HelloWorld('Hello, World!')
our_second_object = HelloWorld('Hello, Brian!')

our_first_object.display()  # Hello, World!
our_second_object.display()  # Hello, Brian!


