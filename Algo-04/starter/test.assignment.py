"""Unfinished test prompts; replace the final stop with your own focused checks."""

from copy import deepcopy
from main import linear_search, binary_search
from ticket_data import TICKETS
from search_support import id_key, category_key, matches


def assignment_checks():
    records = deepcopy(TICKETS)
    original_records = deepcopy(records)
    original_tickets = deepcopy(TICKETS)
    
    position, trace = linear_search(records, "T403")
    assert position == 0
    assert id_key(records[position]) == "T403"
    assert trace == [(0, "T403")]

    position, trace = linear_search(records, "T499")
    assert position is None
    assert trace == [
        (i, id_key(record)) for i, record in enumerate(records)
    ]

    assert linear_search([], "T403") == (None, [])

    single = [deepcopy(records[0])]
    assert linear_search(single, "T403")[0] == 0
    assert linear_search(single, "T499") == (None, [(0, "T403")])
    
    id_ordered = sorted(records, key=id_key)
    id_ordered_before = deepcopy(id_ordered)
    
    for target, expected_position in (("T401", 0), ("T406", len(id_ordered) - 1)):
        position, trace = binary_search(id_ordered, target)
        assert position == expected_position
        assert id_key(id_ordered[position]) == target
        assert any(value == target for _, _, _, value in trace)

    for target in ("T000", "T403A", "T999"):
        position, trace = binary_search(id_ordered, target)
        assert position is None

    assert binary_search([], "T403") == (None, [])
    
    _, binary_trace = binary_search(id_ordered, "T403")
    for low, high, middle, value in binary_trace:
        assert 0 <= low <= middle <= high < len(id_ordered)
        assert value == id_key(id_ordered[middle])
    assert any(value == "T403" for _, _, _, value in binary_trace)
    
    category_ordered = sorted(records, key=category_key)
    category_ordered_before = deepcopy(category_ordered)

    for search in (linear_search, binary_search):
        position, _ = search(
            category_ordered, "account", key=category_key
        )
        assert position is not None
        assert category_key(category_ordered[position]) == "account"
        
    assert linear_search(records, "T401")[0] == 1
    assert binary_search(records, "T401")[0] is None
    
    assert records == original_records
    assert TICKETS == original_tickets
    assert id_ordered == id_ordered_before
    assert category_ordered == category_ordered_before

    """Check independent expected answers, boundaries, traces, and input preservation."""
    # MONDAY: use a separate fixture copy and an independently expected found ID.
    # Check missing, empty, singleton, first/last ID, and valid position zero.
    # Prepare ID order for binary tests. Check absent below/between/above IDs.
    # Check trace contents include the matching visit and actual input values.
    # TUESDAY: use category order and accept any matching duplicate category.
    # Check unchanged input order/fields, including after unsuccessful searches.
    # Separately demonstrate T401's deliberate invalid-order miss on TICKETS.
    # Agreement between two implementations alone is not an independent oracle.


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    assignment_checks()
    print("AL04 checks passed.")