def validate_input(value) -> bool:
    """Check if the input is an integer"""
    return isinstance(value, int) and not isinstance(value, bool)


def validate_parameters(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    """Validate the main parameters for pagination."""
    if not (
        validate_input(current_page)
        and validate_input(total_pages)
        and validate_input(boundaries)
        and validate_input(around)
    ):
        return "All values must be instances of int"

    if (
        total_pages <= 0
        or current_page < 0
        or around < 0
        or boundaries < 0
        
    ):
        return "The values must be positive and within the correct range"

    return ""


def get_left_bound(boundaries: int, total_pages: int) -> list:
    """Get the left boundary pages."""
    return list(range(1, min(boundaries + 1, total_pages + 1))) if boundaries > 0 else []


def get_around_pages(current_page: int, total_pages: int, boundaries: int, around: int) -> tuple:
    """Get the start and end pages around the current page."""
    around_start = max(current_page - around, 1 if boundaries == 0 else boundaries + 1)
    around_end = min(current_page + around, total_pages - (boundaries if boundaries > 0 else 0))
    return around_start, around_end


def get_right_bound(total_pages: int, around_end: int, boundaries: int) -> int:
    """Get the starting page of the right boundary."""
    return max(total_pages - boundaries + 1, around_end + 1) if boundaries > 0 else around_end + 1


def generate_pagination(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    """Main function to generate pagination."""

    validation_error = validate_parameters(current_page, total_pages, boundaries, around)
    if validation_error:
        return validation_error

    boundaries = min(boundaries, total_pages)
    around = min(around, total_pages)

    pagination = []
    try:
        if boundaries >= total_pages:
            return " ".join(map(str, range(1, total_pages + 1)))

        left_bound = get_left_bound(boundaries, total_pages)
        pagination.extend(left_bound)

        around_start, around_end = get_around_pages(current_page, total_pages, boundaries, around)

        if around_start > (left_bound[-1] if left_bound else 1) + 1:
            pagination.append("...")

        pagination.extend(range(around_start, around_end + 1))

        right_bound_start = get_right_bound(total_pages, around_end, boundaries)

        if right_bound_start > around_end + 1:
            pagination.append("...")

        if boundaries > 0:
            right_bound = list(range(right_bound_start, total_pages + 1))
            pagination.extend(right_bound)

    except IndexError:
        return "The values must be positive and within the correct range"

    return " ".join(map(str, pagination))