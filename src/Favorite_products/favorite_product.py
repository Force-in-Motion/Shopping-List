import customtkinter as ctk
from PIL import Image
from src.Favorite_products.config_favorite_products import *


class ScrollFavoriteProducts(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для добавления товаров
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def shows_purchase_history(self, name):
        """
        Переделать! Временный метод для проверки добавления товара в избранное
        """
        product = ctk.CTkCheckBox(self, text=f'{name}', font=('Helvetica', 18, 'bold'),
                                  hover_color='#453E3E', fg_color='#434141', border_width=1)
        product.grid(padx=(10, 0), pady=10)


class ButtonMenuFavoriteProducts(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__add_list_label = None
        self.__config_label_add_product()
        self.__config_buttons_menu()

    def __config_label_add_product(self) -> None:
        """
        Формирует в себе текст, описывающий функционал кнопки добавления нового товара
        """
        self.__label_add_list = ctk.CTkLabel(self, text_color=tc_all, text=tt_all, font=ft_all)
        self.__label_add_list.place(relx=0.1, rely=0.14)

    def __config_buttons_menu(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__add_list_image_button = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_ali)
        self.__add_list = ctk.CTkButton(self, image=self.__add_list_image_button, width=wh_alb, height=ht_alb,
                                            text=tt_alb, fg_color=fgc_alb, hover_color=hc_alb)
        self.__add_list.configure(command=self.add_button_click_handler)
        self.__add_list.place(relx=0.04, rely=0.1)

        self.__del_product = ctk.CTkButton(self, text=tt_db, width=wh_db, fg_color=fgc_db, height=ht_db, text_color=tc_db,
                                       border_width=bw_db, hover_color=hc_db, font=ft_db)
        self.__del_product.configure(command=self.del_button_click_handler)
        self.__del_product.place(relx=0.05, rely=0.65)

        self.__clear_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb, height=ht_cb, text_color=tc_cb,
                                         border_width=bw_cb, hover_color=hc_cb, font=ft_cb)
        self.__clear_btn.configure(command=self.clear_button_click_handler)
        self.__clear_btn.place(relx=0.4, rely=0.65)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cab, width=wh_cab, fg_color=fgc_cab, height=ht_cab,
                                           text_color=tc_cab, border_width=bw_cab, hover_color=hc_cab, font=ft_cab)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.75, rely=0.65)

    def add_button_click_handler(self):
        """
        Обрабатывает клик по кнопке добавления товара
        """
        pass

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления выделенного товара
        """
        pass

    def clear_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления всего товара в избранном
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата в предыдущее меню
        """
        pass


class FavoriteProducts(ctk.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__config_logo()
        self.__config_scroll_frame()
        self.__config_buttons_frame()

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.69, rely=0.05)

    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления покупок
        """
        self.__scroll_frame = ScrollFavoriteProducts(self, width=wh_sp, height=ht_sp, fg_color=fgc_sp, corner_radius=cr_sp)
        self.__scroll_frame.place(relx=0.04, rely=0.05)

    def __config_buttons_frame(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__menu_btn = ButtonMenuFavoriteProducts(self, width=wh_bm, height=ht_bm, fg_color=fgc_bm, corner_radius=cr_bm)
        self.__menu_btn.place(relx=0, rely=0.64)

