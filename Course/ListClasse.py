class MyList(list):

    def __init__(self, lst=[]):
        super(MyList, self).__init__(lst)

    def __add__(self, other):
        return MyList.construct(self, other, flag=1)

    def __radd__(self, other):
        return MyList.construct(other, self, flag=1)

    def __sub__(self, other):
        return MyList.construct(self, other, flag=0)

    def __rsub__(self, other):
        return MyList.construct(other, self, flag=0)

    def __eq__(self, other):
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
        sub_list = MyList()
        for _ in range(len(self)):
            if flag == 0:
                res = self[_] - other[_]
            else:
                res = self[_] + other[_]
            sub_list.append(res)
        return sub_list
