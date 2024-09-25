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

    if current_page < 1 or total_pages < 1:
        return "current page & total pages must be greater than 0"
    if around < 0 or boundaries < 0:
        return "amount & boundaries must be positive int"
    if current_page > total_pages:
        return "Current page cannot exceed the total number of pages."
    return ""


def get_left_boundary_pages(boundaries: int, total_pages: int) -> list:
    """Get the left boundary pages."""
    if boundaries > 0:
        return list(range(1, min(boundaries + 1, total_pages + 1)))
    return []


def get_pages_around_current_page(current_page: int, total_pages: int, boundaries: int, around: int) -> tuple:
    """Get the start and end pages around the current page."""
    if boundaries == 0:
        around_start = max(current_page - around, 1)
    else:
        around_start = max(current_page - around, boundaries + 1)

    around_end = min(current_page + around, total_pages - (boundaries if boundaries > 0 else 0))

    return around_start, around_end


def get_start_page_right_boundary(total_pages: int, around_end: int, boundaries: int) -> int:
    """Get the starting page of the right boundary."""
    if boundaries > 0:
        return max(total_pages - boundaries + 1, around_end + 1)
    return around_end + 1


def generate_pagination(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    """Main function to generate pagination."""

    validation_error_message = validate_parameters(current_page, total_pages, boundaries, around)
    if validation_error_message:
        return validation_error_message

    boundaries = min(boundaries, total_pages)
    around = min(around, total_pages)

    pagination = []

    if boundaries == 0:
        around_start = max(current_page - around, 1)
        around_end = min(current_page + around, total_pages)

        if around_start > 1:
            pagination.append("...")

        pagination.extend(range(around_start, around_end + 1))

        if around_end < total_pages:
            pagination.append("...")

        return " ".join(map(str, pagination))

    if boundaries >= total_pages/2:
        return " ".join(map(str, range(1, total_pages + 1)))

    left_bound = get_left_boundary_pages(boundaries, total_pages)
    pagination.extend(left_bound)

    around_start, around_end = get_pages_around_current_page(current_page, total_pages, boundaries, around)

    if around_start > (left_bound[-1] if left_bound else 1) + 1:
        pagination.append("...")

    pagination.extend(range(around_start, around_end + 1))

    right_bound_start = get_start_page_right_boundary(total_pages, around_end, boundaries)

    if right_bound_start > around_end + 1:
        pagination.append("...")

    if boundaries > 0:
        right_bound = list(range(right_bound_start, total_pages + 1))
        pagination.extend(right_bound)
    result = " ".join(map(str, pagination))
    print(result)
    return result
