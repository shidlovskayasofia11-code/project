import os
from PIL import Image


class Simulator:
    '''
    Klasa odpowiedzialna za pobranie wszystkich informacji od użytkownika
    '''
    def __init__(self):
        '''
        Konstrukor klasy
        '''
        self.window_height = 0
        self.window_width = 0
        self.chance_black = 0
        self.steps = 0
        self.image_sel = False
        self.users_image = None

    def console_informtion(self):
        '''
        Metoda dla wypisywania komunikatów,pobrania ścieżki obrazu,
        liczby kroków,wymiarów planszy,prawdopodobieństwa czarnych pól
        '''
        print("---KONFIGURACJA MRÓWKI LANGTONA---")
        print("Wybierz tryb: ")
        print("1 - Białe tło")
        print("2 - Własny czarno-biały obraz")
        print("3 - Losowo wygenerowany czarno-biały obraz")
        mode = int(input("Twój wybór (1-3): "))
        if self.check_int(mode, 'mode'):
            if mode == 2:
                path = input("Podaj ścieżkę do obrazka: ")
                if os.path.exists(path):
                    self.image_sel = True
                    self.users_image, self.winow_width, self.window_height \
                        = self.load_and_process_image(path)
            else:
                self.window_width = int(input("Podaj szerokość planszy: "))
                self.window_height = int(input("Podaj wysokość planszy: "))
                if self.check_int(self.window_width) \
                        and self.check_int(self.window_height):
                    if mode == 3:
                        chance = int(input("Podaj czarnych pól: "))
                        if self.check_int(chance, 'chance'):
                            self.chance_black = chance
                else:
                    raise ValueError('Podana wartość nie jest poprawna')
        else:
            raise ValueError('Podana wartość nie jest poprawna')
        steps = int(input("Podaj liczbę kroków symulacji: "))
        if self.check_int(steps):
            self.steps = steps
        else:
            raise ValueError('Podana wartość nie jest poprawna')

    def check_int(self, input, which_value='standard_int'):
        '''
        Sprawdza liczbę, podaną przez użytkownika,zgodnie z wymaganiami
        '''
        if which_value == 'mode':
            return input in [1, 2, 3]
        elif which_value == 'chance':
            return 0 <= input <= 100
        return input > 1

    def load_and_process_image(self, path):
        """
        Wczytuje obraz, przetwarza go na format czarno-biały
        i zwraca obiekt obrazu oraz jego wymiary.
        """
        try:
            img = Image.open(path).convert('RGB')
            img = img.convert('1').convert('RGB')
            width, height = img.size
            return img, width, height
        except FileNotFoundError:
            print("Nie znaleziono pliku")
        except Exception:
            print("Plik jest uszkodzony")
