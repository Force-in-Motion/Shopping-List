import customtkinter as ctk
from src.All_lists.config_all_lists import *
from PIL import Image
import sys


class ScrollAddList(ctk.CTkScrollableFrame):
    """
    Класс- контейнер, формирует область со скролом для добавления списков покупок
    """
    def __init__(self, master,  **kwargs):
        super().__init__(master, **kwargs)
        self.__shopping_list = None

    def add_shoping_list(self, name):
        self.__shopping_list = ctk.CTkCheckBox(self, text=f'{name}', font=('Helvetica', 18, 'bold'),
                                  hover_color='#453E3E', fg_color='#434141', border_width=1)
        self.__shopping_list.grid(padx=(10, 0), pady=10)


class ButtonsMenuAddList(ctk.CTkFrame):
    """
    Класс- контейнер, формирует область с кнопками, отвечающими за функционал страницы
    """
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__label_add_list = None

        self.__config_label_add_list()
        self.__config_add_list_button()
        self.__config_menu_buttons()

    def __config_label_add_list(self) -> None:
        """
        Формирует в себе Лейбл - текстовую строку, отвечающую за описание кнопки добавления списка покупок, а так же устанавливает ее параметры и стили
        """
        self.__label_add_list = ctk.CTkLabel(self, text_color=tc, text=tt_lal, font=ft_lal)
        self.__label_add_list.place(relx=0.1, rely=0.14)

    def __config_add_list_button(self) -> None:
        """
        Формирует в себе кнопку, отвечающую за добавление списка покупок, а так же ее обработчик и устанавливает ее в указанное место окна, а так же устанавливает ее параметры и стили
        """
        self.__add_list_image = ctk.CTkImage(light_image=Image.open(path_round_button), size=size_alb)
        self.__add_list = ctk.CTkButton(self, image=self.__add_list_image, width=wh_alb, height=ht_alb, text=tt_alb, fg_color=fgc_alb, hover_color=hc_alb)
        self.__add_list.place(relx=0.04, rely=0.1)
        self.__add_list.configure(command=self.add_list_button_click_handler)

    def __config_menu_buttons(self) -> None:
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__open_list = ctk.CTkButton(self, text=ol_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                         border_width=bw_m, hover_color=hc_m,font=ft_m)
        self.__open_list.place(relx=0.05, rely=0.65)
        self.__open_list.configure(command=self.open_list_button_click_handler)

        self.__edit_list = ctk.CTkButton(self, text=el_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                         border_width=bw_m, hover_color=hc_m, font=ft_m)
        self.__edit_list.place(relx=0.3, rely=0.65)
        self.__edit_list.configure(command=self.edit_list_button_click_handler)

        self.__del_list = ctk.CTkButton(self, text=dl_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                        border_width=bw_m, hover_color=hc_m, font=ft_m)
        self.__del_list.place(relx=0.55, rely=0.65)
        self.__del_list.configure(command=self.del_list_button_click_handler)

        self.__cancel_btn = ctk.CTkButton(self, text=cl_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                       border_width=bw_m, hover_color=hc_m, font=ft_m)
        self.__cancel_btn.place(relx=0.78, rely=0.65)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)

        self.__reminder_btn = ctk.CTkButton(self, text=rr_tt, width=wh_m, fg_color=fgc_m, height=ht_m, text_color=tc_m,
                                        border_width=bw_m, hover_color=hc_m, font=ft_m)
        self.__reminder_btn.place(relx=0.78, rely=0.12)
        self.__reminder_btn.configure(command=self.reminder_button_click_handler)

    def add_list_button_click_handler(self, name) -> None:
        """
        Обрабатывает клик по кнопке добавления список покупок
        """
        pass

    def open_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке открытия списка покупок
        """
        pass

    def edit_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке редактирования списка покупок
        """
        pass

    def del_list_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке удаления списка покупок
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на главную страницу
        """

    def reminder_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке утановка напоминания
        """
        pass


class AllLists(ctk.CTkToplevel):
    """
    Мэйн класс страницы, в себе формирует основной контейнер (фрейм), содержащий остальные виджеты страницы
    """
    def __init__(self):
        super().__init__()
        self.__config_window()
        self.__config_scroll_frame()
        self.__config_menu_buttons()
        self.__config_logo()

    def __config_window(self) -> None:
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl)
        self.geometry(gt)
        self.resizable(rsb_wh, rsb_ht)

    def __config_scroll_frame(self) -> None:
        """
        Формирует параметры и стили контейнера для добавления спсисков покупок
        """
        self.__scroll_frame = ScrollAddList(self, width=wh_sf, height=ht_sf, fg_color=fgc_sf, corner_radius=cr_sf)
        self.__scroll_frame.place(relx=0.04, rely=0.05)

    def __config_menu_buttons(self) -> None:
        """
        Формирует параметры и стили контейнера кнопок
        """
        self.__buttons_frame = ButtonsMenuAddList(self, width=wh_bf, height=ht_bf, fg_color=fgc_bf, corner_radius=cr_sf)
        self.__buttons_frame.place(relx=0, rely=0.6)

    def __config_logo(self) -> None:
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.69, rely=0.05)



