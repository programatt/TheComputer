from components import SimpleALU
from datastructures import BoolArray


def b2b(lst):
    """
    Convert more compact screen real estate
    truth table to one alu is expecting for io
    """
    return [[True if b == 1 else False for b in bits] for bits in lst]


def test_simplealu_single_bit_alu_truth_table():
    truth_table = b2b([
        #A, B, CI, CO, S, A&B, A|B, A, ~B
        [0, 0, 0,  0,  0,  0,   0,  0,  1],
        [0, 0, 1,  0,  1,  0,   0,  0,  1],
        [0, 1, 0,  0,  1,  0,   1,  0,  0],
        [0, 1, 1,  1,  0,  0,   1,  0,  0],
        [1, 0, 0,  0,  1,  0,   1,  1,  1],
        [1, 0, 1,  1,  0,  0,   1,  1,  1],
        [1, 1, 0,  1,  0,  1,   1,  1,  0],
        [1, 1, 1,  1,  1,  1,   1,  1,  0]
    ])
    for row in truth_table:
        (a, b, cin) = tuple(row[:3])
        assert(SimpleALU.single_bit_alu(a, b, cin) == tuple(row[3:]))


def test_simplealu_multiplex_3in_5out():
    """
    0000 = Sum
    0001 = A and B
    0010 = A or B
    0011 = A
    0100 = Not B
    :return:
    """
    truth_table = [
        #cw0, cw1, cw2, s, a&b, a|b, a, ~b, out  output column
        [0,   0,   0,  1,  0,   0,  0,  0,  1],  # s
        [0,   0,   0,  0,  0,   0,  0,  0,  0],  # s
        [0,   0,   1,  0,  1,   0,  0,  0,  1],  # a&b
        [0,   0,   1,  0,  0,   0,  0,  0,  0],  # a&b
        [0,   1,   0,  0,  0,   1,  0,  0,  1],  # a|b
        [0,   1,   0,  0,  0,   0,  0,  0,  0],  # a|b
        [0,   1,   1,  0,  0,   0,  1,  0,  1],  # a
        [0,   1,   1,  0,  0,   0,  0,  0,  0],  # a
        [1,   0,   0,  0,  0,   0,  0,  1,  1],  # ~b
        [1,   0,   0,  0,  0,   0,  0,  0,  0],  # ~b
    ]
    for row in truth_table:
        (s, andb, aorb, a, notb, out) = tuple(row[3:])
        assert(
            SimpleALU.multiplex_output(row[:3], s, andb, aorb, a, notb) == out)


def test_simplealu_multi_bit_alu_add():
    control_word = BoolArray(bits=SimpleALU.ADD_OPERATION)
    a = BoolArray(integer=40)  # 101000
    b = BoolArray(integer=2)   # 000010
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == 42)       # 101010


def test_simplealu_multi_bit_alu_aandb():
    control_word = BoolArray(bits=SimpleALU.AND_OPERATION)
    a    = BoolArray(bits=[True, False, True,  False])
    b    = BoolArray(bits=[True, False, False, True])
    andb = BoolArray(bits=[True, False, False, False])
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == andb)


def test_simplealu_multi_bit_alu_aorb():
    control_word = BoolArray(bits=SimpleALU.OR_OPERATION)
    a    = BoolArray(bits=[True, False, True,  False])
    b    = BoolArray(bits=[True, False, False, True])
    aorb = BoolArray(bits=[True, False, True,  True])
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == aorb)


def test_simplealu_multi_bit_alu_a():
    control_word = BoolArray(bits=SimpleALU.A_OPERATION)
    a = BoolArray(bits=[True, False, True,  False])
    b = BoolArray(bits=[True, False, False, True])
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == a)


def test_simplealu_multi_bit_alu_not_b():
    control_word = BoolArray(bits=SimpleALU.NOTB_OPERATION)
    a    = BoolArray(bits=[False, False, False, False])
    b    = BoolArray(bits=[True,  False, True,  False])
    notb = BoolArray(bits=[False, True,  False, True])
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == notb)
