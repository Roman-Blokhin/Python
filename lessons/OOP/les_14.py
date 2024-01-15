# ООП 14 Пространство имен класса Class Body scope in Python

class DepartmentIt:
    PYTHON = 3
    HTML = 2
    JAVA = 7

    def info(self):  # 1. мы можем обратиться к переменным через 'self.' - экземпляр класса
        print(self.PYTHON, self.JAVA, self.HTML)

    def info_2(self):  # 2. мы можем обратиться к переменным через класс
        print(DepartmentIt.PYTHON, DepartmentIt.JAVA, DepartmentIt.HTML)

    @property
    def info_property(self):  # 3. мы можем обратиться к переменным через свойство property
        print(self.PYTHON, self.JAVA, self.HTML)

    @classmethod
    def info_classmethod(cls):  # 4. мы можем обратиться к переменным через свойство classmethod - через класс
        print(cls.PYTHON, cls.JAVA, cls.HTML)

    @staticmethod
    def info_staticmethod():  # 5. мы можем обратиться к переменным через свойство staticmethod - нет атрибутов
        print(DepartmentIt.PYTHON, DepartmentIt.JAVA, DepartmentIt.HTML)

    # 6. смоделируем ситуацию, когда нам нужно нанять разработчика
    # так как мы обращаемся к переменной - DepartmentIt, то не создается локальное значение PYTHON, а меняется в классе
    # при создании нового экземпляра у переменной будет уже измененное значение, а не начальное
    def person(self):
        DepartmentIt.PYTHON += 1
        print('Python:', DepartmentIt.PYTHON)


it_1 = DepartmentIt()

it_1.info()  # 1
it_1.info_2()  # 2
it_1.info_classmethod()  # 4
it_1.info_staticmethod()  # 5

# 6. смотрим, как меняются переменные в самом классе
it_2 = DepartmentIt()
it_2.info()
it_2.person()
it_2.info()

it_1.info_property()  # 3
