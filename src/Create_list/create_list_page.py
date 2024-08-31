from tkinter.messagebox import showerror
from src.save_and_load_data import *
from src.Top_lvl_pages.top_lvl_pages import *
from src.Create_list.config_create_list import *
import customtkinter as ctk
from PIL import Image


class MainFrame(ctk.CTkFrame):
    class ScrollAddProducts(ctk.CTkScrollableFrame):
        """
        Класс- контейнер, формирует область со скролом для добавления товаров
        """

        def __init__(self, master, name_product, count_product, category, **kwargs):
            super().__init__(master, **kwargs)
            self.product = None

            self.name_product = name_product
            self.count_product = count_product
            self.category = category

        def create_check_box(self):
            print(self.name_product)

            print(self.count_product)

            print(self.category)

            self.product = ctk.CTkCheckBox(self, text=f'{self.name_product}, {self.count_product}, {self.category}',
                                      font=('Helvetica', 18, 'bold'),
                                      hover_color='#453E3E', fg_color='#434141', border_width=1)

            self.product.grid(padx=(10, 0), pady=10)

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__name_shopping_list = None
        self.__name_product = None
        self.__count_product = None
        self.__category_product = None
        self.__label_add_product = None
        self.__confirmation_request = None

        self.__add_category_page = None
        self.__edit_product_page = None

        self.__config_logo()
        self.__config_input_fields()
        self.__config_category_place()
        self.__config_add_buttons()
        self.__config_label_add_product()
        self.__config_buttons_menu()
        self.__config_scroll_frame()

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
        self.__name_product.place(relx=0.035, rely=0.12)

        self.__count_product = ctk.CTkEntry(self, placeholder_text=pht_cp, placeholder_text_color=phtc_cp,
                                              width=wh_cp, height=ht_cp, fg_color=fgc_cp, font=ft_cp, text_color=ptc_nsl)
        self.__count_product.place(relx=0.33, rely=0.12)

    def __config_category_place(self) -> None:
        """
        Формирует в себе категории товара
        """
        self.__category_product = ctk.CTkComboBox(self,  text_color=tc_c,  width=wh_c, height=ht_c, fg_color=fgc_c, font=ft_c,
                                        state=st_c, button_color=bc_c, )
        self.__category_product.configure(values=val_c)
        self.__category_product.place(relx=0.457, rely=0.12)

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
        self.__scroll_frame = self.ScrollAddProducts(self, width=wh_sp, height=ht_sp, fg_color=fgc_sp, corner_radius=cr_sp)
        self.__scroll_frame.pack(pady=250, padx=(30, 240))

    def add_product_button_click_handler(self) -> bool or showerror:
        """
        Обрабатывает клик по кнопке добавления товара в список
        """

        print(self.name_product)

        print(self.count_product)

        print(self.category)

        assert self.name_product != '' and self.count_product != '' and self.category != '', showerror('Ошибка', 'Заполните все поля')

        assert self.count_product.isdigit(), showerror('Ошибка', 'Количество товара может быть только целым числом')

        scroll = MainFrame.ScrollAddProducts(self, self.name_product, self.count_product, self.category)
        scroll.create_check_box()
        return True

    def add_category_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления новой категории товара
        """
        if self.__add_category_page is None or not self.__add_category_page.winfo_exists():
            self.__add_category_page = AddNewCategory(self)

        self.__add_category_page.focus()

    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """

        SaveAndLoadData.write_data_with_json()

    def edit_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        if self.__edit_product_page is None or not self.__edit_product_page.winfo_exists():
            self.__edit_product_page = AddProduct(self)

        self.__edit_product_page.focus()

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        pass

    def __get_name_shopping_list(self):
        return self.__name_shopping_list.get()

    def __get_name_product(self):
        return self.__name_product.get()

    def __get_count_product(self):
        return self.__count_product.get()

    def __get_category_product(self):
        return self.__category_product.get()

    name_shopping_list = property(__get_name_shopping_list)
    name_product = property(__get_name_product)
    count_product = property(__get_count_product)
    category = property(__get_category_product)


class AddList(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует контейнеры (фреймы), содержащие остальные виджеты страницы
    """

    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__config_main_frame()

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)
        self.resizable(rb_wh, rb_ht)

    def __config_main_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления элементов товара, а так же кнопок добавления товара и добавления новой категории
        """
        self.__main_frame = MainFrame(self, width=wh_slc, height=ht_slc, fg_color=fgc_slc, corner_radius=cr_slc)
        self.__main_frame.pack()
        self.__main_frame.pack_propagate(False)



