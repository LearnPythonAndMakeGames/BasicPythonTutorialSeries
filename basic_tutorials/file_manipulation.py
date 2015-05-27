
def file_loader(filepath):
    """Reads in file and returns data"""
    with open(filepath, "r") as file_descriptor:
        data = file_descriptor.read()
    return data

def file_load_lines(filepath):
    """Reads in file and returns data as a list of lines"""
    with open(filepath, "r") as file_descriptor:
        data = file_descriptor.read()
        # data = file_descriptor.readlines()
        data_lines = data.split("\n")
        # original_text = "\n".join(data)
    return data_lines

def file_dumper(filepath, data):
    with open(filepath, "w") as file_descriptor:
        file_descriptor.write(data)

if __name__ == "__main__":
    filepath = "test.txt"
    data = file_loader(filepath)
    print data

    filepath2 = "test2.txt"
    file_dumper(filepath2, data)

    data2 = file_load_lines(filepath)
    print data2
