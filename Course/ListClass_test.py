from unittest import TestCase, main
from ListClasse import MyList


class TestListClass(TestCase):

    a = MyList([5, 1, 3, 7])
    b = MyList([1, 2, 7])
    c = MyList([3, 4])
    d = [1, 2]
    sum_1 = a + b
    sum_2 = d + c
    sub_1 = a - b
    sub_2 = d - c

    def test_add(self):
        self.assertEqual(self.sum_1, [6, 3, 10, 7])
        self.assertTrue(isinstance(self.sum_1, MyList))
        self.assertEqual(self.b, [1, 2, 7])
        self.assertEqual(self.sum_2, [4, 6])
        self.assertTrue(isinstance(self.sum_2, MyList))

    def test_sub(self):
        self.assertEqual(self.sub_1, [4, -1, -4, 7])
        self.assertTrue(isinstance(self.sum_1, MyList))
        self.assertEqual(self.b, [1, 2, 7])
        self.assertEqual(self.sub_2, [-2, -2])
        self.assertTrue(isinstance(self.sum_2, MyList))

    def test_eq(self):
        self.assertTrue(self.a == [8, 8])
        self.assertFalse(self.a == self.d)


if __name__ == '__main__':
    main()
