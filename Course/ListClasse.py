class MyList(list):
    """
    Класс, отнаследованный от списка. Переопределены методы сложения, вычитания и сравнения списков.
    Аргументы всех методов, определенных в классе, кроме метода __init__
    :param self: инстанс класса MyList, в котором хранится список, переданный при создании инстанса
    :param other: дефолтный список либо инстанс класса MyList, в котором хранится список, с которым необходимо
    провести операцию сложения/вычитания
    """
    def __init__(self, lst=[]):
        """
        Инициализация списка через конструктор __init__ класса list
        :param lst: список, передающийся при создании инстанса класса. Будет пустым, если списко передан не будет.
        """
        super(MyList, self).__init__(lst)

    def __add__(self, other):
        """
        Переопределение операции сложения. Будет вызвана, если self является инстансом класса MyList.
        :param self: см. документацию самого класса
        :param other: см. документацию самого класса
        :return: инстанс класса MyList, являющийся результатом поэлементного сложения списков
        """
        return MyList.construct(self, other, flag=1)

    def __radd__(self, other):
        """
        Переопределение операции сложения. Будет вызвана, если self не является инстансом класса MyList.
        :param self: см. документацию самого класса
        :param other: см. документацию самого класса
        :return: инстанс класса MyList, являющийся результатом поэлементного сложения списков
        """
        return MyList.construct(other, self, flag=1)

    def __sub__(self, other):
        """
        Переопределение операции вычитания. Будет вызвана, если self является инстансом класса MyList.
        :param self: см. документацию самого класса
        :param other: см. документацию самого класса
        :return: инстанс класса MyList, являющийся результатом поэлементного вычитания списков
        """
        return MyList.construct(self, other, flag=0)

    def __rsub__(self, other):
        """
        Переопределение операции вычитания. Будет вызвана, если self не является инстансом класса MyList.
        :param self: см. документацию самого класса
        :param other: см. документацию самого класса
        :return: инстанс класса MyList, являющийся результатом поэлементного вычитания списков
        """
        return MyList.construct(other, self, flag=0)

    def __eq__(self, other):
        """
        Функция сравнения списков по сумме их элементов.
        :param self: см. документацию самого класса
        :param other: см. документацию самого класса
        :return: True, если сумма элементов двух списков одинакова и False - если нет
        """
        sum_1 = 0
        sum_2 = 0
        for _ in range(len(self)):
            sum_1 += self[_]
        for _ in range(len(other)):
            sum_2 += other[_]
        if sum_1 == sum_2:
            return True
        return False

    def construct(self, other, flag):
        """
        Сам список, возвращаемый в return, возвращает функция my_meth, в которую в зависимости от разности длины списков
        будут переданы либо исходные списки, либо бОльший из исходных списков и поверхностная копия меньшего списка,
        дополненная нулями. Сами списки не изменяются согласно ТЗ.
        :param self: см. документацию самого класса
        :param other: см. документацию самого класса
        :param flag: =0, если вызван из __(r)sub__ и =1, если вызван из __(r)add__
        :return:Новый список, в котором в зависимости от параметра flag находится результат поэлементного
        сложения/вычитания списков, переданных в self и other и являющийся инстансом класса MyList.
        """
        dif = len(self) - len(other)
        if dif == 0:
            return MyList.my_meth(self, other, flag)
        elif dif > 0:
            tmp = other.copy()
            tmp.extend([0] * dif)
            return MyList.my_meth(self, tmp, flag)
        else:
            tmp = self.copy()
            tmp.extend([0] * abs(dif))
            return MyList.my_meth(tmp, other, flag)

    def my_meth(self, other, flag):
        """
        :param self: см. документацию самого класса
        :param other: см. документацию самого класса
        :param flag: =0, если вызван из __(r)sub__ и =1, если вызван из __(r)add__
        :return: Новый список, в котором в зависимости от параметра flag находится результат поэлементного
        сложения/вычитания списков, переданных в self и other и являющийся инстансом класса MyList.
        """
        sub_list = MyList()
        for _ in range(len(self)):
            if flag == 0:
                res = self[_] - other[_]
            else:
                res = self[_] + other[_]
            sub_list.append(res)
        return sub_list
