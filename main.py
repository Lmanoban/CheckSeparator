# from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ListProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList

from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout

# from kivymd.font_definitions import fonts
# from kivymd.icon_definitions import md_icons

# from kivymd.uix.menu import MDDropdownMenu
# from kivy.clock import Clock

from kivymd.uix.picker import MDDatePicker
import datetime
# import calendar
import os

KV = '''
# https://stackoverflow.com/questions/65698145/kivymd-tab-name-containing-icons-and-text
# this import will prevent disappear tabs through some clicks on them)))
#:import md_icons kivymd.icon_definitions.md_icons
#:import fonts kivymd.font_definitions.fonts

# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color: "Custom"
    on_release: self.parent.set_color_item(self)

    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color


<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/526.png"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        DrawerList:
            id: md_list



Screen:

    MDNavigationLayout:

        ScreenManager:

            Screen:
                           
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: app.title
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: 0, 0, 0, 1

                    MDTabs:
                        id: tabs
                        height: "48dp"
                        tab_indicator_anim: False
                        background_color: 0.1, 0.1, 0.1, 1
                        
                        Tab:
                            id: tab1
                            name: 'tab1'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['calculator-variant']}[/size][/font] Check Separator"
                            
                            BoxLayout:
                                orientation: 'vertical'
                                padding: "10dp"

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calendar-month"

                                    MDTextField:
                                        id: start_date
                                        on_focus: if self.focus: app.date_dialog.open()
                                
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "cash"

                                    MDTextField:
                                        hint_text: "Enter total score"
                                        id: total_score
                                        name: "total score"
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account-supervisor"

                                    MDTextField:
                                        hint_text: "Enter numerous of people(only positive value)"
                                        id: numerous_of_people
                                        name: "numerous of people"
                                        
                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "account" 

                                    MDTextField:
                                        hint_text: "Enter person name"
                                        id: name
                                        name: 'name'

                                BoxLayout:
                                    orientation: 'horizontal'

                                    MDIconButton:
                                        icon: "calculator-variant" 

                                    MDTextField:
                                        hint_text: "Enter cost of meal then push button"
                                        id: cash
                                        name: 'cash'
                                        
                                    MDIconButton:
                                        icon: "gesture-tap-button"
                                        on_release: app.calc_table(*args)
                                        
                                    MDIconButton:
                                        icon: "stop-circle"
                                        on_release: app.calc_table_close(*args)
                                        
                                BoxLayout:
                                    orientation: 'horizontal'
                                    
                                    MDRectangleFlatIconButton:
                                        icon: "clipboard-text-off"
                                        text: "Clear Result List"
                                        theme_text_color: "Custom"
                                        text_color: 0.1, 0.1, 0.1, 1.0
                                        line_color: 0.1, 0.1, 0.1, 1.0
                                        icon_color: 0.1, 0.1, 0.1, 1.0
                                        on_release: app.clear_result_list(*args)

                        Tab:
                            id: tab2
                            name: 'tab2'
                            text: f"[size=20][font={fonts[-1]['fn_regular']}]{md_icons['table-large']}[/size][/font] Result List"
                            
                            BoxLayout:
                                orientation: "vertical"
                                padding: "10dp"
                                                             
                                BoxLayout:
                                    size_hint_y: .1
                                    size_hint_x: 1
                                    orientation: "vertical"
                                    padding: "10dp"
                                        
                                    MDLabel:
                                        halign: "center"
                                        text: "Result List"
                                                                       
                                BoxLayout:
                                    size_hint_y: .1
                                    size_hint_x: 1
                                    orientation: "vertical"
                                    padding: "10dp"

                                    MDIcon:
                                        halign: "center"
                                        icon: "clipboard-list"
                                
                                BoxLayout:
                                    orientation: "vertical"
                                    padding: "10dp"

                                    ScrollView:

                                        MDList:
                                            id: table_list
                                            
                                BoxLayout:  
                                    orientation: 'horizontal'
                                    
                                    MDRectangleFlatIconButton:
                                        pos_hint: {"center_x": .5}
                                        icon: "cached"
                                        text: "Read cache log"
                                        theme_text_color: "Custom"
                                        text_color: 0.1, 0.1, 0.1, 1.0
                                        line_color: 0.1, 0.1, 0.1, 1.0
                                        icon_color: 0.1, 0.1, 0.1, 1.0
                                        on_release: app.read_cache_doc()
                                        
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer
                
<ItemTable>:
    size_hint_y: None
    height: "42dp"

    canvas:
        Color:
            rgba: root.color
        Rectangle:
            size: self.size
            pos: self.pos

    MDLabel:
        text: root.num
        halign: "center"
    MDLabel:
        text: root.name
        halign: "center"
    MDLabel:
        text: root.date
        halign: "center"
    MDLabel:
        text: root.res_sum
        halign: "center"
    MDLabel:
        text: root.percent
        halign: "center"
                        
'''

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

        icons_item_menu_lines = {
            "account-cowboy-hat": "About author",
            "github": "Source code",
        }
        for icon_name in icons_item_menu_lines.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name,
                           text=icons_item_menu_lines[icon_name])
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
            print(result_sum)
            print(sum_of_check)
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
        print(result_sum)
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
                            print(peoples)
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
                            print(peoples)
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
                            print(peoples)
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
                            print(peoples)
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
        name_of_people = self.screen.ids.name.text
        with open("cache.txt", "r+") as inf:
            inf.seek(0, 2)
            inf.write(str(peoples) + " ")
            inf.write(str(name_of_people) + " ")
            inf.write(str(result_sum) + "\n")

    def save_in_cache_date(self):
        with open("cache.txt", "r+") as inf:
            inf.seek(0, 2)
            inf.write(self.screen.ids.start_date.text+"\n")

    def read_cache_doc(self):
        # with open("cache.txt") as inf:
        #     inf.read()
        # my_file = open("cache.txt")
        # return my_file
        os.system("start " + "cache.txt")


CheckSeparatorApp().run()
