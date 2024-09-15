
class Templates:
    @staticmethod
    def checks_presence_element(data, matrix):
        # """
        # Проверяет наличие искомого элемента в каждом списке матрицы
        # :param data: Принимает искомый элемент
        # :param matrix: Принимает матрицу
        # :return: Возвращает True если элемент есть в матрице, иначе False
        # """
        for elem in matrix:
            return True if data in elem else False



