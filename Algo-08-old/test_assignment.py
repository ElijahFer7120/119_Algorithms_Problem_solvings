"""Optional focused check starting points; expand them across the week."""

from network_support import validate_model
from main import breadth_first, depth_first, shortest_hop_path, MY_RESTRICTION
from network_data import GRAPH, START, GOAL, RESTRICTIONS

TEST_STAGE = 3  # Raise to 2 Tuesday and 3 Thursday after completing those tests.


def test_model():
    """Begin Monday with a clearly valid two-way model and an unknown reference."""
    assert validate_model({"A": ["B"], "B": ["A"]}) == []
    assert validate_model({"A": ["Missing"]}) == ["A: unknown node Missing"]
    # Add your one broken-and-repaired copy of the workshop model.
    original = {room: neighbors.copy() for room, neighbors in GRAPH.items()}
    copy = {room: neighbors.copy() for room, neighbors in GRAPH.items()}

    copy["Office"].append("Breakroom")
    assert validate_model(copy) == ["Office: unknown node Breakroom"]

    copy["Office"].remove("Breakroom")
    assert validate_model(copy) == []
    assert GRAPH == original


def test_traversals():
    """Check independent expectations before trying the full workshop fixture."""
    tiny = {"A": ["B", "C"], "B": ["A"], "C": ["A"], "D": []}
    
    original = {node: neighbors[:] for node, neighbors in tiny.items()}
    
    bfs_order, bfs_trace, bfs_edges = breadth_first(tiny, "A")
    assert bfs_order == ["A", "B", "C"]
    assert [step["processed"] for step in bfs_trace] == bfs_order
    assert bfs_edges == 4
    
    dfs_order, dfs_trace, dfs_edges = depth_first(tiny, "A")
    assert dfs_order == ["A", "B", "C"]
    assert [step["processed"] for step in dfs_trace] == dfs_order
    assert dfs_edges == 4
    # Assert expected orders, no repeated processing, four adjacency entries,
    # and source preservation using both functions.
    assert tiny == original


def test_paths_and_personal_case():
    original_graph = {
    room: neighbors.copy() for room, neighbors in GRAPH.items()
    }
    tiny = {"A": ["B", "C"], "B": ["A"], "C": ["A"], "D": []}
    path, parents = shortest_hop_path(tiny, "A", "C")
    assert path == ["A", "C"]
    assert parents == {"A": None, "B": "A", "C": "A"}
    
    expected_b = None

    personal_blocked = RESTRICTIONS[MY_RESTRICTION]["blocked"]
    path_b, _ = shortest_hop_path(
        GRAPH, START, GOAL, blocked=personal_blocked
    )
    assert path_b == expected_b

    assert shortest_hop_path(tiny, "A", "A") == (["A"], {"A": None})
    assert shortest_hop_path(tiny, "A", "D") == (
        None,
        {"A": None, "B": "A", "C": "A"},
    )

    assert shortest_hop_path(tiny, "A", "C", blocked={"C"}) == (None, {})
    baseline, _ = shortest_hop_path(GRAPH, START, GOAL)
    assert baseline == ["Entrance", "Reception", "Office", "Loading"]

    annex_path, _ = shortest_hop_path(GRAPH, START, "Annex")
    assert annex_path is None
    
    assert GRAPH == original_graph
    """Check route boundaries and your issued blocked-node result independently."""
    # Check a small known path, start=goal, disconnected goal, and a blocked endpoint.
    # Import the supplied workshop data and use MY_RESTRICTION for your personal case.
    # Check exact expected endpoints/hops or None, consecutive connections, no blocked
    # rooms in a returned route, and unchanged source data.


if __name__ == "__main__":
    test_model()
    if TEST_STAGE >= 2:
        test_traversals()
    if TEST_STAGE >= 3:
        test_paths_and_personal_case()
    print("Selected-stage starting checks passed; complete all stages before submission.")
