import pytest

from components import Register
from datastructures import MAX_BITS_SIZE


def test_init_name_attribute_from_passed_value():
    r = Register("R1")
    assert(r.name == "R1")


def test_init_size_property_from_passed_value():
    r = Register("R1", size=7)
    assert(r.size == 7)


def test_init_default_32_bits_long():
    r = Register("R1")
    assert(r.size == 32)


def test_init_set_bits():
    r = Register("R1", bits=[True, False, False])
    assert(r.bits == [True, False, False])


def test_init_should_raise_error_if_size_less_than_1():
    pytest.raises(AssertionError, lambda: Register("R1", size=0))


def test_init_should_raise_error_if_size_greater_than_max_size():
    pytest.raises(AssertionError, lambda: Register("R1", size=MAX_BITS_SIZE + 1))


def test_bitwise_and_should_work():
    r1 = Register("R1", bits=[True, False, True, False])
    r2 = Register("R2", bits=[True, True, False, False])
    r3 = r1 & r2
    assert(r3.bits == [True, False, False, False])


def test_bitwise_xor_should_work():
    r1 = Register("R1", bits=[True, False, True, False])
    r2 = Register("R2", bits=[True, True, False, False])
    r3 = r1 ^ r2
    assert(r3.bits == [False, True, True, False])

def test_repr_correct_format():
    r1 = Register("R1", bits=[True, False, False, True])
    assert(str(r1) == "R1 => 1,0,0,1")
