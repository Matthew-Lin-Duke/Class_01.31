def test_cal_y():
    from y_coordinate import cal_y
    p1 = (9, 10)
    p2 = (4, 6)
    x3 = 30
    answer = cal_y(p1, p2, x3)
    expected = 26.8
    assert answer == expected
