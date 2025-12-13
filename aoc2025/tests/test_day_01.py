from src.day_01.day_01 import move_dial

def test_move_dial_right():
    assert move_dial(11, "R", 8) == (19, 0)

def test_move_dial_left():
    assert move_dial(19, "L", 19) == (0, 1)

def test_move_dial_left_past_zero():
    assert move_dial(0, "L", 1) == (99, 0)

def test_move_dial_right_past_99():
    assert move_dial(99, "R", 1) == (0, 1)

def test_move_dial_l69():
    assert move_dial(50, "L", 68) == (82, 1)

def test_move_dial_l30():
    assert move_dial(82, "L", 30) == (52, 0)

def test_move_dial_r48():
    assert move_dial(52, "R", 48) == (0, 1)

def test_move_dial_l5():
    assert move_dial(0, "L", 5) == (95, 0)

def test_move_dial_r60():
    assert move_dial(95, "R", 60) == (55, 1)