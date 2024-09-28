# This directory will be checked with pytest. It will examine
# all files that start with test_*.py and run all functions with
# names that start with test_

from merge import merge
import random


def test_merge() -> None:
    """Test the merge function."""
    x = [1, 2, 3, 4]
    y = [1, 4, 5, 6]
    assert merge(x, []) == x
    assert merge([], y) == y
    assert merge(x, y) == list(sorted(x + y))

    for _ in range(10):
        x = random.sample(range(100), random.randint(1, 10))
        y = random.sample(range(100), random.randint(1, 10))
        x.sort()
        y.sort()
        assert merge(x, y) == list(sorted(x + y))
