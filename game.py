import pygame as pg
import sys
import random


# Konstanter
SW, SH = 800, 600


sirkelx = 400
sirkely = 300
radius = 120


# Initialiser pygame
pg.init()

BLOKK_STORELSE = 50
navn = "spiller"
# Font størrelse og utsene 
FONT = pg.font.Font("Pygame/Klikker/font.ttf", 30)

skjerm = pg.display.set_mode((SW, SH))
pg.display.set_caption("Klikker")
klokke = pg.time.Clock()
velg = True
while velg:
    skjerm.fill("black")
    tittel = FONT.render("KLIKKER", True, "green")
    tekst1 = FONT.render("Trykk 1 for å starte spiller", True, "white")

    skjerm.blit(tittel, (SW//2 - tittel.get_width()//2, SH//4))
    skjerm.blit(tekst1, (SW//2 - tekst1.get_width()//2, SH//2))

    pg.display.update()
   
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if hendelse.type == pg.KEYDOWN:
            if hendelse.key == pg.K_1:
                start = 1
                velg = False 
                
        

class Spiller:
    def __init__(self, navn):
        self._navn = navn
        self._kliks = 0
        self._upgrade = 0
    
    def klik(self):
        self._kliks += 1
        print("Hei")
        



score = FONT.render("1", True, "white")
score_rect = score.get_rect(center=(SW/2, SH/20))


spiller1 = Spiller(navn)

while True:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if hendelse.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if x >= sirkelx - radius and x <= sirkelx + radius and y >= sirkely - radius and y <= sirkely + radius :
                spiller1.klik()
    
    skjerm.fill('black')
    pg.draw.circle(skjerm, (200, 0, 0), (sirkelx, sirkely), radius)
    score = FONT.render(f"Antal kliks: {spiller1._kliks}", True, "white")
    skjerm.blit(score, (SW/2 - score.get_width()//2, 10))

    pg.display.update()
    klokke.tick(5)


