import json


def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def load_from_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
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


def delete_one_time(data, title):
    data['one_time'] = [temp for temp in data['one_time'] if temp['title'] != title]


def delete_many_time(data, title):
    data['many_time'] = [temp for temp in data['many_time'] if temp['title'] != title]


def delete_subscription(data, title):
    data['subscription'] = [temp for temp in data['subscription'] if temp['title'] != title]


def delete_preferential(data, title):
    data['preferential'] = [temp for temp in data['preferential'] if temp['title'] != title]
