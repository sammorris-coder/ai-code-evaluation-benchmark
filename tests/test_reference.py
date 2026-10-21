from benchmark.reference import average, count_words


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
