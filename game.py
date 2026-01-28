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
nerf = 0

# Initialiser pygame
pg.init()


posklikers = []
klikkers =[ ]


qotes = ["I will build a great, great wall on our southern border, and I will have Mexico pay for that wall. Mark my words.", "I will be phenomenal to the women. I mean, I want to help women.", "The concept of global warming was created by and for the Chinese in order to make U.S. manufacturing non-competitive.", "I have never seen a thin person drinking Diet Coke.", "I'm intelligent. Some people would say I'm very, very, very intelligent.", "My fingers are long and beautiful, as, it has been well documented, are various other parts of my body.", "They're eating the dogs! They're eating the cats! ", "They're eating the pets of the people who live there. ", "I think apologizing's a great thing, but you have to be wrong. I will absolutely apologize, sometime in the hopefully distant future, if I'm ever wrong", "Man, we could use a big fat dose of global warming", "Heidi Klum. Sadly, she's no longer a 10", "a beautiful child went to have the vaccine, and came back and a week later had a tremendous fever, got very, very sick, now is autistic", "Part of the beauty of me is that I am very rich.", "I think the only difference between me and the other candidates is that I'm more honest and my women are more beautiful.", "I love the poorly educated.", "I have a great relationship with the blacks.", "@ariannahuff is unattractive both inside and out. I fully understand why her former husband left her for a man- he made a good decision.", " I've said that if Ivanka weren't my daughter, perhaps I would be dating her.", "I actually don't have a bad hairline.", "The Biden administration spent $8 million making mice transgender", "Canada should become our Cherished 51st State", "I don’t have a racist bone in my body.", "There’s nothing I love more than women, but they’re really a lot different than portrayed. They are far worse than men, far more aggressive", ""]
qotessure = ["Wrong!", "Fake news.", "Sad!", "Total disaster.", "Disgraceful.", "Pathetic.", "A complete joke.", "You’re fired.", "So bad.", "Very unfair.", "Rigged.", "Corrupt.", "Weak.", "Loser.", "A mess.", "Out of control.", "Incompetent.", "Dishonest.", "Terrible.", "So sad.", "Embarrassing.", "Clueless.", "A failure.", "Stupid decision.", "Really bad.", "Unbelievable.", "A joke.", "No idea.", "Failing.", "Disaster.", "Terribly run.", "Fake.", "Not good.", "Very weak.", "Hopeless.", "Shameful.", "Bad deal.", "Totally broken.", "Awful.", "A scam.", "Ridiculous.", "Nonsense.", "Wrong again.", "Very bad people.", "Low energy.", "Crooked.", "An embarrassment.", "Bad leadership.", "A total mess.", "Ghina", "I love women"]

BLOKK_STORELSE = 50
navn = "spiller"
# Font størrelse og utsene 
FONT = pg.font.Font("Pygame/Klikker/font.ttf", 30)
TEKST = pg.font.Font("Pygame/Klikker/font.ttf", 15)
QOTETEKST = pg.font.Font("Pygame/Klikker/font.ttf", 13)
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
        self._merklikspris = 30
        self._klikkere = 0
        self._klikerpris = 200
        self._klikkerkliks = 1
        self._klikerklikspris = 1000


    def klik(self):
        self._kliks += self._kliks_perklik
        self._alltidkliks += self._kliks_perklik

    def autoklik(self):
        self._kliks += (self._klikkerkliks * self._klikkere)

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
spiller1 = Spiller(navn)

upgrades = [
{"navn": "Mer kliks per kliks","rect": pg.Rect(650, 50, 140, 40),"pris": spiller1._merklikspris},
{"navn": "Klikkere","rect": pg.Rect(650, 100, 140, 40), "pris": spiller1._klikerpris},
{"navn": "Klikkerper","rect": pg.Rect(650, 150, 140, 40), "pris": spiller1._klikerklikspris}
]




