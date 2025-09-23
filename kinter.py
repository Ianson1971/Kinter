from tkinter import *

window = Tk() #Создаем окно
window.title("Многострочный текст")
#Создаем заголовок окна
#Функция для вставки текста
def insertTextL():
    text.delete(1.0, END)
    s = "Мотор лево\n"
    text.insert(1.0, s)
def insertTextR():
    text.delete(1.0, END)
    s = "Мотор право\n"
    text.insert(1.0, s)
def insertText_STOP():
    text.delete(1.0, END)
    s = "Мотор стоп\n"
    text.insert(1.0, s)


#Функция для считывания текста
def getText():
    s = text.get(2.0, 2.7)
    label['text'] = s
#Функция для удаления текста
def deleteText():
    text.delete(1.0, END)

#Создаем многострочное текстовое поле
text = Text(width=40, height=10)
text.pack()
#Создаем фрейм
frame = Frame(window)
frame.pack()

#Создаем три кнопки
b_insert = Button(frame, text=" мотор << ",command=insertTextR)
b_insert.pack(side=LEFT)

b_get = Button(frame, text="мотор стоп", command=insertText_STOP)
b_get.pack(side=LEFT)

b_delete = Button(frame, text="мотор >>", command=insertTextL)
b_delete.pack(side=LEFT)

#Создаем метку для вывода текста
label = Label()
label.pack()
#Цикл обработки событий окна
window.mainloop()





