import pytest
from main import generate_pagination



@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (4, 10, 2, 2, "1 2 3 4 5 6 ... 9 10"),
        (1, 10, 2, 2, "1 2 3 ... 9 10"),
        (5, 15, 1, 1, "1 ... 4 5 6 ... 15"),
        (10, 20, 3, 1, "1 2 3 ... 9 10 11 ... 18 19 20"),
        (4, 5, 1, 0, "1 ... 4 5"),
    ],
)
def test_pagination_basic(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected

@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (1, 1, 2, 2, "1"),
        (1, 5, 1, 0, "1 ... 5"),
        (5, 5, 1, 0, "1 ... 5"),
        (1, 100, 5, 5, "1 2 3 4 5 6 ... 96 97 98 99 100"),
        (100, 100, 5, 5, "1 2 3 4 5 ... 95 96 97 98 99 100"),
        (1, 10, 1, 1, "1 2 ... 10"),
        (10, 10, 1, 1, "1 ... 9 10"),
    ]
)
def test_first_last_page(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected

@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (1, 5, 10, 10, "1 2 3 4 5"),
        (2, 5, 5, 1, "1 2 3 4 5"),
        (3, 4, 5, 1, "1 2 3 4"),
        (5, 5, 5, 5, "1 2 3 4 5"),
        (10, 10, 6, 1, "1 2 3 4 5 6 7 8 9 10"),
        (1, 10, 6, 1, "1 2 3 4 5 6 7 8 9 10"),
        (5, 10, 6, 3, "1 2 3 4 5 6 7 8 9 10"),
    ]
)
def test_cover_all_pages(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected

@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (1, 0, 2, 2, "current page & total pages must be greater than 0"),
        (0, 10, 2, 2, "current page & total pages must be greater than 0"),
        (0, 0, 0, 0, "current page & total pages must be greater than 0"),
    ],
)
def test_invalid_total_and_current_pages(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (1, 5, 0, 0, "1 ..."),
        (3, 5, 1, 0, "1 ... 3 ... 5"),
        (5, 5, 1, 0, "1 ... 5"),
    ],
)
def test_around_are_zero(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected



@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (1000000000, 10, 2, 1, "Current page cannot exceed the total number of pages."),
        (3, 1000000000, 2, 1, "1 2 3 4 ... 999999999 1000000000"),
        (3, 10, 1000000000, 1, "1 2 3 4 5 6 7 8 9 10"),
        (3, 10, 2, 1000000000, "1 2 3 4 5 6 7 8 9 10"),
    ],
)
def test_large_values(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected



@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        ("1", 10, 2, 2, "All values must be instances of int"),
        (4, "10", 2, 2, "All values must be instances of int"),
        (4, 10, "2", 2, "All values must be instances of int"),
        (4, 10, 2, "2", "All values must be instances of int"),
    ],
)
def test_string_input(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (True, 10, 2, 2, "All values must be instances of int"),
        (4, True, 2, 2, "All values must be instances of int"),
        (4, 10, False, 2, "All values must be instances of int"),
        (4, 10, 2, True, "All values must be instances of int"),
    ],
)
def test_boolean_input(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (4.5, 10, 2, 2, "All values must be instances of int"),
        (4, 10.5, 2, 2, "All values must be instances of int"),
        (4, 10, 2.5, 2, "All values must be instances of int"),
        (4, 10, 2, 2.5, "All values must be instances of int"),
    ],
)
def test_float_input(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (None, 10, 2, 2, "All values must be instances of int"),
        (4, None, 2, 2, "All values must be instances of int"),
        (4, 10, None, 2, "All values must be instances of int"),
        (4, 10, 2, None, "All values must be instances of int"),
    ],
)
def test_none_input(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (-1, 10, 2, 2, "current page & total pages must be greater than 0"),
        (4, -1, 2, 2, "current page & total pages must be greater than 0"),
        (4, 10, -1, 2, "amount & boundaries must be positive int"),
        (4, 10, 2, -1, "amount & boundaries must be positive int"),
    ],
)
def test_negative_input(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected


@pytest.mark.parametrize(
    "current_page, total_pages, boundaries, around, expected",
    [
        (5, 5, 0, 5, "1 2 3 4 5"),
        (1, 3, 0, 3, "1 2 3"),
        (5, 10, 0, 0, "... 5 ..."),
        (1, 10, 0, 0, "1 ..."),
        (1, 10, 0, 2, "1 2 3 ..."),
        (10, 10, 0, 0, "... 10"),
        (9, 10, 0, 2, "... 7 8 9 10"),
    ],
)
def test_boundaries_are_zero(current_page, total_pages, boundaries, around, expected):
    assert generate_pagination(current_page, total_pages, boundaries, around) == expected
