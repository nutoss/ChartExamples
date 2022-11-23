
#Примеры построения графиков
import tkinter as tk

#Функция закрытия программы
def do_close():
   window.destroy()


#Создание главного цикла
window=tk.Tk()
window.geometry("450x450")
window.title ("Примеры построения графиков")

#Добавление метки заголовка
lbtTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica',16, 'bold'), fg = '#0000cc')
lbtTitle.place(x=55, y=25)

#Добавление кнопки и метки для графика 1

btnChart = tk.Button(window, text = "График 1", font = ('Helvetica',10, 'bold'))
btnChart.place(x=40, y=115, width=90, height=30)

lbtChart = tk.Label(text = "График синуса matplotlib")
lbtChart.place(x=170, y=122)


#Добавление кнопки закрытия программы
btnClose = tk.Button(window, text = "Закрыть", font = ('Helvetica',10, 'bold'), command=do_close)
btnClose.place(x=330, y=400, width=90, height=30)



#Запуск цикла mainloop
window.mainloop()
