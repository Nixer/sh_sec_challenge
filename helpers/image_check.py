import json

with open('values/images.json') as f:
    data = json.load(f)


def punisher(elements):
    value = True
    for e in elements:
        print(e.get_attribute("src"))
        if e.get_attribute("src") == data["Punisher"]:
            value = False
    return value
