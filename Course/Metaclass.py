class CustomMeta(type):

    def __call__(cls, *args, **kwargs):
        new_instance = super().__call__(*args, **kwargs)
        new_attr = {}
        for name, val in new_instance.__dict__.items():
            if not (name.startswith('__') and name.endswith('__')):
                new_attr['custom_' + name] = val
        else:
            new_attr[name] = val
        new_instance.__dict__ = new_attr
        return new_instance

    def __new__(mcs, user_class_name,
                user_class_parents, user_class_attr):
        new_attr = {}
        for name, val in user_class_attr.items():
            if not (name.startswith('__') and name.endswith('__')):
                new_attr['custom_' + name] = val
            else:
                new_attr[name] = val
        return type.__new__(mcs, user_class_name,
                            user_class_parents, new_attr)

    def new_attribute(cls, param):
        new_attr = {}
        for name, val in param.items():
            if not (name.startswith('__') and name.endswith('__')):
                new_attr['custom_' + name] = val
            else:
                new_attr[name] = val
        return


class CustomClass(metaclass=CustomMeta):
    x = 50

    # __c = 70

    def __init__(self, val=99):
        self.val = val

    @staticmethod
    def line():
        return 100


a = CustomClass()
print(hasattr(a, 'custom_x'))
print(hasattr(a, 'x'))
