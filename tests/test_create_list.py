import pytest
import customtkinter as ctk
from src.create.create_list import ScrollCreateList, CreateList
from src.start.main_page import MainPage


start_window = MainPage()

create_list = CreateList(start_window)

scroll_create_list = ScrollCreateList(create_list, create_list)

checkbox = ctk.CTkCheckBox(scroll_create_list)



@pytest.fixture(scope='session')
def fills_list_checkboxes():
    checkbox_1 = ctk.CTkCheckBox(scroll_create_list, text='кочерга, 4, Инструменты')
    checkbox_1.select()

    checkbox_2 = ctk.CTkCheckBox(scroll_create_list, text='скакалка, 4, Спорт. Товары')
    checkbox_2.deselect()

    checkbox_3 = ctk.CTkCheckBox(scroll_create_list, text='леска, 4, Рыбалка')
    checkbox_3.deselect()

    checkbox_4 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_4.select()

    checkbox_5 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_5.select()

    checkbox_6 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_6.deselect()

    checkbox_7 = ctk.CTkCheckBox(scroll_create_list, text='ружье, 4, Охота')
    checkbox_7.select()

    return scroll_create_list.list_checkboxes.extend([checkbox_1, checkbox_2, checkbox_3, checkbox_4, checkbox_5, checkbox_6, checkbox_7])



data_test_scl_create_checkbox = [( 'ананас', 4, 'Продукты питания', None),
                                 ( 'кочерга', 4, 'Инструменты', None),
                                 ( 'скакалка', 4, 'Спорт. Товары', None),
                                 ( 'леска', 4, 'Рыбалка', None),
                                 ( 'ружье', 4, 'Охота', None)]

@pytest.mark.SCL_create_checkbox
@pytest.mark.parametrize('val1, val2, val3, expect_result', data_test_scl_create_checkbox)
def test_create_checkbox(val1, val2, val3, expect_result):
    """
    Проверяет создание нового чекбокса в скролле фрейма и проверяет, что чекбокс добавлен в список
    """
    count_checkboxes_in_list = len(scroll_create_list.list_checkboxes)

    assert scroll_create_list.create_checkbox(val1, val2, val3) is None

    assert len(scroll_create_list.list_checkboxes) == count_checkboxes_in_list + 1



data_test_scl_set_new_text_for_checkbox = [(checkbox, 'ананас, 4, Продукты питания', None),
                                           (checkbox, 'кочерга, 9, Инструменты', None),
                                           (checkbox, 'скакалка, 48, Спорт. Товары', None),
                                           (checkbox, 'леска, 14, Рыбалка', None),
                                           (checkbox, 'ружье, 25, Охота', None),]

@pytest.mark.SCL_set_text_checkbox
@pytest.mark.parametrize('val1, val2, expect_result', data_test_scl_set_new_text_for_checkbox)
def test_set_new_text_for_checkbox(val1, val2, expect_result):
    """
    Проверяет установку нового текста для чекбокса и проверяет, что текст изменился
    """
    old_text_checkbox = val1.cget("text")

    assert scroll_create_list.set_new_text_for_checkbox(val1, val2) is None

    assert val1.cget("text")!= old_text_checkbox


@pytest.mark.SCL_list_select_checkboxes
def test_create_list_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_create_list.create_list_select_checkboxes()

    for i in result:
        assert type(i) == ctk.CTkCheckBox

    assert len(result) == 4


@pytest.mark.SCL_list_text_select_checkboxes
def test_create_list_text_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции фильтрации чекбоксов и создания списка текстов активных чекбоксов, а так же тип элементов списка
    """
    result = scroll_create_list.create_list_text_select_checkbox()

    for i in result:
        assert type(i) == str

    assert len(result) == 4


@pytest.mark.SCL_delete_checkbox
def test_delete_checkbox(fills_list_checkboxes):
    """
    Проверяет удаление чекбокса из скролл фрейма и проверяет, что чекбокс удален из списка
    """
    initial_count = scroll_create_list.count_checkboxes

    assert initial_count == 12

    scroll_create_list.delete_checkbox()

    initial_count = scroll_create_list.count_checkboxes

    assert initial_count == 8


@pytest.mark.SCL_check_select_checkboxes
def test_check_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции проверки чекбоксов и создания списка активных чекбоксов, а так же проверяет, что чекбоксы отмечены
    """
    for i in scroll_create_list.list_checkboxes:
        i.select()

    assert scroll_create_list.check_selected_checkbox() is True

    scroll_create_list.reset_checkboxes()

    assert scroll_create_list.check_selected_checkbox() is False


@pytest.mark.SCL_get_select_checkboxes
def test_get_select_checkboxes(fills_list_checkboxes):
    """
    Проверяет работу функции получения чекбоксов и возвращения текста активных чекбоксов или вернет (None, None)
    """
    for i in scroll_create_list.list_checkboxes:
        i.select()

    text, elem = scroll_create_list.get_selected_checkbox()

    assert text == 'ананас, 4, Продукты питания'

    assert elem == scroll_create_list.list_checkboxes[0]

    for i in scroll_create_list.list_checkboxes:
        i.deselect()

    assert scroll_create_list.get_selected_checkbox() == (None, None)

















