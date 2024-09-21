import json
import os

#

class SaveAndLoadData:

    @staticmethod
    def create_folder() -> None:
        if not os.path.isdir(path_data):
            os.mkdir(path_data)

    @staticmethod
    def check_file_shopping_lists():
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_data + r'\shopping_lists.json'
        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def check_file_favorites_products():
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_data + r'\favorites_products.json'
        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def check_file_purchase_history():
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path_data + r'\purchase_history.json'
        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def read_data_with_shopping_lists() -> any:
        with open(path_data + r'\shopping_lists.json', 'r') as f:
            load_data = json.load(f)
            return load_data

    @staticmethod
    def write_data_in_shopping_lists(load_data) -> bool:
        with open(path_data + r'\shopping_lists.json', 'w') as f:
            json.dump(load_data, f, ensure_ascii=False, indent=4)
            return True

    @staticmethod
    def read_data_with_favorites_products() -> any:
        with open(path_data + r'\favorites_products.json', 'r') as f:
            load_data = json.load(f)
            return load_data

    @staticmethod
    def write_data_in_favorites_products(load_data) -> bool:
        with open(path_data + r'\favorites_products.json', 'w') as f:
            json.dump(load_data, f, ensure_ascii=False, indent=4)
            return True

    @staticmethod
    def read_data_with_purchase_history() -> any:
        with open(path_data + r'\purchase_history.json', 'r') as f:
            load_data = json.load(f)
            return load_data

    @staticmethod
    def write_data_in_purchase_history(load_data) -> bool:
        with open(path_data + r'\purchase_history.json', 'w') as f:
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


