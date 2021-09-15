def test_celsius_from_farenheit():
    from temp_conversion import celsius_from_farhenheit
    result = celsius_from_farhenheit(20)
    expected = 68
    assert result == expected
