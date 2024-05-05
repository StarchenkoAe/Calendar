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

        #Кнопки для переключения между месяцами
        self.prev_button = tk.Button(self.calendar_tab, text="<<<", command=self.prev_month)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=5)
        self.next_button = tk.Button(self.calendar_tab, text=">>>", command=self.next_month)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=5)

        #Создаем таблицу с днями месяца
        for week in self.cal:
            row = tk.Frame(self.calendar_tab)
            row.pack(side=tk.TOP, padx=10, pady=5)
            for day in week:
                if day == 0:
                    tk.Label(row, width=4, text=" ").pack(side=tk.LEFT)
                else:
                    #Получаем день недели для текущей даты
                    weekday = datetime(self.year, self.month, day).weekday()
                    #Выделение праздничных дней или сегодняшнего дня
                    if (self.month == 1 and day in [1, 2, 3, 4, 5, 6, 7, 8]) or \
                       (self.month == 2 and day == 23) or \
                       (self.month == 3 and day == 8) or \
                       (self.month == 5 and day == 1) or \
                       (self.month == 5 and day == 9) or \
                       (self.month == 6 and day == 12) or \
                       (self.month == 11 and day == 4) or \
                       (self.month == 1 and day == 7):
                        bg_color = "red"  # Выделение праздничных дней красным
                    elif (self.month == date.today().month) and (day == self.day) and (self.year == date.today().year):
                        bg_color = "blue"  # Выделение сегодняшнего дня синим 
                    else:
                        bg_color = "white"
                    
                    tk.Label(row, width=4, text=day, bg=bg_color).pack(side=tk.LEFT)
      
    def create_info_widgets(self):
        #Информация о календаре
        info_text = "Этот  календарь  отображает  текущий месяц \n"
        info_text +="c выделением  праздничных  дней красным  и \n"
        info_text += "сегодняшнего   дня   синим.  Вы     можете \n"
        info_text += "переключаться  между  месяцами,  используя кнопки <<< или >>>."
        self.info_text = tk.Text(self.info_tab, width=50, height=10, wrap="word")
        self.info_text.insert(tk.END, info_text)
        self.info_text.config(state="disabled")
        self.info_text.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
    #Переключение между месяцами
    def prev_month(self):
        self.month -= 1
        if self.month == 0:
            self.month = 12
            self.year -= 1
        self.update_calendar()

    def next_month(self):
        self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1
        self.update_calendar()

    def update_calendar(self):
        for widget in self.calendar_tab.winfo_children():
            widget.destroy()
        self.cal = calendar.monthcalendar(self.year, self.month)
        self.create_calendar_widgets()    
        
#Создаем основное окно приложения с определенным размером
root = tk.Tk()
root.title("Календарь")
root.geometry("400x300")

#Создаем экземпляр приложения
app = CalendarApp(root)

root.mainloop()      
