from datastructures import BoolArray, MAX_BITS_SIZE

class Register(object):
    def __init__(self, name, bits=None, size=32):
        assert(1 <= size <= MAX_BITS_SIZE)
        self.name = name
        self.value = BoolArray(bits=bits, size=size)

    @property
    def size(self):
        return self.value.size

    @property
    def bits(self):
        return self.value.bits

    def __and__(self, other):
        return self.value & other.value

    def __xor__(self, other):
        return self.value ^ other.value