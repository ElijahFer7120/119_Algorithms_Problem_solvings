"""Optional English-first starter for individual search contracts and correctness."""

from copy import deepcopy

from ticket_data import TICKETS
from search_support import id_key, category_key, matches, compare_values
from ticket_display import show_ticket, show_tickets, show_trace


# MONDAY - Separate the requested value from the traversal.

def linear_search(records, target, key=id_key):
    trace = []
    for i, record in enumerate(records):
        value = key(record)
        trace.append((i, value))
        if matches(value, target):
            return i, trace
    return None, trace
    """Return the first matching position and visits, or None and visits."""
    # Begin an empty trace. Visit records in their existing order.
    # Select each record's value through key(record).
    # Remember its position and selected value before checking for a match.
    # Return the position and trace on a match; otherwise finish with None/trace.
    # Leave the records unchanged. An empty input has no visits.
    raise NotImplementedError("Implement the ordered scan.")


def binary_search(records, target, key=id_key):
    trace = []
    low = 0
    high = len(records) - 1
    while low <= high:
        mid = (low + high) // 2
        value = key(records[mid])
        trace.append((low, high, mid, value))
        cmp = compare_values(value, target)
        if cmp == 0:
            return mid, trace
        elif cmp < 0:
            low = mid + 1
        else:
            high = mid - 1
    return None, trace
    """Return any matching position and interval visits on a key-ordered input."""
    # The caller supplies a list ascending under the same key used here.
    # Begin with an empty trace and an inclusive interval covering the list.
    # While the interval contains candidates, select its integer midpoint.
    # Record low, high, middle, and the selected value before changing bounds.
    # Compare that value with target: match, lower, or higher.
    # Return on equality; otherwise discard the impossible side AND midpoint.
    # When no candidates remain, return None with the visits collected.
    # Do not sort or perform a sortedness scan inside this function.
    raise NotImplementedError("Implement interval narrowing.")


# TUESDAY CHECKPOINT - Verify the contract and preserve an independent submission.

def main():
    """Show completed searches with readable results and teaching traces."""
    show_tickets("Original tickets", TICKETS)
    
    linear_position, linear_trace = linear_search(TICKETS, "T403")
    print(f"Linear search for T403: position={linear_position}")
    show_ticket(
        TICKETS[linear_position] if linear_position is not None else None
    )
    show_trace("linear search for T403", linear_trace)
    
    missing_position, missing_trace = linear_search(TICKETS, "T499")
    print(f"Linear search for T499: position={missing_position}")
    show_ticket(
        TICKETS[missing_position] if missing_position is not None else None
    )
    show_trace("linear search for T499", missing_trace)
    
    id_ordered = sorted(TICKETS, key=id_key)
    binary_position, binary_trace = binary_search(id_ordered, "T403")
    print("\nBinary search for T403 in ID order:")
    show_ticket(
        id_ordered[binary_position] if binary_position is not None else None
    )
    show_trace("binary search for T403", binary_trace)
    
    wrong_order_position, _ = binary_search(TICKETS, "T401")
    linear_t401_position, _ = linear_search(TICKETS, "T401")
    print("\nT401 ordering demonstration:")
    print("Linear search on the original list:")
    show_ticket(
        TICKETS[linear_t401_position]
        if linear_t401_position is not None else None
    )
    if wrong_order_position is None:
        print("Binary search missed T401 on the unsorted list.")
    else:
        print("Binary search returned a position, but the input was still unsorted.")
    print("Binary search can discard the target's side when its input is not ordered.")

    category_ordered = sorted(TICKETS, key=category_key)
    category_position, _ = linear_search(
        category_ordered, "account", key=category_key
    )
    print("\nLinear search for category 'account':")
    show_ticket(
        category_ordered[category_position]
        if category_position is not None else None
    )

    category_position, _ = binary_search(
        category_ordered, "account", key=category_key
    )
    print("\nBinary search for category 'account':")
    show_ticket(
        category_ordered[category_position]
        if category_position is not None else None
    )
    """Show completed searches with readable results and two small teaching traces."""
    # MONDAY: inspect TICKETS, then show found T403 and absent T499 using a scan.
    # Prepare an ID-ascending view outside binary_search; repeat those requests.
    # A result position belongs to the exact list searched; test `is None`.
    # Show one trace from each valid path with show_trace.
    # Deliberately search original unsorted data for T401; explain the miss.
    # Use category_key with a category-ordered view for repeated category account.
    # Accept any matching category record, not necessarily the same position.

    # TUESDAY: finish the boundary/duplicate/nonmutation tests and short README.
    # Run the final personal week_04/AL04 copy before submitting its repo URL.
    # Copy completed functions into AL05 later; preserve this submitted snapshot.
    print("AL04 starter: begin with Monday's linear search.")


if __name__ == "__main__":
    main()