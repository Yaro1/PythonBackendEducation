PREFIX = "custom_"


class Meta(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        # print('  Meta.__prepare__(mcs=%s, name=%r, bases=%s, **%s)' % (
        #     mcs, name, bases, kwargs
        # ))
        return {}

    def __new__(mcs, name, bases, attrs, **kwargs):
        # print('  Meta.__new__(mcs=%s, name=%r, bases=%s, attrs=[%s], **%s)' % (
        #                  mcs, name, bases, ', '.join(attrs), kwargs
        #       ))
        attrs = dict((PREFIX + name, value) if not name.startswith('__') else (name, value) for name, value in attrs.items())
        return super().__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs, **kwargs):
        # print('  Meta.__init__(cls=%s, name=%r, bases=%s, attrs=[%s], **%s)' % (
        #     cls, name, bases, ', '.join(attrs), kwargs
        # ))
        super().__init__(name, bases, attrs)

    def __call__(cls, *args, **kwargs):
        # print('  Meta.__call__(cls=%s, args=%s, kwargs=%s)' % (
        #     cls, args, kwargs
        # ))
        obj = super().__call__(*args, **kwargs)
        obj.__dict__ = {PREFIX + name: value for name, value in obj.__dict__.items()}
        return obj


class CustomClass(metaclass=Meta):
    x = 50

    def __init__(self, val=99):
        self.val = val

    def line(self):
        return 100


inst = CustomClass()
print(inst.custom_x)
print(inst.custom_val)
print(inst.custom_line())

# inst.x  # ошибка
# inst.val  # ошибка
# inst.line() # ошибка
