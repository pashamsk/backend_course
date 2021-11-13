class MyList(list):

    def __init__(self, lst=[]):
        super(MyList, self).__init__(lst)
        self.my_list = lst

    def __add__(self, other):
        return MyList.construct(self, other, flag=1)

    def __sub__(self, other):
        return MyList.construct(self, other, flag=0)

    def __eq__(self, other):
        if len(self.my_list) == len(other):
            for _ in range(len(self.my_list)):
                if self.my_list[_] != other[_]:
                    return False
        return True

    def construct(self, other, flag):
        dif = len(self.my_list) - len(other)
        if dif == 0:
            return MyList.my_meth(self.my_list, other, flag)
        elif dif > 0:
            tmp = other
            tmp.extend([0] * dif)
            return MyList.my_meth(self.my_list, tmp, flag)
        else:
            tmp = self.my_list
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

v = [2, 4, 7]
a = MyList([1, 3, 4, 5, 7])
b = MyList([5, 6, 8])
d = MyList([5, 6, 8])
c = a + v
e = a + b
print(c, e)
print(b - a)
print(isinstance(c, MyList))
print(b == d)
# print(b == c)