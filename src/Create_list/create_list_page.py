from src.Top_lvl_pages.top_lvl_pages import *
from tkinter.messagebox import showerror
from src.save_and_load_data import SaveAndLoadData as sld
from src.Create_list.config_create_list import *
from src.Templates import Templates
import customtkinter as ctk
from PIL import Image


class ScrollCreateList(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для добавления товаров
    """

    def __init__(self, main_window, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__main_window = main_window
        self.__product = None
        self.__list_check_boxes = []

    def create_check_box(self, name_product, count_product, category) -> None:
        """
        Создает чекбокс в скролл фрейме с переданными данными в качестве текста
        :param name_product: Принимает название продукта
        :param count_product: Принимает количество продукта
        :param category: Принимает категорию продукта
        :return: None
        """
        self.__product = ctk.CTkCheckBox(self, text=f'{name_product}, {count_product}, {category}', font=ft_p,
                                         hover_color=hc_p, fg_color=fgc_p, border_width=bw_p)

        self.__list_check_boxes.append(self.__product)
        self.__product.grid(padx=(10, 0), pady=10)

    def set_new_text_for_check_box(self, checkbox,  new_text) -> None:
        """
        Устанавливает новый текст для чекбокса если он не существует
        :param checkbox: Принимает ссылку на чекбокс
        :param new_text: Принимает новый текст для чекбокса
        :return: None
        """
        if checkbox is not None:
            checkbox.configure(text=new_text)

    def check_selected_check_box(self) -> bool:
        """
        Обходит список чекбоксов и выполняет проверку, если хоть один активен - вернет True иначе False
        """
        for checkbox in self.__list_check_boxes:
            if checkbox.get() == 1:
                return True
        return False

    def delete_check_box(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает текст нажатого чекбокса и ссылку на него
        Если он не является None то удаляет его из скролл фрейма и из списка чекбоксов
        """
        selected_text, checkbox = self.get_selected_check_box()

        if not (checkbox is None):
            checkbox.destroy()
            self.__list_check_boxes.remove(checkbox)

    def get_selected_check_box(self) -> (str, object) or (None, None):
        """
        Обходит список чекбоксов, определяет активный чекбокс если такой имеется и возвращает кортеж из его текста и ссылки на него,
        Если в списке нет активных чекбоксов то возвращает кортеж (None, None)
        :return:
        """
        for checkbox in self.__list_check_boxes:
            if checkbox.get() == 1:
                return checkbox.cget("text"), checkbox
        return None, None

    def __get_count_check_boxes(self):
        """
        :return: Возвращает количество чекбоксов в списке
        """
        return len(self.__list_check_boxes)

    count_check_boxes = property(__get_count_check_boxes)


class ConfigCreateList(ctk.CTkFrame):
    """
    Класс- контейнер для виджетов, которые формируют конфигурацию и составляющие списка покупок,
    Такие как название списка, название товара, категория и его количество, а так же логотип приложения
    """
    def __init__(self, main_window, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__main_window = main_window

        self.__name_shopping_list = None
        self.__name_product = None
        self.__count_product = None
        self.__category_product = None

        self.__label_add_product = None

        self.__list_categories = sld.read_categories_with_json()

        self.__config_logo()
        self.__config_input_fields()
        self.__config_category_list()
        self.__config_add_buttons()
        self.__config_label_add_product()

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.72, rely=0.14)

    def __config_input_fields(self) -> None:
        """
        Формирует в себе поля ввода данных пользователя
        """
        self.__name_shopping_list = ctk.CTkEntry(self, placeholder_text=tt_nsl, placeholder_text_color=ptc_nsl,
                                              width=wh_nsl, height=ht_nsl, fg_color=fgc_nsl, font=ft_nsl, text_color=ptc_nsl)
        self.__name_shopping_list.place(relx=0.036, rely=0.17)

        self.__name_product = ctk.CTkEntry(self, placeholder_text=pht_np, placeholder_text_color=phtc_np,
                                              width=wh_np, height=ht_np, fg_color=fgc_np, font=ft_np, text_color=ptc_nsl)
        self.__name_product.place(relx=0.035, rely=0.45)

        self.__count_product = ctk.CTkEntry(self, placeholder_text=pht_cp, placeholder_text_color=phtc_cp,
                                              width=wh_cp, height=ht_cp, fg_color=fgc_cp, font=ft_cp, text_color=ptc_nsl)
        self.__count_product.place(relx=0.33, rely=0.45)

    def __config_category_list(self) -> None:
        """
        Формирует в себе категории товара
        """
        self.__category_product = ctk.CTkComboBox(self,  text_color=tc_c,  width=wh_c, height=ht_c, fg_color=fgc_c, font=ft_c,
                                        state=st_c, button_color=bc_c, )
        self.__category_product.configure(values=self.__list_categories.get("cs"))
        self.__category_product.place(relx=0.457, rely=0.45)

    def __config_label_add_product(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__label_add_product = ctk.CTkLabel(self, text=tt_apl, font=ft_apl)
        self.__label_add_product.place(relx=0.1, rely=0.75)

    def __config_add_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за добавление нового товара и добавление новой категории, а так же устанавливает их параметры и стили
        """
        self.__add_product_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_api)
        self.__add_product = ctk.CTkButton(self, image=self.__add_product_image, width=wh_apb, height=ht_apb, text=tt_apb,
                                                fg_color=fgc_apb, hover_color=hc_apb)
        self.__add_product.configure(command=self.__main_window.add_product_button_click_handler)
        self.__add_product.place(relx=0.035, rely=0.7)

        self.__add_category_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_aci)
        self.__add_category = ctk.CTkButton(self, image=self.__add_category_image, width=wh_acb, height=ht_acb, text=tt_acb,
                                                fg_color=fgc_acb, hover_color=hc_acb)
        self.__add_category.configure(command=self.__main_window.add_category_button_click_handler)
        self.__add_category.place(relx=0.64, rely=0.45)

    def __get_name_shopping_list(self):
        """
        :return: Возвращает название списка покупок
        """
        return self.__name_shopping_list.get()

    def __get_name_product(self):
        """
        :return: Возвращает название товара покупок
        """
        return self.__name_product.get()

    def __get_count_product(self):
        """
        :return: Возвращает количество товара
        """
        return self.__count_product.get()

    def __get_category_product(self):
        """
        :return: Возвращает категорию товара
        """
        return self.__category_product.get()

    name_shopping_list = property(__get_name_shopping_list)
    name_product = property(__get_name_product)
    count_product = property(__get_count_product)
    category = property(__get_category_product)


class ButtonsMenuCreateList(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, main_window, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__main_window = main_window

        self.__config_buttons_menu()

    def __config_buttons_menu(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы,
        А так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__save_lst = ctk.CTkButton(self, text=tt_s, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                      border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__save_lst.configure(command=self.__main_window.save_button_click_handler)
        self.__save_lst.place(relx=0.035, rely=0.2)

        self.__edit_product = ctk.CTkButton(self, text=tt_e, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                      border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__edit_product.configure(command=self.__main_window.edit_button_click_handler)
        self.__edit_product.place(relx=0.3, rely=0.2)

        self.__del_product = ctk.CTkButton(self, text=tt_d, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                     border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__del_product.configure(command=self.__main_window.del_button_click_handler)
        self.__del_product.place(relx=0.55, rely=0.2)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_c, width=wh_bm, fg_color=fgc_bm,height=ht_bm, text_color=tc_bm,
                                         border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__cancel_btn.configure(command=self.__main_window.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.8, rely=0.2)


class CreateList(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует контейнеры (фреймы), содержащие остальные виджеты страницы,
     А так же содержит основные методы, отвечающие за функционал страницы
    """
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window

        self.__confirmation_request_page = None
        self.__edit_product_page = None
        self.__add_category_page = None

        self.__data_create_list = None
        self.__scroll_create_list = None
        self.__btn_menu_create_list = None

        self.__list_products = []

        self.__config_window()
        self.__config_create_list()
        self.__config_scroll_frame()
        self.__config_buttons_menu()

        self.__load_data = sld.read_data_with_shopping_lists() if sld.check_file_shopping_lists() else {}

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)
        self.resizable(rb_wh, rb_ht)

    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления товаров
        """
        self.__scroll_create_list = ScrollCreateList(self, master=self, width=wh_sf, height=ht_sf, fg_color=fgc_sf, corner_radius=cr_sf)
        self.__scroll_create_list.pack(pady=10, padx=(30, 240))

    def __config_create_list(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления элементов товара, а так же кнопок добавления товара и добавления новой категории
        """
        self.__data_create_list = ConfigCreateList(self, master=self, width=wh_ccl, height=ht_ccl, fg_color=fgc_ccl,
                                                     corner_radius=cr_ccl)
        self.__data_create_list.pack()
        self.__data_create_list.pack_propagate(False)

    def __config_buttons_menu(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления элементов товара, а так же кнопок добавления товара и добавления новой категории
        """
        self.__btn_menu_create_list = ButtonsMenuCreateList(self, master=self, width=w_bm, height=h_bm, fg_color=fg_bm, corner_radius=cr_bm)
        self.__btn_menu_create_list.pack()
        self.__btn_menu_create_list.pack_propagate(False)

    def add_product_button_click_handler(self) -> bool or showerror:
        """
        Обрабатывает клик по кнопке добавления товара в список, при наступлении исключения - выбрасывает окно с ошибкой
        """
        assert self.__data_create_list.name_product != '' and self.__data_create_list.count_product != '' and self.__data_create_list.category != '', showerror('Ошибка', 'Заполните все поля')

        assert self.__data_create_list.count_product.isdigit(), showerror('Ошибка', 'Количество товара может быть только целым числом')

        if Templates.checks_presence_element(self.__data_create_list.name_product, self.__list_products):
            showerror('Ошибка', 'Такой продукт уже есть в списке')
            return

        self.__scroll_create_list.create_check_box(self.__data_create_list.name_product, self.__data_create_list.count_product, self.__data_create_list.category)

        product = [self.__data_create_list.name_product, self.__data_create_list.count_product, self.__data_create_list.category]

        self.__list_products.append(product)

        return True

    def add_category_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления новой категории товара
        """
        self.__add_category_page = AddNewCategory(self)
        self.withdraw()

    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок, при наступлении исключения - выбрасывает окно с ошибкой
        """
        from src.All_lists.all_shoping_lists import AllLists

        assert self.__scroll_create_list.count_check_boxes != 0, showerror('Ошибка', 'Добавьте товар или нажмите "Отмена"')

        assert self.__data_create_list.name_shopping_list != '', showerror('Ошибка', 'Добавьте название списка покупок или нажмите "Отмена"')

        sld.create_folder()

        self.__load_data[self.__data_create_list.name_shopping_list] = self.__list_products

        sld.write_data_in_shopping_lists(self.__load_data)

        if isinstance(self.__main_window, AllLists):
            self.__main_window.scroll_all_lists.add_new_check_box(self.__data_create_list.name_shopping_list)

        self.__main_window.deiconify()

        self.destroy()

    def update_load_data(self, old_text, new_text) -> None:
        """
        Обходит матрицу продуктов, сравнивает полученный текст из чекбокса, если они совпадают то меняет по индесу старый продукт на новый
        :param old_text: Старый текст чекбокса, до редактирования
        :param new_text: Новый текст чекбокса, после редактирования
        """
        old_items = old_text.split(', ')
        new_items = new_text.split(', ')

        for index, elem in enumerate(self.__list_products):
            if elem == old_items:
                self.__list_products[index] = new_items

    def edit_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара, при наступлении исключения - выбрасывает окно с ошибкой
        """
        assert self.__scroll_create_list.count_check_boxes != 0, showerror('Ошибка', 'Список товаров пуст, редактировать нечего')

        if not self.__scroll_create_list.check_selected_check_box():
            showerror('Ошибка', 'Выберите товар для редактирования')
            return

        self.__edit_product_page = AddProduct(self, self.__scroll_create_list)

        self.withdraw()

    def del_target_condition(self) -> None:
        """
        Внутри себя вызывает другую функцию, при помощи которой, получает текст нажатого чекбокса и ссылку на него
        Проверяет текст, если он не является None То входит в условие и удаляет продукт из списка продуктов временной памяти
        """
        selected_text, checkbox = self.__scroll_create_list.get_selected_check_box()

        if not (selected_text is None):
            product_to_remove = selected_text.split(', ')

            for product in self.__list_products:

                if product == product_to_remove:
                    self.__list_products.remove(product)

        return None

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара, при наступлении исключения - выбрасывает окно с ошибкой
        """
        assert self.__scroll_create_list.count_check_boxes != 0, showerror('Ошибка', 'Список товаров пуст, удалять нечего')

        if not self.__scroll_create_list.check_selected_check_box():
            showerror('Ошибка', 'Выберите товар для удаления')
            return

        self.__confirmation_request_page = ConfirmationPage(self, self.__scroll_create_list)

        self.withdraw()

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()
        self.destroy()

    def __get_scroll_frame(self):
        """
        :return: Возвращает ссылку на скролл фрейм
        """
        return self.__scroll_create_list

    def __get_list_products(self):
        """
        :return: Возвращает ссылку на лист продуктов
        """
        return self.__list_products

    def __get_data_create_list(self):
        """
        :return: Возвращает ссылку на data_create_list
        """
        return self.__data_create_list

    data_create_list = property(__get_data_create_list)
    scroll_create_list = property(__get_scroll_frame)
    list_products = property (__get_list_products)
