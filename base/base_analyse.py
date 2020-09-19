import json


def analyse(file):
    with open("./data/" + file, "r", encoding="utf-8") as f:
        list_data = []
        dict_data = json.load(f)
        for value in dict_data.values():
            list_data.append(value)
        return list_data