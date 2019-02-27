from datastructures import BoolArray


class Register(BoolArray):
    def __init__(self, name, bits=None, size=32):
        super(Register, self).__init__(bits, size)
        self.name = name

    def __repr__(self):
        return f"{self.name} => {super().__repr__()}"

