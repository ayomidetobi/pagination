from main import generate_pagination

def test_pagination_basic()->None:
    assert generate_pagination(4, 10, 2, 2) == "1 2 3 4 5 6 ... 9 10"
    assert generate_pagination(1, 10, 2, 2) == "1 2 3 ... 9 10"
    assert generate_pagination(5, 15, 1, 1) == "1 ... 4 5 6 ... 15"
    assert generate_pagination(10, 20, 3, 1) == "1 2 3 ... 9 10 11 ... 18 19 20"
    assert generate_pagination(4, 5, 1, 0) == "1 ... 4 5"

def test_invalid_total_and_current_pages() -> None:
    assert generate_pagination(1, 0, 2, 2) == ""
    assert generate_pagination(0, 10, 2, 2) == ""
    assert generate_pagination(3, 2, 1, 1) == ""
    assert generate_pagination(-1, 10, 2, 2) == ""
    assert generate_pagination(6, 5, 2, 1) == ""


def test_first_last_page()->None:
    assert generate_pagination(1, 1, 2, 2) == "1"
    assert generate_pagination(1, 5, 1, 0) == "1 ... 5"
    assert generate_pagination(5, 5, 1, 0) == "1 ... 5"
    assert generate_pagination(1, 100, 5, 5) == "1 2 3 4 5 6 ... 96 97 98 99 100"
    assert generate_pagination(100, 100, 5, 5) == "1 2 3 4 5 ... 95 96 97 98 99 100"
    assert generate_pagination(1, 10, 1, 1) == "1 2 ... 10"
    assert generate_pagination(10, 10, 1, 1) == "1 ... 9 10"


def test_boundaries_or_around_are_zero() -> None:
    assert generate_pagination(1, 5, 0, 0) == ""
    assert generate_pagination(3, 5, 1, 0) == "1 ... 3 ... 5"
    assert generate_pagination(5, 5, 1, 0) == "1 ... 5"


def test_boundaries_cover_all_pages() -> None:
    assert generate_pagination(1, 5, 10, 10) == "1 2 3 4 5"
    assert generate_pagination(2, 5, 5, 1) == "1 2 3 4 5"
    assert generate_pagination(3, 4, 5, 1) == "1 2 3 4"
    assert generate_pagination(5, 5, 5, 5) == "1 2 3 4 5"


def test_large_pagination()->None:
    assert generate_pagination(50, 100, 10, 10) == "1 2 3 4 5 6 7 8 9 10 ... 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 ... 91 92 93 94 95 96 97 98 99 100"
    assert generate_pagination(1, 100, 5, 5) == "1 2 3 4 5 6 ... 96 97 98 99 100"


def test_small_pagination()->None:
    assert generate_pagination(3, 5, 1, 2) == "1 2 3 4 5"
