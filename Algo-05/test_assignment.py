"""Unfinished prompts for sort stability, pipeline contracts, and rule revision."""

from copy import deepcopy
from main import insertion_sort, build_views
from search_support import id_key, days_key
from ticket_data import TICKETS
from pipeline_support import select_open_tickets

def ids(records):
    return [r["id"] for r in records]

def assignment_checks():
    
    for empty in ([], [TICKETS[0]]):
        out, comparisons, moves, trace = insertion_sort(empty, days_key)
        assert out == empty and out is not empty and comparisons == 0 and moves == 0
        
    
    base = sorted(TICKETS, key=days_key)
    for data in (base, base[::-1], TICKETS):
        before = deepcopy(data)
        out, _, _, trace = insertion_sort(data, days_key)
        assert out == sorted(data, key=days_key) 
        assert data == before
        assert out is not data
        assert all(any(o is r for r in data) for o in out)
    
    tied = [TICKETS[0], TICKETS[2]]
    assert ids(insertion_sort(tied, days_key)[0]) == ["T403", "T405"]
    assert ids(insertion_sort(tied[::-1], days_key)[0]) == ["T405", "T403"]
    
    small = select_open_tickets(TICKETS, 4)
    out, comparisons, moves, trace = insertion_sort(small, days_key)
    assert ids(out) == ["T406", "T402", "T403", "T405"]
    assert trace == [
        [1, ["T403", "T405", "T402", "T406"]],
        [2, ["T402", "T403", "T405", "T406"]],
        [3, ["T406", "T402", "T403", "T405"]],
    ]
    assert moves == 5
    assert comparisons == 6 
    
    expected = {
        4: (["T403", "T405", "T402", "T406"], ["T406", "T402", "T403", "T405"],
            ["T402", "T403", "T405", "T406"]),
        7: (["T403", "T405"], ["T403", "T405"], ["T403", "T405"]),   # boundary: 7 is included
        8: ([], [], []),
    }
    
    for limit, (sel_ids, age_ids, id_ids) in expected.items():
        sel, age, idv = build_views(TICKETS, limit)
        assert ids(sel) == sel_ids
        assert ids(age) == age_ids
        assert ids(idv) == id_ids
        assert "T404" not in ids(sel)               
        assert all(a is any_s for a, any_s in zip(sel, sel))
        assert all(any(r is s for s in sel) for r in age + idv) 
    
    assert "T406" in ids(build_views(TICKETS, 4)[0])
    assert "T406" not in ids(build_views(TICKETS, 5)[0])

    assert len(TICKETS) == 6 and TICKETS[0]["id"] == "T403"
    
    fixture = deepcopy(TICKETS)
    fixture[3]["status"] = "completed"  
    assert "T402" not in ids(build_views(fixture, 4)[0])
    assert "T402" in ids(build_views(TICKETS, 4)[0])
    """Check expected orders, stable ties, shared records, and rebuilt query views."""
    # TUESDAY: test empty/singleton, ordered/reverse/shuffled inputs, and stable ties.
    # Compare output with sorted under the same key; source order/fields stay intact.
    # Check new outer list and shared record identities, using `is` where useful.
    # Check the small fixture's expected counts and ID trace, not timing.
    # THURSDAY: check exact selected/display/search IDs at thresholds 4, 7, and 8.
    # Include boundary ages and completed-ticket exclusion; rebuild from TICKETS.
    # Import your local searches when ready: test found/missing and view positions.
    # Mark wrong-view T406 as deliberate invalid use, separate from valid contracts.
    # Use a separate fixture copy if testing a field edit; do not alter shared seed.
    


if __name__ == "__main__":
    if not __debug__:
        raise SystemExit("Run tests without -O so assertions are enabled.")
    print("AL05 checks passed.")