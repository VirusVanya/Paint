from tkinter import *
from tkinter.messagebox import *

# класс Paint
class Paint(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        # Параметры кисти по умолчанию
        self.brush_size = 10
        self.brush_color = "red"
        self.color = "red"
        # Устанавливаем компоненты UI
        self.setUI()

        # Метод рисования на холсте

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

        # Изменение цвета кисти

    def set_color(self, new_color):
        self.color = new_color
        self.change_btn['activebackground']=new_color

        # Изменение размера кисти

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def setUI(self):
        # Устанавливаем название окна
        self.parent.title("Demo Paint")
        # Размещаем активные элементы на родительском окне
        self.pack(fill=BOTH, expand=1)

        self.columnconfigure(7, weight=1)
        self.rowconfigure(2, weight=1)

        # Создаем холст с белым фоном
        self.canv = Canvas(self, bg="white")

        # Приклепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке,
        # и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и
        # заставляем растягиваться при растягивании всего окна

        self.canv.grid(row=2, column=0, columnspan=8, padx=5, pady=5, sticky=E + W + S + N)

        # задаем реакцию холста на нажатие левой кнопки мыши
        self.canv.bind("<B1-Motion>", self.draw)

        # создаем метку для кнопок изменения цвета кисти
        color_lab = Label(self, text="Цвет: ")

        # Устанавливаем созданную метку в первый ряд и первую колонку,
        # задаем горизонтальный отступ в 6 пикселей
        color_lab.grid(row=0, column=0, padx=6)

        # создание кнопки: установка текста кнопки, задание ширины кнопки (10 символов)
        self.red_btn = Button(self, text="Красный", width=9, activebackground = "red", command=lambda: self.set_color("red"))

        # устанавливаем кнопку в первый ряд, вторая колонка
        self.red_btn.grid(row=0, column=1)

        # по аналогии создаем остальные кнопки
        self.green_btn = Button(self, text="Зеленый", width=9, activebackground = "green", command=lambda: self.set_color("green"))
        self.green_btn.grid(row=0, column=2)

        self.blue_btn = Button(self, text="Синий", width=9, activebackground = "blue", command=lambda: self.set_color("blue"))
        self.blue_btn.grid(row=0, column=3)

        self.black_btn = Button(self, text="Черный", width=9, activebackground = "black", activeforeground = "white", command=lambda: self.set_color("black"))
        self.black_btn.grid(row=0, column=4)

        self.white_btn = Button(self, text="Белый", width=9, activebackground = "white", command=lambda: self.set_color("white"))
        self.white_btn.grid(row=0, column=5)

        self.your_color = Entry(self, width=12)
        self.your_color.place(x=717, y=3)

        # Создаем метку для кнопок изменения размера кисти
        size_lab = Label(self, text="Размер кисти: ")
        size_lab.grid(row=1, column=0, padx=5)
        self.two_btn = Button(self, text="2x", width=9, command=lambda: self.set_brush_size(2))
        self.two_btn.grid(row=1, column=1)

        self.five_btn = Button(self, text="5x", width=9, command=lambda: self.set_brush_size(5))
        self.five_btn.grid(row=1, column=2)

        self.seven_btn = Button(self, text="7x", width=9, command=lambda: self.set_brush_size(7))
        self.seven_btn.grid(row=1, column=3)

        self.ten_btn = Button(self, text="10x", width=9, command=lambda: self.set_brush_size(10))
        self.ten_btn.grid(row=1, column=4)

        self.twenty_btn = Button(self, text="20x", width=9, command=lambda: self.set_brush_size(20))
        self.twenty_btn.grid(row=1, column=5)

        self.fifty_btn = Button(self, text="50x", width=9, command=lambda: self.set_brush_size(50))
        self.fifty_btn.grid(row=1, column=6, sticky=W)

        self.change_btn = Button(self, text="Изменить", width=9, command=lambda: self.set_color(self.your_color.get()))
        self.change_btn.grid(row=1, column=7, sticky=W)

        self.clear_btn = Button(self, text="Очистить", width=9, command=lambda: self.canv.delete("all"))
        self.clear_btn.grid(row=0, column=6, sticky=W)
    
    def dark_win(self):
        self.your_color['bg']='black'
        self.red_btn['bg']='black'
        self.green_btn['bg']='black'
        self.blue_btn['bg']='black'
        self.black_btn['bg']='black'
        self.white_btn['bg']='black'
        self.two_btn['bg']='black'
        self.five_btn['bg']='black'
        self.seven_btn['bg']='black'
        self.ten_btn['bg']='black'
        self.twenty_btn['bg']='black'
        self.fifty_btn['bg']='black'
        self.change_btn['bg']='black'
        self.clear_btn['bg']='black'

        self.your_color['fg']='white'
        self.red_btn['fg']='white'
        self.green_btn['fg']='white'
        self.blue_btn['fg']='white'
        self.black_btn['fg']='white'
        self.white_btn['fg']='white'
        self.two_btn['fg']='white'
        self.five_btn['fg']='white'
        self.seven_btn['fg']='white'
        self.ten_btn['fg']='white'
        self.twenty_btn['fg']='white'
        self.fifty_btn['fg']='white'
        self.change_btn['fg']='white'
        self.clear_btn['fg']='white'

    def light_win(self):
        self.your_color['bg']='white'
        self.red_btn['bg']='#d9d9d9'
        self.green_btn['bg']='#d9d9d9'
        self.blue_btn['bg']='#d9d9d9'
        self.black_btn['bg']='#d9d9d9'
        self.white_btn['bg']='#d9d9d9'
        self.two_btn['bg']='#d9d9d9'
        self.five_btn['bg']='#d9d9d9'
        self.seven_btn['bg']='#d9d9d9'
        self.ten_btn['bg']='#d9d9d9'
        self.twenty_btn['bg']='#d9d9d9'
        self.fifty_btn['bg']='#d9d9d9'
        self.change_btn['bg']='#d9d9d9'
        self.clear_btn['bg']='#d9d9d9'

        self.your_color['fg']='black'
        self.red_btn['fg']='black'
        self.green_btn['fg']='black'
        self.blue_btn['fg']='black'
        self.black_btn['fg']='black'
        self.white_btn['fg']='black'
        self.two_btn['fg']='black'
        self.five_btn['fg']='black'
        self.seven_btn['fg']='black'
        self.ten_btn['fg']='black'
        self.twenty_btn['fg']='black'
        self.fifty_btn['fg']='black'
        self.change_btn['fg']='black'
        self.clear_btn['fg']='black'

# выход из программы  
def close_win():
  if askyesno("Выход", "Вы уверены?"):
    root.destroy()

# вывод справки    
def about():
  showinfo("Demo Paint", "Простейшая рисовалка от сайта: https://it-black.ru")
  
# функция для создания главного окна
def main():
    global root
    root = Tk()
    root.geometry("820x600+300+300")
    app = Paint(root)
    
    m = Menu(root)
    root.config(menu=m)

    fm = Menu(m)
    m.add_cascade(label="Файл", menu=fm)
    fm.add_command(label="Темная тема", command=app.dark_win)
    fm.add_command(label="Светлая тема", command=app.light_win)
    fm.add_command(label="Выход", command=close_win)

    hm = Menu(m)
    m.add_cascade(label="Справка", menu=hm)
    hm.add_command(label="О программе", command=about)
    root.mainloop()

if __name__ == "__main__":
    main()