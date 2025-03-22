import pytest
from map import Map

def test_grid_to_screen():
    obj = Map()
    assert obj.grid_to_screen(4, 6) == (450, 300)
    assert obj.grid_to_screen(8, 0) == (0, 600)
    assert obj.grid_to_screen(3, 2) == (150, 225)
