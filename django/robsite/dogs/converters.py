class FourDigitYearConverter:  # конвертер для преобразования регулярного выражения в простой путь
    regex = "[0-9]{4}"  # прописываем регулярное выражение

    def to_python(self, value):  # делает выражение целым числом
        return int(value)

    def to_url(self, value):  # преобразует данные в нужный для url формат
        return "%04d" % value