class MyList(list):

    def __init__(self, lst=[]):
        super(MyList, self).__init__(lst)
        self.my_list = lst

    def __add__(self, other):
        dif = len(self.my_list) - len(other)
        if dif == 0:
            return MyList.my_add(self.my_list, other)
        elif dif > 0:
            tmp = other
            tmp.extend([0] * dif)
            return MyList.my_add(self.my_list, tmp)
        else:
            tmp = self.my_list
            tmp.extend([0] * abs(dif))
            return MyList.my_add(tmp, other)

    def my_add(self, other):
        add_list = MyList()
        for _ in range(len(self)):
            res = self[_] + other[_]
            add_list.append(res)
        return add_list

    def __sub__(self, other):
        dif = len(self.my_list) - len(other)
        if dif == 0:
            return MyList.my_sub(self.my_list, other)
        elif dif > 0:
            tmp = other
            tmp.extend([0] * dif)
            return MyList.my_sub(self.my_list, tmp)
        else:
            tmp = self.my_list
            tmp.extend([0] * abs(dif))
            return MyList.my_sub(tmp, other)

    def my_sub(self, other):
        sub_list = MyList()
        for _ in range(len(self)):
            res = self[_] - other[_]
            sub_list.append(res)
        return sub_list

    def __eq__(self, other):
        if len(self.my_list) == len(other):
            for _ in range(len(self.my_list)):
                if self.my_list[_] != other[_]:
                    return False
        return True


v = [2, 4, 7]
a = MyList([1, 3, 4, 5, 7])
b = MyList([5, 6, 8])
d = MyList([5, 6, 8])
c = a + v
print(c)
print(b - a)
print(isinstance(c, MyList))
print(b == d)
# print(b == c)
