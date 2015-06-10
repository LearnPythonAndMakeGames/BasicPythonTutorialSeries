import yaml

def yaml_load(filepath):
    """Loads yaml file and returns data"""
    with open(filepath, 'r') as fd:
        return yaml.load(fd)

def yaml_dump(filepath, data):
    """Loads yaml file and returns data"""
    with open(filepath, 'w') as fd:
        return yaml.dump(data, fd)