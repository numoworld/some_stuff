from statistics import median


def quick_sort(items):
    if len(items) <= 1:
        return items
    else:
        pivot = median(
            [
                items[0],
                items[len(items) // 2],
                items[-1]
            ]
        )
        items_less, pivot_items, items_greater = (
            [n for n in items if n < pivot],
            [n for n in items if n == pivot],
            [n for n in items if n > pivot]
        )

        return (
            quick_sort(items_less) +
            pivot_items +
            quick_sort(items_greater)
        )