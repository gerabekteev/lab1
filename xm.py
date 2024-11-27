import xml.etree.ElementTree as ET


def save_to_xml(data, filename):
    root = ET.Element("tickets")

    for category, items in data.items():
        category_elem = ET.SubElement(root, category)
        for item in items:
            item_elem = ET.SubElement(category_elem, "ticket")
            for key, value in item.items():
                ET.SubElement(item_elem, key).text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def load_from_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data = {"one_time": [], "many_time": [], "subscription": [], "preferential": []}

        for category in root:
            for ticket in category:
                item = {}
                for field in ticket:
                    item[field.tag] = field.text
                data[category.tag].append(item)

        return data
    except FileNotFoundError:
        return {"one_time": [], "many_time": [], "subscription": [], "preferential": []}


def add_one_time(data, one_time):
    data['one_time'].append(one_time.to_dict())


def add_many_time(data, many_time):
    data['many_time'].append(many_time.to_dict())


def add_subscription(data, subscription):
    data['subscription'].append(subscription.to_dict())


def add_preferential(data, preferential):
    data['preferential'].append(preferential.to_dict())


def delete_one_time(data, name_owner):
    data['one_time'] = [temp for temp in data['one_time'] if temp['name_owner'] != name_owner]


def delete_many_time(data, name_owner):
    data['many_time'] = [temp for temp in data['many_time'] if temp['name_owner'] != name_owner]


def delete_subscription(data, name_owner):
    data['subscription'] = [temp for temp in data['subscription'] if temp['name_owner'] != name_owner]


def delete_preferential(data, name_owner):
    data['preferential'] = [temp for temp in data['preferential'] if temp['name_owner'] != name_owner]
