import yaml


def analyze_data(file_name, case_key):
    with open("./data/" + file_name + ".yaml", "r") as f:
        data = yaml.load(f)[case_key]
        data_list = list()
        data_list.extend(data.values())
        # for temp in data.values():
        #     data_list.append(temp)
        return data_list
