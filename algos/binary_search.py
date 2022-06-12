def find_index(elements, value):
    """Finds index of an element from sorted(ASC) list of elements with given value"""

    lo, hi = 0, len(elements) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_el = elements[mid]

        if mid_el == value:
            return mid
        elif mid_el < value:
            lo = mid + 1
        elif mid_el > value:
            hi = mid - 1

    return -1
