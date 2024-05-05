#Импортируем нужные библиотеки
import tkinter as tk   #Для создания пользовательского интерфейса
from tkinter import ttk
from datetime import date, datetime  #Для работы с временем
import calendar #Для работы с функциями календаря

class CalendarApp:
    def __init__(self, parent):
        self.parent = parent
        self.year = date.today().year
        self.month = date.today().month
        self.day = date.today().day
        self.cal = calendar.monthcalendar(self.year, self.month)
        self.create_widgets()

    def create_widgets(self):
        #Создаем основной контейнер для вкладок
        self.tabControl = ttk.Notebook(self.parent)
        self.tabControl.pack(expand=1, fill="both")

        #Вкладка с календарем
        self.calendar_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.calendar_tab, text='Календарь')
        self.create_calendar_widgets()

        #Вкладка с описанием работы календаря
        self.info_tab = ttk.Frame(self.tabControl)
        self.tabControl.add(self.info_tab, text='Помощь')
        self.create_info_widgets()

    def create_calendar_widgets(self):
        #Отображения текущего месяца и года
        russian_month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        self.label = tk.Label(self.calendar_tab, text=russian_month_names[self.month - 1] + " " + str(self.year), font=("Bahnschrift Light", 16))
        self.label.pack()

        #Отображения  дней недели
        days_of_week_label = tk.Label(self.calendar_tab, text="П         В         С         Ч         П         С         В", font=("Bahnschrift Light Condensed", 12))
        days_of_week_label.pack()
