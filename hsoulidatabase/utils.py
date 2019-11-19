import json


def get_json_data(json_path):
    with open(json_path) as json_file:
        data = json.load(json_file)
        return data


def write_status(data, output_path):
    with open(output_path, 'w') as outfile:
        json.dump(data, outfile)