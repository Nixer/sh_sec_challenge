import json

with open('values/images.json') as f:
    data = json.load(f)

#Check if 'Punisher' image exists on the page (return False if does)
def punisher(elements):
    value = True
    for e in elements:
        im_link = ((e.get_attribute("src")).split("/"))[-1]
        if im_link == data["Punisher"]:
            value = False
    return value

#Print images names
def images_names(elements):
    for e in elements:
        im_link = ((e.get_attribute("src")).split("/"))[-1]
        for name, link in data.items():
            if im_link == link:
                print(name)
    return True
