import sys

commandline_arguments = sys.argv

if len(commandline_arguments) >= 2:
    commandline_arguments = commandline_arguments[1:]
else:
    commandline_arguments = []


def adder(*args):
    """Adder takes a list of commnadline arguments and returns their sum"""
    value = 0
    for every_argument in args[0]:
        value = int(every_argument) + value
    return value

print adder(commandline_arguments)
