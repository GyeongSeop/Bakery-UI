import tkinter
from tkinter import *


class BakeryView:
    def __init__(self, window):
        self.__init_window(window)

    def __init_window(self, window):
        window.title("빵집")
        window.geometry('400x200')
        label = Label(window, text='주문내역')
        label.pack()
        self.orderText = Text(window)
        self.orderText.pack()

    def add_order(self, orders):
        self.orderText.insert(0.0, orders + "\n")


class CustomerView:
    def __init__(self, name, window, bakery_view):
        self.name = name
        self.__init_window(window)
        self.bakeryView = bakery_view

    def __init_window(self, window):
        window.title("고객: " + self.name)
        window.geometry('350x200')
        label_s = Label(window, text = "샌드위치 (5000원)")
        label_s.grid(column = 0, row = 0)
        label_c = Label(window, text= "케이크 (20000원)")
        label_c.grid(column = 0, row = 1)
        self.num_s = Entry(window, width = 10)
        self.num_c = Entry(window, width = 10)
        self.num_s.grid(column = 1, row = 0)
        self.num_c.grid(column=1, row=1)
        button = Button(window, text= "주문하기",  command = self.send_order)
        button.grid(column = 0, row = 2)

    def send_order(self): #수정
        try:
            S = int(self.num_s.get())
            C = int(self.num_c.get())
            if S>0 and C>0:
                order_text = str(self.name)+": 샌드위치 (5000원) "+ str(S) +"개, 케이크 (20000원) "+ str(C) +"개"
                self.bakeryView.add_order(order_text)
            elif S>0 and C<=0:
                order_text = str(self.name) + ": 샌드위치 (5000원) " + str(S) + "개"
                self.bakeryView.add_order(order_text)
            elif S<=0 and C>0:
                order_text = str(self.name) + ": 케이크 (20000원) " + str(C) + "개"
                self.bakeryView.add_order(order_text)
            else:
                ValueError
        except ValueError:
            try:
                S = int(self.num_s.get())
                if S>0:
                    order_text = str(self.name)+": 샌드위치 (5000원) "+ str(S) +"개"
                    self.bakeryView.add_order(order_text)
                else:
                    ValueError
            except ValueError:
                try:
                    C = int(self.num_c.get())
                    if C>0:
                        order_text = str(self.name) + ": 케이크 (20000원) " + str(C) + "개"
                        self.bakeryView.add_order(order_text)
                    else:
                        ValueError
                except ValueError:
                    pass

if __name__ == '__main__':
    app = Tk()
    bakery = BakeryView(app)
    CustomerView('고객A', Toplevel(app), bakery)
    CustomerView('고객B', Toplevel(app), bakery)
    app.mainloop()
