from benchmark.reference import (
    average,
    cart_total,
    count_words,
    is_positive_integer,
    unique_in_order,
)
import pytest

def test_average_normal_numbers():
    assert average([2, 4, 6]) == 4.0


def test_average_negative_numbers():
    assert average([-2, 0, 2]) == 0.0


def test_average_decimal_numbers():
    assert average([1.5, 2.5]) == 2.0


def test_average_empty_list():
    assert average([]) is None


def test_count_words_normal_text():
    assert count_words("Hello Python world") == 3


def test_count_words_extra_spaces():
    assert count_words("  Hello   Python  ") == 2


def test_count_words_empty_text():
    assert count_words("") == 0


def test_count_words_whitespace_only():
    assert count_words("   \t\n  ") == 0


def test_count_words_newlines():
    assert count_words("Hello\nPython\nworld") == 3


def test_positive_integer():
    assert is_positive_integer(5) is True


def test_positive_integer_one():
    assert is_positive_integer(1) is True


def test_zero_is_not_positive():
    assert is_positive_integer(0) is False


def test_negative_integer_is_not_positive():
    assert is_positive_integer(-3) is False


def test_float_is_not_integer():
    assert is_positive_integer(3.5) is False


def test_string_is_not_integer():
    assert is_positive_integer("5") is False


def test_boolean_is_not_integer():
    assert is_positive_integer(True) is False


def test_unique_in_order_numbers():
    assert unique_in_order([1, 2, 1, 3, 2]) == [1, 2, 3]


def test_unique_in_order_strings():
    assert unique_in_order(["a", "b", "a", "c"]) == ["a", "b", "c"]


def test_unique_in_order_all_duplicates():
    assert unique_in_order([5, 5, 5]) == [5]


def test_unique_in_order_empty_list():
    assert unique_in_order([]) == []


def test_cart_total_without_discount():
    assert cart_total([10, 20, 30]) == 60


def test_cart_total_with_discount():
    assert cart_total([10, 20, 30], 10) == 54


def test_cart_total_empty_cart():
    assert cart_total([]) == 0


def test_cart_total_full_discount():
    assert cart_total([50], 100) == 0


def test_cart_total_negative_price():
    with pytest.raises(ValueError):
        cart_total([10, -5, 20])


def test_cart_total_discount_above_100():
    with pytest.raises(ValueError):
        cart_total([50], 110)


def test_cart_total_negative_discount():
    with pytest.raises(ValueError):
        cart_total([50], -10)
