from ant import Ant
# from main import Configuration
# import pytest
from PIL import Image


def background():
    width, height = 10, 10
    img = Image.new('RGB', (width, height), 'white')
    return img


def test_ant_check_size():
    '''
    Sprawdza, czy klasa Ant przyjmuje wysokość i szerokość poprawnie
    '''
    ant = Ant(background(), 10, 10)
    assert ant.window_height == 10
    assert ant.window_width == 10


def test_start_position():
    ant = Ant(background(), 10, 10)
    assert ant.current_x == 5
    assert ant.current_y == 5
