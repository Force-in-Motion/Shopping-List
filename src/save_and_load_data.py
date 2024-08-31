import json
import os


class SaveAndLoadData:

    @staticmethod
    def check_file():
        """
        Проверяет наличие файла txt по указанному пути, в данном случае в папке
        :return: True или False
        """
        file = path + r'\config.json'
        if os.path.isfile(file):
            return True
        else:
            return False

    @staticmethod
    def read_data_in_json() -> any:
        with open(path + 'config.json', 'r') as f:
            read_data = f.read()
            load_data = json.loads(read_data)
            return load_data

    @staticmethod
    def write_data_with_json(load_data) -> bool:
        with open(path + 'config.json', 'w') as f:
            f.write(load_data)
            return True

    @staticmethod
    def create_folder() -> None:
        if not os.path.isdir(path):
            os.mkdir(path)

    # @staticmethod
    # def





path = os.environ.get('LOCALAPPDATA') + r'\Notes User'
path_csv = os.path.expanduser('~') + r'\Desktop'