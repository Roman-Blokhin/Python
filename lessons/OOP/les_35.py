# OOP 35 Распространение исключений || Propagation exceptions

def third():  # вызывается четвертым
    print('start third')
    try:  # делаем исключение, чтобы не возникла ошибка
        1/0
    except ZeroDivisionError:
        print('handling')
    print('finish third')

def second():
    print('start second')
    third()  # вызывается третьим
    print('finish second')

def first():
    print('start first')
    second()  # вызывается вторым
    print('finish first')


print('hello Roman')
first()  # вызывается первым

# если у нас есть каскад исключений, то он читается снизу вверх, чтобы добраться до места создания исключения/ошибки