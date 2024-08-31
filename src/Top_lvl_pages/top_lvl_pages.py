import customtkinter as ctk
from PIL import Image
from src.Top_lvl_pages.config_top_level_pages import *


class AddNewCategory(ctk.CTkToplevel):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.__input_field = None

        self.__config_logo()
        self.__config_window()
        self.__config_input_field()
        self.__config_buttons()

    def __config_window(self):
        """
        Формирует параметры и стили главного окна приложения
        """
        self.geometry(gt_cw_anc)
        self.title(ttl_cw_anc)
        self.resizable(wh_rzb, ht_rzb)

    def __config_input_field(self):
        """
        Формирует в себе поля ввода данных пользователя
        """
        self.__input_field = ctk.CTkEntry(self, placeholder_text=pht_if, placeholder_text_color=phtc_if,
                                              width=wh_if, height=ht_if, fg_color=fgc_if, font=ft_if)
        self.__input_field.place(relx=0.05, rely=0.2)

    def __config_logo(self):
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.67, rely=0.1)

    def __config_buttons(self):
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__save_btn = ctk.CTkButton(self, text=tt_sb, width=wh_sb, fg_color=fgc_sb, height=ht_sb,
                                           text_color=tc_sb, border_width=bw_sb, hover_color=hc_sb, font=ft_sb)
        self.__save_btn.configure(command=self.save_button_click_handler)
        self.__save_btn.place(relx=0.05, rely=0.7)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb, height=ht_cb,
                                              text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb, font=ft_cb)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.62, rely=0.7)

    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        pass


class AddReminder(AddNewCategory):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title(ttl_ar)


class AddProduct(ctk.CTkToplevel):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__name_product = None
        self.__count_product = None

        self.__config_window()
        self.__config_logo()
        self.__config_input_fields()
        self.__config_buttons_menu()

    def __config_window(self):
        """
        Формирует параметры и стили главного окна приложения
        """
        self.geometry(gt_cw_ap)
        self.title(ttl_cw_ap)

    def __config_input_fields(self):
        """
        Формирует в себе поля ввода данных пользователя
        """
        self.__name_product = ctk.CTkEntry(self, placeholder_text=pht_np, placeholder_text_color=phtc_np,
                                         width=wh_np, height=ht_np, fg_color=fgc_np, font=ft_np)
        self.__name_product.place(relx=0.04, rely=0.2)

        self.__count_product = ctk.CTkEntry(self, placeholder_text=pht_cp, placeholder_text_color=phtc_cp,
                                          width=wh_cp, height=ht_cp, fg_color=fgc_cp, font=ft_cp)
        self.__count_product.place(relx=0.373, rely=0.2)

    def __config_category_list(self):
        """
        Формирует в себе список, доступных по умолчанию, категорий товара
        :return:
        """
        self.__category = ctk.CTkComboBox(self,  text_color=tc_c,  width=wh_c, height=ht_c, fg_color=fgc_c, font=ft_c,
                                        state=st_c, button_color=bc_c)
        self.__category.configure(values=values_c)
        self.__category.place(relx=0.52, rely=0.2)

    def __config_logo(self):
        """
        Формирует параметры и стили главного логотипа приложения
        """
        self.__logo = ctk.CTkImage(light_image=Image.open(path_logo), size=size_l)
        self.__image_label = ctk.CTkLabel(self, image=self.__logo, text=tt_l)
        self.__image_label.place(relx=0.75, rely=0.1)

    def __config_buttons_menu(self):
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__save_btn = ctk.CTkButton(self, text=tt_sb, width=wh_sb, fg_color=fgc_sb,
                                         height=ht_sb, text_color=tc_sb, border_width=bw_sb, hover_color=hc_sb,
                                         font=ft_sb)
        self.__save_btn.configure(command=self.save_button_click_handler)
        self.__save_btn.place(relx=0.04, rely=0.7)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_cb, width=wh_cb, fg_color=fgc_cb,
                                      height=ht_cb, text_color=tc_cb, border_width=bw_cb, hover_color=hc_cb,
                                      font=ft_cb)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.71, rely=0.7)

    def save_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        pass


class ConfirmationPage(ctk.CTkToplevel):
    """
    Класс, описывающий функционал окна верхнего уровня и его виджеты
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__text_label = None

        self.__config_window()
        self.__config_label_confirm()
        self.__config_button_menu()

    def __config_window(self):
        """
        Формирует параметры и стили главного окна приложения
        """
        self.title(ttl_cp)
        self.geometry(gt_cp)

    def __config_label_confirm(self):
        """
        Формирует в себе текст, описывающий назначение окна
        """
        self.__label_confirm = ctk.CTkLabel(self, width=wh_cl, height=ht_cl, text=tt_cl, text_color=tc_cl, font=ft_cl)
        self.__label_confirm.place(relx=0.3, rely=0.1)

    def __config_button_menu(self):
        """
        Формирует в себе кнопки, отвечающие за общий функционал страницы, а так же их обработчики и устанавливает их в указанное место окна, а так же устанавливает его параметры и стили
        """
        self.__confirm_btn = ctk.CTkButton(self, width=wh_cmb, height=ht_cmb, text=tt_cmb, fg_color=fgc_cmb,
                                         text_color=tc_cmb, border_width=bw_cmb, hover_color=hc_cmb, font=ft_cmb)
        self.__confirm_btn.configure(command=self.confirm_button_click_handler)
        self.__confirm_btn.place(relx=0.05, rely=0.6)

        self.__cancel_btn = ctk.CTkButton(self, text=tt_clb, width=wh_clb, fg_color=fgc_clb, height=ht_clb,
                                              text_color=tc_clb, border_width=bw_clb, hover_color=hc_clb, font=ft_clb)
        self.__cancel_btn.configure(command=self.cancel_button_click_handler)
        self.__cancel_btn.place(relx=0.64, rely=0.6)

    def confirm_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке сохранения списка покупок
        """
        pass

    def cancel_button_click_handler(self) -> None:
        """
        Обрабатывает клик по кнопке возврата на предыдущую страницу
        """
        pass