def tegnuppgrades():
  for upgrade in upgrades:
    pg.draw.rect(skjerm, (80, 80, 80), upgrade["rect"] )
    pg.draw.rect(skjerm, "white", upgrade["rect"], 2)

    tekst = TEKST.render(upgrade["navn"] + f" {upgrade["pris"]}", True, "white")
    skjerm.blit(tekst,(upgrade["rect"].x + 5, upgrade["rect"].y + 10))




def tegnkliker():
    for kliker in klikkers:
        pg.draw.rect(skjerm, (80, 80, 80), kliker["rect"] )



        

bilde = pg.image.load("Pygame/Klikker/bilder/Trump1.png").convert_alpha()
bilde_sirkel = pg.transform.scale(bilde, (radius*2, radius*2))

score = FONT.render("1", True, "white")
rando = random.randint(0, 48)
tekst2 = qotessure[rando]
tekstgi2 = TEKST.render(tekst2, True, "white")

rando = random.randint(0, 10)
tekst3 = qotes[rando]
qotestekst = QOTETEKST.render(tekst3, True, "white")

tekstgi = TEKST.render("", True, "white")



while True:
    bilde_sirkel = pg.transform.scale(bilde, (radius*2, radius*2))
    skjerm.fill('black')
    skjerm.blit(bilde_sirkel, (sirkelx - radius, sirkely - radius))
    for hendelse in pg.event.get():
        if hendelse.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if hendelse.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if x >= sirkelx - radius and x <= sirkelx + radius and y >= sirkely - radius and y <= sirkely + radius:
                spiller1.klik()
                tekstgi = TEKST.render("", True, "white")
                tall = random.randint(1, 15)
                bilde_sirkel = pg.transform.scale(bilde, (radius*2.1, radius*2.1))
                skjerm.blit(bilde_sirkel, (sirkelx - radius, sirkely - radius))


                if tall < 3:
                    rando = random.randint(0, 50)
                    tekst2 = qotessure[rando]
                    tekstgi2 = TEKST.render(tekst2, True, "white")
                    
                    
                tall2 = random.randint(1, 100)
                if tall2 >= 90:
                    rando = random.randint(0, 21)
                    tekst3 = qotes[rando]
                    qotestekst = QOTETEKST.render(tekst3, True, "white")

                

            for upgrade in upgrades:
                if upgrade["rect"].collidepoint(hendelse.pos):
                    tekst = spiller1.oppgradering(upgrade["navn"])
                    tekstgi = TEKST.render(tekst, True, "white")
                    upgrades[0]["pris"] = spiller1._merklikspris
                    upgrades[1]["pris"] = spiller1._klikerpris
                    upgrades[2]["pris"] = spiller1._klikerklikspris
            if byttbilde < spiller1._alltidkliks and bnumer != 11:
                bnumer += 1
                bilde = pg.image.load(f"Pygame/Klikker/bilder/Trump{bnumer}.png").convert_alpha()
                bilde_sirkel = pg.transform.scale(bilde, (radius*2, radius*2))
                byttbilde += 500
                if byttbilde > 1500:
                    byttbilde *= 1.1

    nerf += 1
    if nerf >= 10:
        if spiller1._klikkere > 0:
            spiller1.autoklik()
            nerf = 0                 
                    
                    

    skjerm.blit(bilde_sirkel, (sirkelx - radius, sirkely - radius))

    score = FONT.render(f"Antal kliks: {spiller1._kliks}", True, "white")

    skjerm.blit(tekstgi, (SW/2 - tekstgi.get_width()//2, 50))
    skjerm.blit(tekstgi2, (SW/4 - tekstgi2.get_width()//2, 300))
    skjerm.blit(qotestekst, (SW/2 - qotestekst.get_width()//2, 450))
    skjerm.blit(score, (SW/2 - score.get_width()//2, 10))


    tegnuppgrades()

    pg.display.update()
    klokke.tick(20)


