from src.day_05.main2 import compact_ranges, ranges_overlap


def test_ranges_overlap_not_overlapping():
    assert ranges_overlap([1, 2], [3, 4]) is False


def test_ranges_overlap_are_overlapping():
    assert ranges_overlap([1, 2], [2, 3]) is True


def test_compact_ranges_lo_hi():
    id_ranges = [[1, 2], [2, 3]]
    assert compact_ranges(id_ranges, [1, 2], [2, 3]) == [[1, 3]]


def test_compact_ranges_hi_lo():
    id_ranges = [[1, 2], [2, 3]]
    assert compact_ranges(id_ranges, [2, 3], [1, 2]) == [[1, 3]]


def test_compact_ranges_fully_contained():
    id_ranges = [[1, 5], [2, 3]]
    assert compact_ranges(id_ranges, [1, 5], [2, 3]) == [[1, 5]]
