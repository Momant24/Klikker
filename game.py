import pygame as pg
import sys
import random
import time


# Konstanter
SW, SH = 800, 600


sirkelx = 400
sirkely = 300
radius = 120
Upgradebrede = 700
byttbilde = 200
bnumer = 1

# Initialiser pygame
pg.init()

upgrades = [
{"navn": "Mer kliks per kliks","rect": pg.Rect(650, 50, 140, 40)},
{"navn": "Klikkere","rect": pg.Rect(650, 100, 140, 40)},
{"navn": "Klikkerper","rect": pg.Rect(650, 150, 140, 40)}
]



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
        self._alltidkliks = 0
        self._upgrade = 0
        self._kliks_perklik = 1
        self._kostnad = 0
        self._merklikspris = 30
        self._klikkere = 0
        self._klikerpris = 200
        self._klikkerkliks = 1
        self._klikerklikspris = 1000


    def klik(self):
        self._kliks += self._kliks_perklik
        self._alltidkliks += self._kliks_perklik

    def autoklik(self):
        self._kliks += round(self._klikkerkliks * self._klikkere)

    def oppgradering(self, sendtin):
        if sendtin == "Mer kliks per kliks":
            
            if self._merklikspris <= self._kliks:
                self._kliks -= self._merklikspris
                self._kliks_perklik += 1
                self._merklikspris = round(self._merklikspris * 1.1)
                return(f"Du kjøpte {sendtin} og har nå {self._kliks} kliks igjen og gjør {self._kliks_perklik} kliks per klik")
            else:
                return(f"Det koster {self._merklikspris} du har bare {self._kliks}")
        if sendtin == "Klikkere":
            if self._klikerpris <= self._kliks:
                self._kliks -= self._klikerpris
                self._klikkere += 1
                self._klikerpris = round(self._klikerpris * 1.1)
                return(f"Du kjøpte {sendtin} og har nå {self._klikkere} klikere som kliker for deg")
            else:
                return(f"Det koster {self._klikerpris} du har bare {self._kliks}")
        if sendtin == "Klikkerper":
            if self._klikerklikspris <= self._kliks:
                self._kliks -= self._klikerklikspris
                self._klikkerkliks += 1
                self._klikerklikspris = round(self._klikerklikspris * 1.1)
                return(f"Du kjøpte {sendtin} og klikerne gjør {self._klikkerkliks} per klikk")
            else:
                return(f"Det koster {self._klikerklikspris} du har bare {self._kliks}")

                
            
      

        
        return("Du har ikke råd")
        
def tegnuppgrades():
  for upgrade in upgrades:
    pg.draw.rect(skjerm, (80, 80, 80), upgrade["rect"] )
    pg.draw.rect(skjerm, "white", upgrade["rect"], 2)

    tekst = TEKST.render(upgrade["navn"], True, "white")
    skjerm.blit(tekst,(upgrade["rect"].x + 5, upgrade["rect"].y + 10))

        

bilde = pg.image.load("Pygame/Klikker/bilder/Trump1.png").convert_alpha()
bilde_sirkel = pg.transform.scale(bilde, (radius*2, radius*2))

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
            for upgrade in upgrades:
                if upgrade["rect"].collidepoint(hendelse.pos):
                    tekst = spiller1.oppgradering(upgrade["navn"])
                    tekstgi = TEKST.render(tekst, True, "white")
            if byttbilde < spiller1._alltidkliks and bnumer != 11:
                bnumer += 1
                bilde = pg.image.load(f"Pygame/Klikker/bilder/Trump{bnumer}.png").convert_alpha()
                bilde_sirkel = pg.transform.scale(bilde, (radius*2, radius*2))
                byttbilde += 500
                if byttbilde > 1500:
                    byttbilde *= 1.3
    if spiller1._klikkere > 0:
        spiller1.autoklik()                    
                    
                    

    skjerm.blit(bilde_sirkel, (sirkelx - radius, sirkely - radius))

    score = FONT.render(f"Antal kliks: {spiller1._kliks}", True, "white")

    skjerm.blit(tekstgi, (SW/2 - tekstgi.get_width()//2, 50))
    skjerm.blit(score, (SW/2 - score.get_width()//2, 10))


    tegnuppgrades()

    pg.display.update()
    klokke.tick(5)


