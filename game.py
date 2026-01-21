import pygame as pg
import sys
import random
import time


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
TEKST = pg.font.Font("Pygame/Klikker/font.ttf", 15)
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
        
        if hendelse.type == pg.MOUSEBUTTONDOWN:
            velg = False
                
        

class Spiller:
    def __init__(self, navn):
        self._navn = navn
        self._kliks = 0
        self._upgrade = 0
        self._kliks_perklik = 1
        self._kostnad = 0
        self._merkliksantal = 0

    
    def klik(self):
        self._kliks += self._kliks_perklik
    

        

    def oppgradering(self, sendtin):
        if sendtin == "Mer kliks per kliks":
            Merklikspris = 50 + self._merkliksantal * 10
            if Merklikspris <= self._kliks:
                self._kliks -= Merklikspris
                self._kliks_perklik += 1
                self._merkliksantal += 1 
                return(f"Du kjøpte {sendtin} for {Merklikspris} og har nå {self._kliks} kliks igjen og gjør {self._kliks_perklik} kliks per klik")
            else:
                return(f"Det koster {Merklikspris} du har bare {self._kliks}")
                
            
        elif sendtin == "Pinne":
            pris = 0


        
        return("Du har ikke råd")
        

        



score = FONT.render("1", True, "white")


tekstgi = TEKST.render("", True, "white")

spiller1 = Spiller(navn)

while True:
    skjerm.fill('black')
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if hendelse.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if x >= sirkelx - radius and x <= sirkelx + radius and y >= sirkely - radius and y <= sirkely + radius:
                spiller1.klik()
                tekstgi = TEKST.render("", True, "white")
            if x >= 700:
                if y <= 50:
                    tekst = spiller1.oppgradering("Mer kliks per kliks")
                    tekstgi = TEKST.render(f"{tekst}", True, "white")
                    
                        
                    
                    
    
    pg.draw.circle(skjerm, (200, 0, 0), (sirkelx, sirkely), radius)
    score = FONT.render(f"Antal kliks: {spiller1._kliks}", True, "white")

    skjerm.blit(tekstgi, (SW/2 - tekstgi.get_width()//2, 50))
    skjerm.blit(score, (SW/2 - score.get_width()//2, 10))

    pg.display.update()
    klokke.tick(5)


