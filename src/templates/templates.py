
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
            if data in elem: return True
        return False
