import pytest


@pytest.mark.parametrize("tup1, tup2, x, expected_y", [
    ((2, 1), (5, 4), 6, 5),
    ((8,8), (6, 11), 13, 0.5),
    ((2, 3), (8, 4), 8, 4)])
    

def test_coord(tup1, tup2, x, expected_y):
    from coord_function import coord
    answer = coord(tup1, tup2, x)
    expected = expected_y
    assert answer == expected
