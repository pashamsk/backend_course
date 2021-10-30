class CustomMeta(type):

    def __new__(mcs, user_class_name,
                user_class_parents, user_class_attr):
        new_attr = {}
        for name, val in user_class_attr.items():
            if not name.startswith('__'):
                new_attr['custom_' + name] = val
            else:
                new_attr[name] = val

        return type.__new__(mcs, user_class_name,
                            user_class_parents, new_attr)


class CustomClass(metaclass=CustomMeta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100

print(hasattr(CustomClass, 'custom_x'))
