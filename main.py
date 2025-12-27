from ant import Ant
from simulator import Simulator
from PIL import Image
import os
import random

PINK_COLOR = (255, 20, 147)


class Configuration:
    def __init__(self):
        '''
        Konstruktor klasy Configuration
        Zawiera niezbędnę dla symulacji atrybuty 
        '''
        self.simulator = Simulator()
        self.height = self.simulator.window_height
        self.width = self.simulator.window_width
        if self.simulator.image_sel:
            self.background = self.simulator.users_image
        else:
            size = (self.width, self.height)
            self.background = Image.new('RGB', size, 'white')
        self.pixels_access = self.background.load()
        self.ant = Ant(self.background, self.width, self.height)
        self.steps = self.simulator.steps
        self.chance_black = self.simulator.chance_black
        self.result_folder = "result"
        if os.path.exists(self.result_folder):
            os.system(f'rm -rf "{self.result_folder}"')
        os.makedirs(self.result_folder)

    def random_black_change(self):
        '''
        Zamienia kolor pikseli na czarny na obrazie
        w zależności od podanego przez użytkownika
        prawdopodobieństwa wystąpienia czarnego
        '''
        if self.chance_black > 0:
            for x in range(self.width):
                for y in range(self.height):
                    if random.randint(0, 100) < self.chance_black:
                        self.pixels_access[x, y] = (0, 0, 0)

    def start(self):
        '''
        Główna pętla symulacji
        '''
        self.random_black_change()
        # zapisuje pocztkową pozycję mrówki na planszy jako krok_0.png
        save = self.background.copy()
        save.putpixel((self.ant.current_x, self.ant.current_y), PINK_COLOR)
        save.save(os.path.join(self.result_folder, 'krok_0.png'))
        print(f"Rozpoczynam symulację na {self.steps} kroków.")
        print(f"Obrazy będą w folderze: {os.path.abspath(self.result_folder)}")
        for step in range(self.steps):
            self.ant.rotation()
            self.ant.inverse_pixel()
            self.ant.next_step()
            ax, ay = self.ant.current_x, self.ant.current_y
            real_color_under_ant = self.pixels_access[ax, ay]
            self.pixels_access[ax, ay] = PINK_COLOR
            filename = f"krok_{step+1}.png"
            path = os.path.join(self.result_folder, filename)
            self.background.save(path)
            self.pixels_access[ax, ay] = real_color_under_ant
        print("Zakończono.")


if __name__ == '__main__':
    configuration = Configuration()
    configuration.start()
