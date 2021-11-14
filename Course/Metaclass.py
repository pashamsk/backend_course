class CustomMeta(type):

    def __call__(cls, *args, **kwargs):
        new_instance = super().__call__(*args, **kwargs)
        new_instance.__dict__ = CustomMeta.new_attribute(new_instance.__dict__)
        return new_instance

    def __new__(mcs, user_class_name,
                user_class_parents, user_class_attr):
        new_attr = CustomMeta.new_attribute(user_class_attr)
        return super(CustomMeta, mcs).__new__(mcs, user_class_name,
                                              user_class_parents, new_attr)

    @staticmethod
    def new_attribute(param):
        new_attr = {}
        for name, val in param.items():
            if not (name.startswith('__') and name.endswith('__')):
                new_attr['custom_' + name] = val
            else:
                new_attr[name] = val
        return new_attr


class CustomClass(metaclass=CustomMeta):
    x = 50
    __y = 70

    def __init__(self, val=99):
        self.val = val

    @staticmethod
    def line():
        return 100
