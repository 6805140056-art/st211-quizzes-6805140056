from solution import roman_to_number, validate_roman_rules


def test_roman_to_number():
    assert roman_to_number("III") == 3
    assert roman_to_number("VIII") == 8
    assert roman_to_number("IX") == 9


def test_invalid_repeated_symbols():
    valid, message = validate_roman_rules("VV")
    assert valid is False

    valid, message = validate_roman_rules("IIII")
    assert valid is False