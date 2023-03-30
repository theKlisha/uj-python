from os import write
from pathlib import Path
import pygame
from random import randint

pygame.init()
path = Path("score")

# kolory
CZARNY = (0, 0, 0)
BIALY = (255, 255, 255)

class Rakietka(pygame.sprite.Sprite):
    # klasa Rakietka dziedziczy z klasy "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy najpierw konstruktor klasy bazowej (Sprite)
        # dzięki metodzie super() dziedziczymy wszystkie elementy klasy bazowej
        super().__init__()

        # przekazanie koloru Rakietka oraz szerokości i wysokości, kolor tła i ustawienie go na przezroczyste
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysuję Rakietka jako prostokąt
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def moveLeft(self, pixels):
        self.rect.x -= pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x < 0:
           self.rect.x = 0

    def moveRight(self, pixels):
        self.rect.x += pixels
        # sprawdzanie położenia brzegowego
        if self.rect.x > 600:
           self.rect.x = 600



class Pilka(pygame.sprite.Sprite):
    # klasa Pilka dziedziczy ze "Sprite" w Pygame.

    def __init__(self, color, width, height):
        # wołamy konstruktor klasy bazowej
        super().__init__()

        # przekazujemy rozmiary, kolor, przezroczystość
        self.image = pygame.Surface([width, height])
        self.image.fill(CZARNY)
        self.image.set_colorkey(CZARNY)

        # rysowanie piłki (jako prostokącika)
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # losowanie prędkości
        self.velocity = [randint(4, 8), randint(1, 4)]

        # pobieramy prostokąt (jego rozmiary) z obiektu image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def bounce(self):
        self.velocity[0] = -self.velocity[0]
        self.velocity[1] = randint(-8,8)

def getHighScore():
    try:
        f = open(path, 'r')
        s = int(f.read())
        f.close()
        return s
    except:
        return 0

def writeHighScore(score): 
    f = open(path, 'w')
    f.write(str(score))
    f.close()

# definiujemy rozmiary i otwieramy nowe okno
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

rakietka = Rakietka(BIALY, 100, 10)
rakietka.rect.x = 300
rakietka.rect.y = 475

pileczka = Pilka(BIALY, 10, 10)
pileczka.rect.x = 345
pileczka.rect.y = 0

# lista wszystkich widzalnych obiektów potomnych z klasy Sprite
all_sprites_list = pygame.sprite.Group()

# dodanie obu rakietek i piłeczki do listy
all_sprites_list.add(rakietka)
all_sprites_list.add(pileczka)

# zaczynamy właściwy blok programu
kontynuuj = True

# służy do kontroli liczby klatek na sekudnę (fps)
clock = pygame.time.Clock()

# Początkowe wyniki graczy
score = 0
done = False

# -------- GLÓWNA PĘTLA PROGRAMU -----------
while kontynuuj:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # zamknięcie okienka
            kontynuuj = False

    if not done:
        # ruchy obiektów Rakietkas klawisze strzałka góra dół lub klawisz w s
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            rakietka.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            rakietka.moveRight(5)

        # aktualizacja listy duszków
        all_sprites_list.update()

        # sprawdzenie czy piłeczka nie uderza w którąś ścianę
        # i odpowiednie naliczenie punktu jeśli minie rakietkę A lub B i uderzy w ścianę za nią
        if pileczka.rect.x >= 690:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.x <= 0:
            pileczka.velocity[0] = -pileczka.velocity[0]
        if pileczka.rect.y > 490:
            pileczka.velocity[1] = -pileczka.velocity[1]
            done = True
        if pileczka.rect.y < 0:
            pileczka.velocity[1] = -pileczka.velocity[1]

        # sprawdzenie kolizji piłeczki z obiektem rakietkaA lub rakietkaB
        if pygame.sprite.collide_mask(pileczka, rakietka):
            score += 1
            pileczka.bounce()

    # RYSOWANIE
    # czarny ekran
    screen.fill(CZARNY)

    # narysowanie obiektów
    all_sprites_list.draw(screen)

    if done:
        # wyświetlanie wyników
        highScore = getHighScore()
        font = pygame.font.Font(None, 42)
        text1 = font.render("wynik: {}".format(score), 1, BIALY)
        text2 = font.render("najlepszy wynik: {}".format(highScore), 1, BIALY)
        screen.blit(text1, (30, 30))
        screen.blit(text2, (30, 70))

        if highScore < score:
            writeHighScore(score)

    # odświeżenie / przerysowanie całego ekranu
    pygame.display.flip()

    # 60 klatek na sekundę
    clock.tick(60)

# koniec
pygame.quit()
