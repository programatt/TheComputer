import pytest

from datastructures import BoolArray, MAX_BITS_SIZE


def test_should_allow_size_1_to_size_32_bits():
    # noinspection PyBroadException
    try:
        for i in range(1, 33):
            BoolArray(size=i)
    except AssertionError:
        pytest.fail("Creating BoolArray size {} raised AssertionError".format(i))


def test_should_throw_exception_size_less_than_1():
    pytest.raises(AssertionError, lambda: BoolArray(size=0))


def test_should_throw_exception_size_greater_than_MAX_BITS_SIZE():
    pytest.raises(AssertionError, lambda: BoolArray(size=MAX_BITS_SIZE + 1))


def test_should_throw_exception_if_bits_not_list_of_booleans():
    pytest.raises(AssertionError, lambda: BoolArray(bits=["not", "booleans"]))


def test_should_throw_exception_if_bits_length_less_that_1():
    pytest.raises(AssertionError, lambda: BoolArray(bits=[]))


def test_bits_from_integer():
    a = BoolArray(size=MAX_BITS_SIZE)
    a.bits[-2] = True
    b = BoolArray(integer=2)
    assert(a == b)


def test_invert_bits():
    a = BoolArray(bits=[True, False, True, False])
    a = ~a
    assert(a == [False, True, False, True])


def test_eq_compares_bits():
    a = BoolArray(bits=[True, False])
    b = BoolArray(bits=[True, False])
    c = BoolArray(bits=[False, True])
    assert(a == b)
    assert(b != c)
    assert(a != c)


def test_eq_undefined():
    a = BoolArray(bits=[True, False])
    pytest.raises(ValueError, lambda: a == "[True, False]")


def test_eq_integer():
    a = BoolArray(bits=[True, False])
    assert(a == 2)


def test_repr_shows_bits_right_to_left():
    b = BoolArray(bits=[True, False, True, False])
    assert(str(b) == "1,0,1,0")


def test_bitwise_and_works():
    a = BoolArray(bits=[True, False, True, False])
    b = BoolArray(bits=[True, False, False, True])
    c = a & b
    d = b & a
    assert(c.bits == [True, False, False, False])
    assert(d.bits == [True, False, False, False])


def test_bitwise_and_works_with_boolean_list():
    a = BoolArray(bits=[True, False, True, False])
    b = [True, False, False, True]
    c = a & b
    assert(c.bits == [True, False, False, False])


def test_bitwise_and_pads_high_order_bits_if_one_boolarray_larger_than_other():
    a = BoolArray(bits=[True, False, True, False, True])
    #                   False,
    b = BoolArray(bits=       [True, False, False, True])
    c = a & b
    assert(c.bits == [False, False, False, False, True])


def test_bitwise_xor_works():
    a = BoolArray(bits=[True, False, True, False])
    b = BoolArray(bits=[True, False, False, True])
    c = a ^ b
    d = b ^ a
    assert (c.bits == [False, False, True, True])
    assert (d.bits == [False, False, True, True])


def test_bitwise_xor_pads_high_order_bits_if_one_boolarray_larger_than_other():
    a = BoolArray(bits=[True, False, True, False, True])
    #                  False,
    b = BoolArray(bits=      [True, False, False, True])
    c = a ^ b
    assert(c.bits == [True, True, True, False, False])


def test_convert_to_integer_properly():
    a = BoolArray(bits=[True, False, False, False])
    assert(a == 8)