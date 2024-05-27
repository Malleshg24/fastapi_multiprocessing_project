import pytest
from app.utils.addition import add_lists

def test_add_lists():
    assert add_lists([[1, 2], [3, 4]]) == [3, 7]
    assert add_lists([[], [1, 2, 3]]) == [0, 6]
    assert add_lists([[0], [0, 0]]) == [0, 0]
    with pytest.raises(TypeError):
        add_lists([[1, 'a'], [3, 4]])
