from src.day_09.main import area_of_rectangle

def test_area_of_rectangle_1x1_square():
    assert area_of_rectangle([0,0],[0,0]) == 1

def test_area_of_rectangle_2x2_square1():
    assert area_of_rectangle([0,0],[1,1]) == 4

def test_area_of_rectangle_2x2_square2():
    assert area_of_rectangle([1,1],[0,0]) == 4

def test_area_of_rectangle_2x2_square3():
    assert area_of_rectangle([0,1],[1,0]) == 4

def test_area_of_rectangle_2x2_square4():
    assert area_of_rectangle([1,0],[0,1]) == 4

def test_area_of_rectangle_2x4_rect():
    assert area_of_rectangle([0,0],[1,3]) == 8

def test_area_of_rectangle_4x2_rect():
    assert area_of_rectangle([0,0],[3,1]) == 8

def test_area_of_rectangle_ex1():
    assert area_of_rectangle([2,5],[9,7]) == 24

def test_area_of_rectangle_ex2():
    assert area_of_rectangle([7,1],[11,7]) == 35

def test_area_of_rectangle_ex3():
    assert area_of_rectangle([7,3],[2,3]) == 6

def test_area_of_rectangle_ex4():
    assert area_of_rectangle([2,5],[11,1]) == 50