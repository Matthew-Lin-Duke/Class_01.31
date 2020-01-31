def test_cal_y():
    from y_coordinate import cal_y
    p1 = (9, 10)
    p2 = (4, 6)
    x3 = 30
    answer = cal_y(p1, p2, x3)
    expected = 26.8
    assert answer == expected


def test_on_line_true():
    from y_coordinate import on_line
    p1 = (9, 10)
    p2 = (4, 6)
    p3 = (2, 4)
    p4 = (30, 26.8)
    answer = on_line(p1, p2, p4)
    expected = True
    assert answer == expected


def test_on_line_false():
    from y_coordinate import on_line
    p1 = (9, 10)
    p2 = (4, 6)
    p3 = (2, 4)
    p4 = (30, 26.8)
    answer = on_line(p1, p2, p3)
    expected = False
    assert answer == expected
