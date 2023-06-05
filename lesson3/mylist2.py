"""
Напишите класс MyList2, который будет работать аналогично встроенному классу list(). Класс должен иметь следующие
методы:

- __init__(self, data): конструктор, принимающий список элементов;
- __iter__(self): магический метод, который возвращает итератор;
- __next__(self): магический метод, который возвращает следующий элемент последовательности;
- __getitem__(self, index): магический метод, который позволяет обратиться к элементу списка по индексу.
"""


class MyList2:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.data):
            current_element = self.data[self.index]
            self.index += 1
            return current_element
        else:
            raise StopIteration()

    def __getitem__(self, item):
        return self.data[item]


my_list = MyList2([1, 2, 3])
for i in my_list:
    print(i)  # 1 2 3

print(my_list[1])  # 2
