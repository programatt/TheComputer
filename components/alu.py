from datastructures import BoolArray


class SimpleALU(object):
    ADD_OPERATION = [False, False, False]
    AND_OPERATION = [False, False, True]
    OR_OPERATION = [False, True, False]
    A_OPERATION = [False, True, True]
    NOTB_OPERATION = [True, False, False]

    @staticmethod
    def single_bit_alu(a, b, carryin):
        """
        Calculate SUM, CARRYOUT, NEGATE B,
        LOGICAL AND, LOGICAL OR on
        inputs a, b, carryin
        """
        aXORb = a ^ b
        aANDb = a & b
        s = aXORb ^ carryin
        carryout = aANDb | (carryin & aXORb)
        return carryout, s, aANDb, a | b, a, not b

    @staticmethod
    def multiplex_output(control_word, s, andb, aorb, a, notb):
        """Multiplex 5 output bits with 3 control bits"""
        (cw0, cw1, cw2) = tuple(control_word)
        return (not cw0 and not cw1 and not cw2 and s) or \
               (not cw0 and not cw1 and cw2 and andb) or \
               (not cw0 and cw1 and not cw2 and aorb) or \
               (not cw0 and cw1 and cw2 and a) or \
               (cw0 and not cw1 and not cw2 and notb)

    @staticmethod
    def multi_bit_alu(a, b, cw):
        """
        Run Single Stage ALU for each bit in registers
        a, b and return output using control word cw
        :param a: Register A
        :param b: Register B
        :param cw: Operation Output
        :return: BoolArray
        """
        assert(
            issubclass(type(a), BoolArray) and
            issubclass(type(b), BoolArray)
        )
        assert(a.size == b.size)
        cin = False
        output = []
        for ba, bb in zip(a.lowhighbits, b.lowhighbits):
            cout, s, aab, aob, a, notb = SimpleALU.single_bit_alu(
                ba, bb, cin
            )
            out = SimpleALU.multiplex_output(
                cw.bits, s, aab, aob, a, notb
            )
            output.append(out)
            cin = cout

        # F(A, B, C) = (D, E)
        # ([A], [B], 0) => F => [E]

        # We added the bits low to high, but it's stored high to low
        output.reverse()

        return BoolArray(bits=output)


