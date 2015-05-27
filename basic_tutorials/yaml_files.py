import yaml

def yaml_loader(filepath):
    """Loads a yaml file"""
    with open(filepath, "r") as file_descriptor:
        data = yaml.load(file_descriptor)
    return data

def yaml_dump(filepath, data):
    """Dumps data to a yaml file"""
    with open(filepath, "w") as file_descriptor:
        yaml.dump(data, file_descriptor)

if __name__ == "__main__":
    filepath = "test.yaml"
    data = yaml_loader(filepath)

    items = data.get('items')
    for item_name, item_value in items.iteritems():
        print item_name, item_value

    filepath2 = "test2.yaml"
    data2 = {
        "items": {
            "sword": 100,
            "axe": 80,
            "boots": 40
        }
    }
    yaml_dump(filepath2, data2)

