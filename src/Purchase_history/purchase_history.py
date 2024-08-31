import customtkinter as ctk
from PIL import Image
from src.Purchase_history.config_purchase_history import *


class ScrollPurchaseHistory(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для работы с добавленными товарами
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def shows_purchase_history(self, name):
        product = ctk.CTkCheckBox(self, text=f'{name}', font=('Helvetica', 18, 'bold'),
                                  hover_color='#453E3E', fg_color='#434141', border_width=1)
        product.grid(padx=(10, 0), pady=10)


class ButtonsMenuPurchaseHistory(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__config_menu_buttons()

    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__del_product = ctk.CTkButton(self, text=tt_dp, width=wh_dp, fg_color=fgc_dp, height=ht_dp,
                                           text_color=tc_dp, border_width=bw_dp, hover_color=hc_dp, font=ft_dp)
        self.__del_product.configure(command=self.del_button_click_handler)
        self.__del_product.place(relx=0.05, rely=0.5)

        self.__clear_history = ctk.CTkButton(self, text=tt_ch, width=wh_ch, fg_color=fgc_ch, height=ht_ch,
                                             text_color=tc_ch, border_width=bw_ch, hover_color=hc_ch, font=ft_ch)
        self.__clear_history.configure(command=self.clear_button_click_handler)
        self.__clear_history.place(relx=0.4, rely=0.5)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb,
                                        height=ht_cb, text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb,
                                        font=ft_cb)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.75, rely=0.5)

    def del_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления товара
        """
        pass

    def clear_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования товара
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        pass


class PurchaseHistory(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основные контейнеры (фреймы), содержащие остальные виджеты страницы
    """
    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__config_logo()
        self.__config_scroll_frame()
        self.__config_menu_buttons()

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
        self.logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.image_label = ctk.CTkLabel(self, image=self.logo, text=tt_l)
        self.image_label.place(relx=0.69, rely=0.05)

    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления товаров
        """
        self.__scroll_frame = ScrollPurchaseHistory(self, width=wh_sf, height=ht_sf, fg_color=fgc_sf, corner_radius=cr_sf)
        self.__scroll_frame.place(relx=0.04, rely=0.05)

    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__menu_btn = ButtonsMenuPurchaseHistory(self, width=wh_mb, height=ht_mb, fg_color=fgc_mb, corner_radius=cr_mb)
        self.__menu_btn.place(relx=0, rely=0.75)
