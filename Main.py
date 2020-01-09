"""
The main file the the CodeGeneratorCore project's main file.
All the action of the project is start from here.
"""

# File reader
import yaml

from cores.rules.rule_config import RuleConfig


def read_files(files):
    files_type = type(files)
    res = []
    if files_type:  # if the type is list, will read every file in list.
        for file in files:
            temp = read_as_yaml(file)
            res.extend(temp)
    elif files_type == type(""):  # if the type is str, will read it.
        res.extend(read_as_yaml(files))
    return res


# read the yaml file
def read_as_yaml(file):
    x = []
    with open(file) as f:
        res = yaml.load_all(f)
        for value in res:
            x.append(value)
    return x


if __name__ == '__main__':
    x = []
    with open("cores/rules/rules.yaml") as f:
        res = yaml.full_load_all(f)
        for value in res:
            x.append(value)
    temp = RuleConfig()
    temp.init_by_list(x)
