import pygame as pg
import sys
import random


# Konstanter
SW, SH = 800, 600


sirkelx = 400
sirkely = 300


# Initialiser pygame
pg.init()

BLOKK_STORELSE = 50

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

skjerm.fill('black')
pg.draw.circle(skjerm, (200, 0, 0), (sirkelx, sirkely), 120)

while True:
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if hendelse.type == pg.MOUSEBUTTONDOWN and mouse_x:
            print("Hello")

    click = pg.mouse.get_pressed()
    if click[0] == True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        print(mouse_x)

    pg.display.update()
    klokke.tick(5)


