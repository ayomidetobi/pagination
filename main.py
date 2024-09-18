def generate_pagination(current_page: int, total_pages: int, boundaries: int, around: int) -> str:

    def validate_input(value) -> bool:
        return isinstance(value, int) and not isinstance(value, bool)


    if not (validate_input(current_page) and validate_input(total_pages) and
            validate_input(boundaries) and validate_input(around)):
        return "All values must be instances of int"
    
    if total_pages <= 0 or current_page <= 0 or current_page > total_pages:
        return "The values must be positive and within the correct range"

    pagination = []
    try:
        if boundaries >= total_pages:
            return " ".join(map(str, range(1, total_pages + 1)))


        left_bound = list(range(1, min(boundaries + 1, total_pages + 1)))
        pagination.extend(left_bound)


        around_start = max(current_page - around, boundaries + 1)
        around_end = min(current_page + around, total_pages - boundaries)

        if around_start > left_bound[-1] + 1:
            if left_bound[-1] != around_start - 1:
                pagination.append("...")


        pagination.extend(range(around_start, around_end + 1))


        right_bound_start = max(total_pages - boundaries + 1, around_end + 1)


        if right_bound_start > around_end + 1:
            if around_end != right_bound_start - 1:
                pagination.append("...")

        right_bound = list(range(right_bound_start, total_pages + 1))
        pagination.extend(right_bound)

    except IndexError:
        return ""

    
    pagination_str = " ".join(map(str, pagination))
    return pagination_str
