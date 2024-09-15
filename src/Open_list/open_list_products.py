import customtkinter as ctk
from PIL import Image
from src.Open_list.config_open_list_products import *


class ScrollOpenListProducts(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для работы с добавленными товарами либо для добавления новых
    """
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__config_favorite_button()

    def __config_favorite_button(self) -> None:
        """
        Формирует в себе кнопку, отвечающую за функционал добавления товара в избранное, а так же ее обработчик и устанавливает ее в указанное место окна, а так же устанавливает ее параметры и стили
        """
        self.__image_favorite = ctk.CTkImage(light_image=Image.open(path_favorite_button), size=size_if)

        self._btn_favorite = ctk.CTkButton(self, image=self.__image_favorite, width=wh_bf, height=ht_bf, text=tt_bf,
                                                fg_color=fgc_bf, hover_color=hc_bf)
        self._btn_favorite.configure(command=self.favorite_button_click_handler)
        self._btn_favorite.grid(padx=(10, 0), pady=0, row=0, column=2)

    def add_product_check_box(self, name, count, category):
        product = ctk.CTkCheckBox(self, text=f'{name}, {count}, {category}', font=('Helvetica', 18, 'bold'),
                                  hover_color='#453E3E', fg_color='#434141', border_width=1)
        product.grid(padx=(10, 0), pady=10)

    def favorite_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке добавления товара в список избранного
        """
        pass


class ButtonsMenuOpenList(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__main_window = main_window
        self.__label_add_product = None

        self.__config_label_add_product()
        self.__config_menu_buttons()

    def __config_label_add_product(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__add_product_label = ctk.CTkLabel(self, text_color=tc_apl, text=tt_apl, font=ft_apl)
        self.__add_product_label.place(relx=0.1, rely=0.14)

    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__add_product_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_api)
        self.__add_product = ctk.CTkButton(self, image=self.__add_product_image, width=wh_ap, height=ht_ap, text=tt_ap,
                                             fg_color=fgc_ap, hover_color=hc_ap)
        self.__add_product.configure(command= self.__main_window.add_button_click_handler)
        self.__add_product.place(relx=0.04, rely=0.1)

        self.__edit_product = ctk.CTkButton(self, text=tt_ep, width=wh_ep, fg_color=fgc_ep, height=ht_ep,
                                            text_color=tc_ep, border_width=bw_ep, hover_color=hc_ep, font=ft_ep)
        self.__edit_product.configure(command= self.__main_window.edit_button_click_handler)
        self.__edit_product.place(relx=0.3, rely=0.65)

        self.__filter_products = ctk.CTkButton(self, text=tt_fp, width=wh_fp, fg_color=fgc_fp, height=ht_fp,
                                               text_color=tc_fp, border_width=bw_fp, hover_color=hc_fp, font=ft_fp)
        self.__filter_products.configure(command= self.__main_window.filter_button_click_handler)
        self.__filter_products.place(relx=0.05, rely=0.65)

        self.__del_product = ctk.CTkButton(self, text=tt_dp, width=wh_dp, fg_color=fgc_dp, height=ht_dp,
                                           text_color=tc_dp, border_width=bw_dp, hover_color=hc_dp, font=ft_dp)
        self.__del_product.configure(command= self.__main_window.del_button_click_handler)
        self.__del_product.place(relx=0.55, rely=0.65)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb, height=ht_cb,
                                          text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb, font=ft_cb)
        self.__cancel_btn.configure(command= self.__main_window.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.78, rely=0.65)


class ListProducts(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основные контейнеры (фреймы), содержащие остальные виджеты страницы
    """
    def __init__(self, main_window):
        super().__init__()
        self.__main_window = main_window
        self.__scroll_open_list = None
        self.__open_list_menu_btn = None

        self.__config_window()
        self.__config_logo()
        self.__config_menu_buttons()
        self.__config_scroll_frame()

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl_cw)
        self.geometry(gt_cw)
        self.resizable(rzb_wh, rzb_ht)

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.69, rely=0.05)

    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления товаров
        """
        self.__scroll_open_list = ScrollOpenListProducts(self, master=self, width=wh_sf, height=ht_sf, fg_color=fgc_sf,corner_radius=cr_sf)
        self.__scroll_open_list.place(relx=0.04, rely=0.05)

    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__open_list_menu_btn = ButtonsMenuOpenList(self, master=self, width=wh_mb, height=ht_mb, fg_color=fgc_mb, corner_radius=cr_mb)
        self.__open_list_menu_btn.place(relx=0, rely=0.6)

    def add_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        pass

    def edit_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        pass

    def filter_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        pass

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        self.__main_window.deiconify()
        self.destroy()
