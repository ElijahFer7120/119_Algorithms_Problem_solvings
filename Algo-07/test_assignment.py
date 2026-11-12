"""Optional AL07 test starting point; expand it with your own expectations."""

from main import greedy_change, calculate_cached
from investigation_support import exhaustive_change, cached_fibonacci, uncached_fibonacci


def test_tuesday():
    """Begin with an independently reasoned payment counterexample."""
    assert greedy_change([1, 4, 6], 8) == [6, 1, 1]
    assert exhaustive_change([1, 4, 6], 8) == [4, 4]
    
    # Stuck-but-reachable case: greedy fails but exhaustive succeeds.
    assert greedy_change([4, 6], 8) is None
    assert exhaustive_change([4, 6], 8) == [4, 4]
    # Impossible case: no combination can reach the target.
    assert greedy_change([4, 6], 7) is None
    assert exhaustive_change([4, 6], 7) is None
    # Agreement case: greedy and exhaustive should match.
    assert greedy_change([1, 5, 10], 12) == exhaustive_change([1, 5, 10], 12)
    # Zero-target case: should return an empty list.
    assert greedy_change([1, 4, 6], 0) == []
    assert exhaustive_change([1, 4, 6], 0) == []
    # Input list should not be modified by the function.
    coins = [1, 4, 6]
    greedy_change(coins, 8)
    assert coins == [1, 4, 6]
    # Can also check that exhaustive_change does not modify the input list.
    #* AI suggested adding the check for exhaustive_change below
    coins = [1, 4, 6]
    exhaustive_change(coins, 8)
    assert coins == [1, 4, 6]


def test_thursday():
    """Check saved answers and bounded counts against a hand-checkable input."""
    result, calls, hits, cache = cached_fibonacci(5, calculate_cached)
    assert result == 5
    assert calls == 9
    assert hits == 3
    assert len(cache) == 6
    
    result, calls, hits, cache = cached_fibonacci(0, calculate_cached)
    assert result == 0
    assert cache == {0: 0}
    
    result, calls, hits, cache = cached_fibonacci(1, calculate_cached)
    assert result == 1
    assert cache == {1: 1}
    
    result, calls, hits, cache = cached_fibonacci(6, calculate_cached)
    assert result == 8
    
    first = cached_fibonacci(5, calculate_cached)
    second = cached_fibonacci(5, calculate_cached)
    assert first[:3] == second[:3]
    assert first[3] == second[3]
    assert first[3] is not second[3]
    # Add base cases, another known answer, fresh repeated runs, and invalid n.


if __name__ == "__main__":
    test_tuesday()
    # THURSDAY: uncomment the following call when implementing the cache.
    test_thursday()
    print("Tuesday starting check passed after tests expanded.")
    print("Thursday starting check passed after tests expanded.")