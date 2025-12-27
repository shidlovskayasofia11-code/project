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
        self.console_informtion()

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
        try:
            mode = int(input("Twój wybór (1-3): "))
        except ValueError:
            print("Taki tryb nie istnieje.")
        if mode == 2:
            path = input("Podaj ścieżkę do obrazka: ")
            if os.path.exists(path):
                try:
                    self.image_sel = True
                    img = Image.open(path).convert('RGB')
                    img = img.convert('1').convert('RGB')
                    self.users_image = img
                    self.window_width, self.window_height = img.size
                except Exception:
                    print("Plik jest uszkodzony")
            else:
                print("Nie znaleziono pliku.")
        else:
            try:
                self.window_width = int(input("Podaj szerokość planszy: "))
                self.window_height = int(input("Podaj wysokość planszy: "))
            except ValueError:
                print("Podane wymiary nie są poprawne")
            if mode == 3:
                try:
                    self.chance_black = int(input("Podaj % czarnych pól: "))
                except ValueError:
                    self.chance_black = 20
        try:
            self.steps = int(input("Podaj liczbę kroków symulacji: "))
        except ValueError:
            print("Błędna liczba!")
