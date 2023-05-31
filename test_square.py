from square import square_num


def test_square_num():
    a = 4
    result = square_num(a)
    ##assert the observed value(result) with the expected value
    assert result == 16