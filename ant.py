
from PIL import Image
import random


class Ant:
    '''
    Klasa reprezentująca logikę mrówki.
    '''
    def __init__(self, pillow_image: Image, window_width, window_height):
        '''
        Konstrukor klasy.
        Pobiera od uzytkownika obraz, szerokość i wysokość okna.
        '''
        self.pillow_img = pillow_image
        self.window_width = window_width
        self.window_height = window_height
        self.pixels = pillow_image.load()
        self.current_x = window_width // 2
        self.current_y = window_height // 2

    def inverse_pixel(self):
        '''
        Zmiana koloru piksela na przeciwny.
        '''
        current_color = self.pixels[self.current_x, self.current_y]
        if current_color == (0, 0, 0):
            self.pixels[self.current_x, self.current_y] = (255, 255, 255)
        else:
            self.pixels[self.current_x, self.current_y] = (0, 0, 0)

    def rotation(self):
        '''
        Obrót mrówki zależnie od koloru pola.
        '''
        current_color = self.pixels[self.current_x, self.current_y]
        if current_color == (255, 255, 255):
            pass
        else:
            pass

    def verify_position(self, x, y):
        '''
        Sprawdza,czy x i y są na planszy.
        '''
        if 0 <= x < self.window_width and 0 <= y < self.window_height:
            return True
