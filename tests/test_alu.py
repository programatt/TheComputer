from components import SimpleALU
from datastructures import BoolArray

def test_simplealue_single_bit_alu_truth_table():
    truth_table = [
        # A,    B,     CARRYIN, CARRYOUT, SUM,   A&B,   A|B,   A,    NOT B
        [False, False, False,   False,    False, False, False, False, True],
        [False, False, True,    False,    True,  False, False, False, True],
        [False, True,  False,   False,    True,  False, True,  False, False],
        [False, True,  True,    True,     False, False, True,  False, False],
        [True,  False, False,   False,    True,  False, True,  True,  True],
        [True,  False, True,    True,     False,  False, True, True,  True],
        [True,  True,  False,   True,     False, True,  True,  True,  False],
        [True,  True,  True,    True,     True,  True,  True,  True,  False]
    ]
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
        # CW0,   CW1,   CW2,  SUM,   A&B,   A|B,   A,     NOT B, OUT
        [False, False, False, True,  False, False, False, False, True],   # SUM
        [False, False, False, False, False, False, False, False, False],  # SUM
        [False, False, True,  False, True,  False, False, False, True],   # A&B
        [False, False, True,  False, False, False, False, False, False],  # A&B
        [False, True,  False, False, False, True,  False, False, True],   # A|B
        [False, True,  False, False, False, False, False, False, False],  # A|B
        [False, True,  True,  False, False, False, True,  False, True],   # A
        [False, True,  True,  False, False, False, False, False, False],  # A
        [True, False,  False, False, False, False, False,  True,  True],  # NOT B
        [True, False,  False, False, False, False, False,  False, False],  # NOT B
    ]
    for row in truth_table:
        (s, andb, aorb, a, notb, out) = tuple(row[3:])
        assert(SimpleALU.multiplex_output(row[:3], s, andb, aorb, a, notb) == out)

def test_simplealu_multi_bit_alu_add():
    control_word = BoolArray(bits=SimpleALU.ADD_OPERATION)
    # TODO make this test less icky by allowing BoolArray(int)
    a = BoolArray(integer=40)
    b = BoolArray(integer=2)
    # Assert Result = b (implement eq method on BoolArray)
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == 42)

def test_simplealu_multi_bit_alu_aandb():
    control_word = BoolArray(bits=SimpleALU.AND_OPERATION)
    # TODO make this test less icky by allowing BoolArray(int)
    a = BoolArray(bits=[True, False, True, False])
    b = BoolArray(bits=[True, False, False, True])
    # Assert Result = b (implement eq method on BoolArray)
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == [True, False, False, False])

def test_simplealu_multi_bit_alu_aandb():
    control_word = BoolArray(bits=SimpleALU.OR_OPERATION)
    # TODO make this test less icky by allowing BoolArray(int)
    a = BoolArray(bits=[True, False, True, False])
    b = BoolArray(bits=[True, False, False, True])
    # Assert Result = b (implement eq method on BoolArray)
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == [True, False, True, True])

def test_simplealu_multi_bit_alu_a():
    control_word = BoolArray(bits=SimpleALU.A_OPERATION)
    # TODO make this test less icky by allowing BoolArray(int)
    a = BoolArray(bits=[True, False, True, False])
    b = BoolArray(bits=[True, False, False, True])
    # Assert Result = b (implement eq method on BoolArray)
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == a)

def test_simplealu_multi_bit_alu_not_b():
    control_word = BoolArray(bits=SimpleALU.NOTB_OPERATION)
    # TODO make this test less icky by allowing BoolArray(int)
    a = BoolArray(bits=[False, False, False, False])
    b = BoolArray(bits=[True, False, True, False])
    # Assert Result = b (implement eq method on BoolArray)
    output = SimpleALU.multi_bit_alu(a, b, control_word)
    assert(output == BoolArray(bits=[False, True, False, True]))
