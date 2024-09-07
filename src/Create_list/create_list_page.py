from src.Top_lvl_pages.top_lvl_pages import *
from tkinter.messagebox import showerror
from src.save_and_load_data import SaveAndLoadData as sld
from src.Create_list.config_create_list import *
import customtkinter as ctk
from PIL import Image


class ScrollAddProducts(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для добавления товаров
    """

    def __init__(self, main_window, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__main_window = main_window
        self.__product = None
        self.__count_check_boxes = 0
        self.__list_check_boxes = []

    def create_check_box(self, name_product, count_product, category):

        self.__product = ctk.CTkCheckBox(self, text=f'{name_product}, {count_product}, {category}', font=ft_p,
                                         hover_color=hc_p, fg_color=fgc_p, border_width=bw_p)
        self.__count_check_boxes += 1
        self.__list_check_boxes.append(self.__product)
        self.__product.grid(padx=(10, 0), pady=10)

    def set_new_text_for_check_box(self, checkbox,  new_text):
        if checkbox is not None:
            checkbox.configure(text=new_text)

    def check_selected_check_box(self):
        for checkbox in self.__list_check_boxes:
            if checkbox.get() == 1:
                return True
        return False

    def delete_check_box(self):
        text, checkbox = self.get_selected_check_box()

        for checkbox in self.__list_check_boxes:
            if checkbox.cget("text") == text:
                checkbox.destroy()

        self.__count_check_boxes -= 1

    def get_selected_check_box(self):
        for checkbox in self.__list_check_boxes:
            if checkbox.get() == 1:
                return checkbox.cget("text"), checkbox

    def __get_count_check_boxes(self):
        return self.__count_check_boxes

    count_check_boxes = property(__get_count_check_boxes)


class CreateList(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует контейнеры (фреймы), содержащие остальные виджеты страницы
    """
    def __init__(self, main_window):
        super().__init__()

        self.__main_window = main_window

        self.__name_shopping_list = None
        self.__name_product = None
        self.__count_product = None
        self.__category_product = None

        self.__label_add_product = None

        self.__confirmation_request_page = None
        self.__add_category_page = None
        self.__edit_product_page = None

        self.__scroll_frame = None

        self.__list_products = []
        self.__list_categories = sld.read_categories_with_json()

        self.__config_logo()
        self.__config_input_fields()
        self.__config_category_list()
        self.__config_add_buttons()
        self.__config_label_add_product()
        self.__config_scroll_frame()
        self.__config_buttons_menu()
        self.__config_window()

        if sld.check_file():
            self.__load_data = sld.read_data_with_json()
        else:
            self.__load_data = {}

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)
        self.resizable(rb_wh, rb_ht)

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.72, rely=0.05)

    def __config_input_fields(self) -> None:
        """
        Формирует в себе поля ввода данных пользователя
        """
        self.__name_shopping_list = ctk.CTkEntry(self, placeholder_text=tt_nsl, placeholder_text_color=ptc_nsl,
                                              width=wh_nsl, height=ht_nsl, fg_color=fgc_nsl, font=ft_nsl, text_color=ptc_nsl)
        self.__name_shopping_list.place(relx=0.036, rely=0.05)

        self.__name_product = ctk.CTkEntry(self, placeholder_text=pht_np, placeholder_text_color=phtc_np,
                                              width=wh_np, height=ht_np, fg_color=fgc_np, font=ft_np, text_color=ptc_nsl)
        self.__name_product.place(relx=0.035, rely=0.125)

        self.__count_product = ctk.CTkEntry(self, placeholder_text=pht_cp, placeholder_text_color=phtc_cp,
                                              width=wh_cp, height=ht_cp, fg_color=fgc_cp, font=ft_cp, text_color=ptc_nsl)
        self.__count_product.place(relx=0.33, rely=0.125)

    def __config_category_list(self) -> None:
        """
        Формирует в себе категории товара
        """
        self.__category_product = ctk.CTkComboBox(self,  text_color=tc_c,  width=wh_c, height=ht_c, fg_color=fgc_c, font=ft_c,
                                        state=st_c, button_color=bc_c, )
        self.__category_product.configure(values=self.__list_categories.get("cs"))
        self.__category_product.place(relx=0.457, rely=0.125)

    def __config_label_add_product(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__label_add_product = ctk.CTkLabel(self, text=tt_apl, font=ft_apl)
        self.__label_add_product.place(relx=0.1, rely=0.21)

    def __config_add_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за добавление нового товара и добавление новой категории, а так же устанавливает их параметры и стили
        """
        self.__add_product_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_api)
        self.__add_product = ctk.CTkButton(self, image=self.__add_product_image, width=wh_apb, height=ht_apb, text=tt_apb,
                                                fg_color=fgc_apb, hover_color=hc_apb)
        self.__add_product.configure(command=self.add_product_button_click_handler)
        self.__add_product.place(relx=0.035, rely=0.2)

        self.__add_category_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_aci)
        self.__add_category = ctk.CTkButton(self, image=self.__add_category_image, width=wh_acb, height=ht_acb, text=tt_acb,
                                                fg_color=fgc_acb, hover_color=hc_acb)
        self.__add_category.configure(command=self.add_category_button_click_handler)
        self.__add_category.place(relx=0.64, rely=0.12)

    def __config_buttons_menu(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__save_lst = ctk.CTkButton(self, text=tt_s, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                      border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__save_lst.configure(command=self.save_button_click_handler)
        self.__save_lst.place(relx=0.035, rely=0.85)

        self.__edit_product = ctk.CTkButton(self, text=tt_e, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                      border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__edit_product.configure(command=self.edit_button_click_handler)
        self.__edit_product.place(relx=0.3, rely=0.85)

        self.__del_product = ctk.CTkButton(self, text=tt_d, width=wh_bm, fg_color=fgc_bm, height=ht_bm, text_color=tc_bm,
                                     border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__del_product.configure(command=self.del_button_click_handler)
        self.__del_product.place(relx=0.55, rely=0.85)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_c, width=wh_bm, fg_color=fgc_bm,height=ht_bm, text_color=tc_bm,
                                         border_width=bw_bm, hover_color=hc_bm, font=ft_bm)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.8, rely=0.85)

    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления товаров
        """
        self.__scroll_frame = ScrollAddProducts(self, master=self, width=wh_sp, height=ht_sp, fg_color=fgc_sp, corner_radius=cr_sp)
        self.__scroll_frame.place(relx=0.04, rely=0.35)

    def add_product_button_click_handler(self) -> bool or showerror:
        """
        Обрабатывает клик по кнопке добавления товара в список
        """
        assert self.name_product != '' and self.count_product != '' and self.category != '', showerror('Ошибка', 'Заполните все поля')

        assert self.count_product.isdigit(), showerror('Ошибка', 'Количество товара может быть только целым числом')

        product = [self.name_product, self.count_product, self.category]

        self.__list_products.append(product)

        self.__scroll_frame.create_check_box(self.name_product, self.count_product, self.category)

        return True

    def update_load_data(self, old_text, new_text):
        for i in range(0, len(self.__list_products), 1):

            for s in range(0, len(self.__list_products[i]), 1):

                if f"{self.__list_products[i][0]}, {self.__list_products[i][1]}, {self.__list_products[i][2]}" == old_text:

                    self.__list_products[i][0], self.__list_products[i][1], self.__list_products[i][2] = new_text.split(", ")

                    return

    def add_category_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления новой категории товара
        """
        self.__add_category_page = AddNewCategory(self)
        self.withdraw()

    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        assert self.__scroll_frame.count_check_boxes != 0, showerror('Ошибка', 'Добавьте товар или нажмите "Отмена"')

        assert self.name_shopping_list != '', showerror('Ошибка', 'Добавьте название списка покупок или нажмите "Отмена"')

        sld.create_folder()

        self.__load_data[self.name_shopping_list] = self.__list_products

        sld.write_data_in_json(self.__load_data)

        self.__main_window.deiconify()

        self.destroy()

    def edit_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        assert self.__scroll_frame.count_check_boxes != 0, showerror('Ошибка', 'Список товаров пуст, редактировать нечего')

        if not self.__scroll_frame.check_selected_check_box():
            showerror('Ошибка', 'Выберите товар для редактирования')
            return

        self.__edit_product_page = AddProduct(self, self.__scroll_frame)

        self.withdraw()

    def del_target_product_from_list_products(self):
        text, check_box = self.__scroll_frame.get_selected_check_box()

        for i in range(0, len(self.__list_products), 1):

            for s in range(0, len(self.__list_products[i]), 1):

                if f"{self.__list_products[i][0]}, {self.__list_products[i][1]}, {self.__list_products[i][2]}" == text:
                    del self.__list_products[i]

                    return

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара
        """
        assert self.__scroll_frame.count_check_boxes != 0, showerror('Ошибка', 'Список товаров пуст, удалять нечего')

        if not self.__scroll_frame.check_selected_check_box():
            showerror('Ошибка', 'Выберите товар для удаления')
            return

        print(self.__list_products)

        self.__confirmation_request_page = ConfirmationPage(self, self.__scroll_frame)

        self.withdraw()


    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()
        self.destroy()

    def __get_name_shopping_list(self):
        return self.__name_shopping_list.get()

    def __get_name_product(self):
        return self.__name_product.get()

    def __get_count_product(self):
        return self.__count_product.get()

    def __get_category_product(self):
        return self.__category_product.get()

    def __get_list_products(self):
        return self.__list_products

    name_shopping_list = property(__get_name_shopping_list)
    name_product = property(__get_name_product)
    count_product = property(__get_count_product)
    category = property(__get_category_product)
    list_products = property (__get_list_products)
