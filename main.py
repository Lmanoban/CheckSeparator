from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.picker import MDDatePicker
import datetime
import os
import webbrowser

KV = open('app_interface.kv', 'r').read()
result_sum = 0
peoples = 1
sum_of_check = 0


class ContentNavigationDrawer(BoxLayout):
    """Класс реализации контента для навигации.

    """
    pass


class ItemDrawer(OneLineIconListItem):
    """Свойства модуля kivy.properties.

    """
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    """Цвет текста навигационного меню

    """
    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class Tab(MDFloatLayout, MDTabsBase):
    """Класс реализации контента для вкладок.

    """
    pass


class ItemTable(BoxLayout):
    """Свойства модуля kivy.properties

    """
    num = StringProperty()
    date = StringProperty()
    name = StringProperty()
    res_sum = StringProperty()
    percent = StringProperty()
    color = ListProperty()


class CheckSeparatorApp(MDApp):
    """Приложение

    Тело основного приложения, воспроизводящее расчеты и заполняющее таблицу.

    """
    title = "Check Separator"
    by_who = "by Mihail Podoshevskiy"

    def __init__(self, **kwargs):
        """Дизайн

        Воспроизводит дизайн окон приложения.

        """
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.date_dialog = MDDatePicker(
            callback=self.get_date,
            background_color=(0.1, 0.1, 0.1, 1.0),
        )

    def get_date(self, date):
        """Дата и время

        """
        print(date)
        self.screen.ids.start_date.text = date.strftime("%d-%m-%Y")

    def build(self):
        """Окно приложения

        Возвращает рабочее окно приложения screen.

        """
        return self.screen

    def on_start(self):
        """Стартовые значениея

        Задает стартовые значения для полей ввода данных приложения.

        """
        self.screen.ids.start_date.text = datetime.date.today().strftime("%d-%m-%Y")
        self.screen.ids.total_score.text = "0"
        self.screen.ids.numerous_of_people.text = "0"
        self.screen.ids.name.text = "Name"
        self.screen.ids.cash.text = "0"
        self.save_in_cache_date()
        self.screen.ids.table_list.add_widget(
            ItemTable(
                color=(0.2, 0.2, 0.2, 0.2),
                num="№",
                name="Name",
                res_sum="Сумма",
                percent="Процент от счета",
            )
        )

    def calc_table(self, *args):
        """Сложение

        Сложения суммы за купленные товары одного человека.

        """
        global result_sum
        global sum_of_check
        try:
            start_sum = self.screen.ids.cash.text
            start_sum = float(start_sum)
            result_sum += start_sum
            sum_of_check += start_sum
        except ValueError:
            self.screen.ids.cash.text = "The price cannot be literal"

    def calc_table_close(self, *args, **kwargs):
        """Таблица

        Заполняет строки таблицы полученными данными и обновляет счет для
        суммирования следующего человека.

        """
        global result_sum
        global peoples
        global sum_of_check
        try:
            numerous_of_people = self.screen.ids.numerous_of_people.text
            numerous_of_people = int(numerous_of_people)
            total_score = self.screen.ids.total_score.text
            total_score = float(total_score)
            try:
                if numerous_of_people > 0:
                    name_of_people = self.screen.ids.name.text
                    if peoples != numerous_of_people + 1:
                        if peoples % 2 != 0:
                            row_color = (1, 1, 1, 1)
                            per_cent = (result_sum / total_score) * 100
                            self.screen.ids.table_list.add_widget(
                                ItemTable(
                                    color=row_color,
                                    num=str(peoples),
                                    name=name_of_people,
                                    res_sum=str(result_sum),
                                    percent=f"{per_cent:.1f}%",
                                )
                            )
                            self.save_in_cache()
                            peoples += 1
                            result_sum = 0
                        else:
                            per_cent = (result_sum / total_score) * 100
                            row_color = (0.2, 0.2, 0.2, 0.1)
                            self.screen.ids.table_list.add_widget(
                                ItemTable(
                                    color=row_color,
                                    num=str(peoples),
                                    name=name_of_people,
                                    res_sum=str(result_sum),
                                    percent=f"{per_cent:.1f}%",
                                )
                            )
                            self.save_in_cache()
                            peoples += 1
                            result_sum = 0
                else:
                    self.screen.ids.numerous_of_people.text = "0"
            except ZeroDivisionError:
                if numerous_of_people > 0:
                    name_of_people = self.screen.ids.name.text
                    if peoples != numerous_of_people + 1:
                        if peoples % 2 != 0:
                            row_color = (1, 1, 1, 1)
                            self.screen.ids.table_list.add_widget(
                                ItemTable(
                                    color=row_color,
                                    num=str(peoples),
                                    name=name_of_people,
                                    res_sum=str(result_sum),
                                )
                            )
                            self.save_in_cache_zero()
                            peoples += 1
                            result_sum = 0
                        else:
                            row_color = (0.2, 0.2, 0.2, 0.1)
                            self.screen.ids.table_list.add_widget(
                                ItemTable(
                                    color=row_color,
                                    num=str(peoples),
                                    name=name_of_people,
                                    res_sum=str(result_sum),
                                )
                            )
                            self.save_in_cache_zero()
                            peoples += 1
                            result_sum = 0
                else:
                    self.screen.ids.numerous_of_people.text = "0"
        except ValueError:
            self.screen.ids.numerous_of_people.text = "0"
            self.screen.ids.total_score.text = "0"

    def clear_result_list(self, *args):
        """Чистка списка

        Очищает созданный список при необходимости с возможностью продолжить
        работу с приложением.

        """
        global peoples
        global result_sum
        global sum_of_check
        self.screen.ids.table_list.clear_widgets()
        peoples = 1
        result_sum = 0
        sum_of_check = 0
        self.screen.ids.table_list.add_widget(
            ItemTable(
                color=(0.2, 0.2, 0.2, 0.2),
                num="№",
                name="Name",
                res_sum="Сумма",
                percent="Процент от счета",
            )
        )

    def save_in_cache(self):
        name_of_people = self.screen.ids.name.text
        total_score = self.screen.ids.total_score.text
        total_score = float(total_score)
        per_cent = (result_sum / total_score) * 100
        with open("cache.txt", "r+") as inf:
            inf.seek(0, 2)
            inf.write(str(peoples)+" ")
            inf.write(str(name_of_people)+" ")
            inf.write(str(result_sum)+" ")
            inf.write(f"{per_cent:.1f}%"+"\n")

    def save_in_cache_zero(self):
        """Запись данных

        Записывает данны полученные во время использования в файл cache.txt.

        """
        name_of_people = self.screen.ids.name.text
        with open("cache.txt", "r+") as inf:
            inf.seek(0, 2)
            inf.write(str(peoples) + " ")
            inf.write(str(name_of_people) + " ")
            inf.write(str(result_sum) + "\n")

    def save_in_cache_date(self):
        """Запись даты

        Записывает дату запуска приложения в файл cache.txt.

        """
        with open("cache.txt", "r+") as inf:
            inf.seek(0, 2)
            inf.write(self.screen.ids.start_date.text+"\n")

    def read_cache_doc(self):
        """Чтение cach'a

        Вызывает файл cache.txt в отдельное окно.

        """
        os.system("start " + "cache.txt")

    def author_link(self):
        webbrowser.open("https://github.com/Lmanoban", new=2)

    def code_link(self):
        webbrowser.open("https://github.com/Lmanoban/CheckSeparator", new=2)


CheckSeparatorApp().run()
