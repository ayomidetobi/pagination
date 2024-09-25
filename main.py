def validate_input(value) -> bool:
    """Check if the input is an integer"""
    return isinstance(value, int) and not isinstance(value, bool)


def validate_parameters(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    """Validate the main parameters for pagination."""
    for argument in [current_page, total_pages, boundaries, around]:
        if not validate_input(argument):
            return "All values must be instances of int"
    if current_page < 1 or total_pages < 1:
        return "current page & total pages must be greater than 0"
    if around < 0 or boundaries < 0:
        return "amount & boundaries must be positive int"
    if current_page > total_pages:
        return "Current page cannot exceed the total number of pages."
    return ""


def get_boundaries(total_pages: int, boundaries: int) -> tuple:
    """Get start and end boundaries."""
    if boundaries <= total_pages:
        start_boundary = list(range(1, boundaries + 1))
        end_boundary = list(range(total_pages - boundaries + 1, total_pages + 1))
    else:
        start_boundary = end_boundary = list(range(1, total_pages + 1))
    return start_boundary, end_boundary


def get_around_pages(current_page: int, total_pages: int, around: int) -> list:
    """Get the range of pages around the current page."""
    start_around = max(current_page - around, 1)
    end_around = min(current_page + around, total_pages)
    return list(range(start_around, end_around + 1))


def generate_pagination(current_page: int, total_pages: int, boundaries: int, around: int) -> str:
    """Main function to generate pagination."""
    validation_error = validate_parameters(current_page, total_pages, boundaries, around)
    if validation_error:
        return validation_error

    start_boundary, end_boundary = get_boundaries(total_pages, boundaries)
    current_around = get_around_pages(current_page, total_pages, around)

    
    visible = sorted(set(start_boundary + current_around + end_boundary))

    result_list = [visible[0]]
    for page in range(1, len(visible)):
        if visible[page] == visible[page - 1] + 1:
            result_list.append(visible[page])
        else:
            result_list.append(f"... {visible[page]}")

   
    if boundaries == 0:
        if result_list[0] != 1:
            result_list.insert(0, "...")
        if current_around[-1] != total_pages:
            result_list.append("...")

    return " ".join(map(str, result_list))