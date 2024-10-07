import pytest
import customtkinter as ctk
from src.create.create_list import ScrollCreateList, CreateList
from src.start.main_page import MainPage

start_window = MainPage()

create_list = CreateList(start_window)

scroll_create_list = ScrollCreateList(create_list, create_list)

checkbox = ctk.CTkCheckBox(scroll_create_list)

data_test_scl_create_checkbox = [( 'ананас', 4, 'Продукты питания', None),
                                 ( 'кочерга', 4, 'Инструменты', None),
                                 ( 'скакалка', 4, 'Спорт. Товары', None),
                                 ( 'леска', 4, 'Рыбалка', None),
                                 ( 'ружье', 4, 'Охота', None)]

@pytest.mark.SCL_create_checkbox
@pytest.mark.parametrize('val1, val2, val3, expect_result', data_test_scl_create_checkbox)
def test_create_checkbox(val1, val2, val3, expect_result):
    assert scroll_create_list.create_checkbox(val1, val2, val3) is None


data_test_scl_set_new_text_for_checkbox = [(checkbox, 'ананас, 4, Продукты питания', None),
                                           (checkbox, 'кочерга, 9, Инструменты', None),
                                           (checkbox, 'скакалка, 48, Спорт. Товары', None),
                                           (checkbox, 'леска, 14, Рыбалка', None),
                                           (checkbox, 'ружье, 25, Охота', None),]

@pytest.mark.SCL_set_text_checkbox
@pytest.mark.parametrize('val1, val2, expect_result', data_test_scl_set_new_text_for_checkbox)
def test_set_new_text_for_checkbox(val1, val2, expect_result):
    assert scroll_create_list.set_new_text_for_checkbox(val1, val2) is None


data_test_create_list_select_checkboxes = [scroll_create_list.list_checkboxes, [checkbox]]


@pytest.mark.SCL_list_select_checkboxes
@pytest.mark.parametrize('val, expect_result', data_test_create_list_select_checkboxes)
def test_create_list_select_checkboxes(val, expect_result):
    assert scroll_create_list.create_list_select_checkboxes() is None




















# data_test_scl_create_checkbox_negative = [( int, int, int, pytest.raises(TypeError)),
#                                           ( str, int, int, pytest.raises(TypeError)),
#                                           ( int, None, int, pytest.raises(TypeError)),
#                                           ( str, None, str, pytest.raises(TypeError)),
#                                           ( None, None, None, pytest.raises(TypeError)),
#                                           ( [None], [], dict, pytest.raises(TypeError)),
#                                           ( dict, [], str, pytest.raises(TypeError)),]
#
# @pytest.mark.SCL_create_checkbox_neg
# @pytest.mark.parametrize('val1, val2, val3, expect_result', data_test_scl_create_checkbox_negative)
# def test_create_checkbox_negative(val1, val2, val3, expect_result):
#     with expect_result:
#         scroll_create_list.create_checkbox(val1, val2, val3) is None