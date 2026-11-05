"""Optional English-first starter for stable sorting and a key-correct pipeline."""

from ticket_data import TICKETS
from search_support import compare_values, id_key, days_key
from pipeline_support import select_open_tickets
from ticket_display import show_ticket, show_tickets, show_trace


# After preparing your local search_algorithms.py, add its search imports here.
# Copy your AL04 functions/imports, or use the instructor-released recovery module.



# TUESDAY - Stable ordering, with counts for one tiny example.

def insertion_sort(records, key):
    ordered = list(records)
    comparisons = 0
    moves = 0
    
    trace = []
    for position in range(1, len(ordered)):
        current = ordered[position]
        i = position - 1
        while i >= 0:
            comparisons += 1
            if key(ordered[i]) <= key(current):
                break
            ordered[i + 1] = ordered[i]
            moves += 1
            i -= 1
        ordered[i + 1] = current
        trace.append([position, [r["id"] for r in ordered]])
    return ordered, comparisons, moves, trace

# THURSDAY - Compose existing interfaces; rebuild after the eligibility change.

def build_views(records, minimum_days=4):
    """Return selected, age-display, and ID-search lists sharing eligible records."""
    selected = select_open_tickets(records, minimum_days)
    age_display, _, _, _ = insertion_sort(selected, days_key)
    id_search = sorted(selected, key=id_key)
    return selected, age_display, id_search

def linear_search(records, target, key=id_key):
    """Return the first matching position and visits, or None and visits."""
    trace = []
    for i, record in enumerate(records):
        value = key(record)
        trace.append((i, value))
        if compare_values(value, target) == 0:
            return i, trace
    return None, trace

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

def main():
    selected = select_open_tickets(TICKETS, 4)
    ordered, comparisons, moves, trace = insertion_sort(selected, days_key)
    show_tickets("Open tickets, age >= 4 (stable, by days_open)", ordered)
    show_trace("Insertion sort trace for open tickets, age >= 4 (stable)", trace)
    print(f"Comparisons: {comparisons}, right-shifts: {moves}")
    print("matches sorted():", ordered == sorted(selected, key=days_key))
    print("Source unchanged:", len(TICKETS), "records")
    
    selected, age_display, id_search = build_views(TICKETS, 4)
    for target in ("T403", "T499",):
        pos, _ = binary_search(id_search, target, id_key)
        print(f"{target}: index {pos} in id_search")
        if pos is not None:
            show_ticket(id_search[pos])
            print(" Same record in age_display at index", age_display.index(id_search[pos]))

    wrong, _ = binary_search(age_display, "T406", id_key)
    print(f"T406 on age display: {wrong} (binary search needs the list sorted by the searched key)")
    
    for limit in (7, 8):
        selected, age_display, id_search = build_views(TICKETS, limit)
        print(f"Minimum days = {limit}: {len(selected)} selected")
        if not selected:
            print(" No tickets meet the minimum days requirement.")
            
    print("Finished building views for all minimum days limits.")
    
    """Present completed daily stages and explain the issued threshold change."""
    # TUESDAY: select open tickets aged at least 4 days; show stable age ordering.
    # Label the tiny ID trace and comparison/right-shift counts as teaching evidence.
    # Check your sort against sorted, including tied keys and unchanged source.

    # THURSDAY: build both views and use the local search_algorithms functions.
    # Find T403 and absent T499; resolve positions in the particular list searched.
    # Deliberately use the age display for ID binary search of T406; explain failure.
    # Rebuild from TICKETS at minimum_days=7, then 8, to show revised/empty results.
    # Keep app output readable; put short workload/copy/change notes in README.md.
    # Test and submit the complete personal week_04/AL05 folder independently.
if __name__ == "__main__":
    main()