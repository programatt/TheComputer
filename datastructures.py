def is_boolean_list(lst):
    return type(lst) == list and all([type(i) == bool for i in lst])

def assert_boolean_list(lst):
    assert(1 <= len(lst) <= MAX_BITS_SIZE)
    assert(is_boolean_list(lst))

MAX_BITS_SIZE=32

class BoolArray(object):
    def __init__(self, bits=None, size=MAX_BITS_SIZE):
        assert (1 <= size <= MAX_BITS_SIZE)
        # because empty lists are not Truthy :(
        # noinspection PySimplifyBooleanCheck
        if bits:
            assert_boolean_list(bits)
            self.bits = bits
            self.size = len(bits)
        elif bits == []:
            raise AssertionError("bits must not be empty list")
        else:
            self.bits = [False for _ in range(0, size)]
            self.size = len(self.bits)

    def __repr__(self):
        """Display Bits Right To Left (High Order To Low Order)"""
        return ",".join(self.__tobits())

    def __int__(self):
        """Convert to integer by interpreting bits as base 2 number high order to low order"""
        return int("".join(self.__tobits()), 2)

    def __tobits(self):
        """Convert bits from list of booleans to list of string 1's and 0's"""
        return ["1" if b else "0" for b in self.bits]

    def __and__(self, other):
        """
        Calculate Bitwise AND (&) Operation on Two BoolArrays
        Or A BoolArray and A List of booleans
        """
        return self.__execute_bitwise_operator(self, other, lambda a, b: a & b)

    def __xor__(self, other):
        """
        Calculate Bitwise Exclusive OR (^) Operation on Two BoolArrays
        Or A BoolArray and A List of booleans
        """
        return self.__execute_bitwise_operator(self, other, lambda a, b: a ^ b)

    @staticmethod
    def __execute_bitwise_operator(a, b, op):
        ibl = is_boolean_list(b)
        assert(type(b) == BoolArray or ibl)

        if(ibl):
            size_diff = a.size - len(b)
            b = b.copy()
        else:
            size_diff = a.size - b.size
            b = b.bits.copy()
        a = a.bits.copy()
        padding = [False for _ in range(0, size_diff)]
        if size_diff > 0:
            b = padding + b
        else:
            a = padding + a
        return BoolArray(bits=[op(z[0], z[1]) for z in zip(a,b)])

