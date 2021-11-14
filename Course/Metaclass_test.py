from unittest import TestCase, main
from Metaclass import CustomClass


class TestMetaclass(TestCase):

    def test_rename_except_init(self):
        self.assertTrue(hasattr(CustomClass, 'custom_line'))
        self.assertTrue(hasattr(CustomClass, 'custom__CustomClass__y'))
        self.assertTrue(hasattr(CustomClass, 'custom_x'))
        self.assertFalse(hasattr(CustomClass, 'line'))
        self.assertFalse(hasattr(CustomClass, '_CustomClass__y'))
        self.assertFalse(hasattr(CustomClass, 'x'))

    def test_rename_init(self):
        a = CustomClass()
        self.assertTrue(hasattr(a, 'custom_val'))
        self.assertFalse(hasattr(a, 'val'))


if __name__ == '__main__':
    main()
