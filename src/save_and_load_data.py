import json
import os


class SaveAndLoadData:

    @staticmethod
    def create_folder() -> None:
        if not os.path.isdir(path_data):
            os.mkdir(path_data)

    @staticmethod
    def check_file():
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_data + r'\data.json'
        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def read_data_with_json() -> any:
        with open(path_data + r'\data.json', 'r') as f:
            load_data = json.load(f)
            return load_data

    @staticmethod
    def write_data_in_json(load_data) -> bool:
        with open(path_data + r'\data.json', 'w') as f:
            json.dump(load_data, f, ensure_ascii=False, indent=4)
            return True

    @staticmethod
    def read_categories_with_json() -> any:
        with open(path_categories, 'r') as f:
            load_data = json.load(f)
            return load_data

    @staticmethod
    def write_categories_in_json(load_data):
        with open(path_categories, 'w') as f:
            json.dump(load_data, f, ensure_ascii=False, indent=4)
            return True







path_data = os.environ.get('LOCALAPPDATA') + r'\Shopping list data'


path_categories = r'D:\Python\School\Проекты\Shopping-List\src\Categories\categories.json'

path_csv = os.path.expanduser('~') + r'\Desktop'

SaveAndLoadData.read_data_with_json()
