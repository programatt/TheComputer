from datastructures import BoolArray


class Register(BoolArray):
    def __init__(self, name, integer=None, bits=None, size=32):
        super(Register, self).__init__(integer, bits, size)
        self.name = name

    def __repr__(self):
        return "{} => {}".format(
            self.name,
            super().__repr__()
        )

