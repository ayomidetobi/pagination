from main import generate_pagination


def test_pagination_basic() -> None:
    assert generate_pagination(4, 10, 2, 2) == "1 2 3 4 5 6 ... 9 10"
    assert generate_pagination(1, 10, 2, 2) == "1 2 3 ... 9 10"
    assert generate_pagination(5, 15, 1, 1) == "1 ... 4 5 6 ... 15"
    assert generate_pagination(10, 20, 3, 1) == "1 2 3 ... 9 10 11 ... 18 19 20"
    assert generate_pagination(4, 5, 1, 0) == "1 ... 4 5"


def test_invalid_total_and_current_pages() -> None:
    assert (
        generate_pagination(1, 0, 2, 2)
        == "current page & total pages must be greater than 0"
    )
    assert (
        generate_pagination(0, 10, 2, 2)
        == "1 2 ... 9 10"
    )
    
    assert (
        generate_pagination(0, 0, 0, 0)
        == "current page & total pages must be greater than 0"
    )


def test_first_last_page() -> None:
    assert generate_pagination(1, 1, 2, 2) == "1"
    assert generate_pagination(1, 5, 1, 0) == "1 ... 5"
    assert generate_pagination(5, 5, 1, 0) == "1 ... 5"
    assert generate_pagination(1, 100, 5, 5) == "1 2 3 4 5 6 ... 96 97 98 99 100"
    assert generate_pagination(100, 100, 5, 5) == "1 2 3 4 5 ... 95 96 97 98 99 100"
    assert generate_pagination(1, 10, 1, 1) == "1 2 ... 10"
    assert generate_pagination(10, 10, 1, 1) == "1 ... 9 10"


def test_around_are_zero() -> None:
    assert generate_pagination(1, 5, 0, 0) == "1 ..."
    assert generate_pagination(3, 5, 1, 0) == "1 ... 3 ... 5"
    assert generate_pagination(5, 5, 1, 0) == "1 ... 5"


def test_boundaries_cover_all_pages() -> None:
    assert generate_pagination(1, 5, 10, 10) == "1 2 3 4 5"
    assert generate_pagination(2, 5, 5, 1) == "1 2 3 4 5"
    assert generate_pagination(3, 4, 5, 1) == "1 2 3 4"
    assert generate_pagination(5, 5, 5, 5) == "1 2 3 4 5"


def test_large_values() -> None:
    assert (
        generate_pagination(1000000000, 10, 2, 1)
        == "1 2 ... 9 10"
    )
    assert (
        generate_pagination(3, 1000000000, 2, 1)
        == "1 2 3 4 ... 999999999 1000000000"
    )
    assert (
        generate_pagination(3, 10, 1000000000, 1)
        == "1 2 3 4 5 6 7 8 9 10"
    )
    assert (
        generate_pagination(3, 10, 2, 1000000000)
        == "1 2 3 4 5 6 7 8 9 10"
    )



def test_string_input() -> None:
    assert generate_pagination("1", 10, 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, "10", 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, "2", 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, 2, "2") == "All values must be instances of int"


def test_boolean_input() -> None:
    assert generate_pagination(True, 10, 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, True, 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, False, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, 2, True) == "All values must be instances of int"


def test_float_input() -> None:
    assert generate_pagination(4.5, 10, 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10.5, 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, 2.5, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, 2, 2.5) == "All values must be instances of int"


def test_none_input() -> None:
    assert generate_pagination(None, 10, 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, None, 2, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, None, 2) == "All values must be instances of int"
    assert generate_pagination(4, 10, 2, None) == "All values must be instances of int"


def test_negative_input() -> None:
    assert (
        generate_pagination(-1, 10, 2, 2)
        == "current page & total pages must be greater than 0"
    )
    assert (
        generate_pagination(4, -1, 2, 2)
        == "current page & total pages must be greater than 0"
    )
    assert (
        generate_pagination(4, 10, -1, 2)
        == "amount & boundaries must be positive int"
    )
    assert (
        generate_pagination(4, 10, 2, -1)
        == "amount & boundaries must be positive int"
    )



def test_boundaries_are_zero() -> None:
    assert generate_pagination(5, 5, 0, 5) == "1 2 3 4 5"
    assert generate_pagination(1, 3, 0, 3) == "1 2 3"
    assert generate_pagination(5, 10, 0, 0) == "... 5 ..."
    assert generate_pagination(1, 10, 0, 0) == "1 ..."
    assert generate_pagination(1, 10, 0, 2) == "1 2 3 ..."
    assert generate_pagination(10, 10, 0, 0) == "... 10"
    assert generate_pagination(9, 10, 0, 2) == "... 7 8 9 10"
