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
teller = 0
grønlandkjøpt = False
dragrønnland = False

# Initialiser pygame
pg.init()

posklikers = []
klikkers =[ ]


qotes = ["I will build a great, great wall on our southern border, and I will have Mexico pay for that wall. Mark my words.", "I will be phenomenal to the women. I mean, I want to help women.", "The concept of global warming was created by and for the Chinese in order to make U.S. manufacturing non-competitive.", "I have never seen a thin person drinking Diet Coke.", "I'm intelligent. Some people would say I'm very, very, very intelligent.", "My fingers are long and beautiful, as, it has been well documented, are various other parts of my body.", "They're eating the dogs! They're eating the cats! ", "They're eating the pets of the people who live there. ", "I think apologizing's a great thing, but you have to be wrong. I will absolutely apologize, sometime in the hopefully distant future, if I'm ever wrong", "Man, we could use a big fat dose of global warming", "Heidi Klum. Sadly, she's no longer a 10", "a beautiful child went to have the vaccine, and came back and a week later had a tremendous fever, got very, very sick, now is autistic", "Part of the beauty of me is that I am very rich.", "I think the only difference between me and the other candidates is that I'm more honest and my women are more beautiful.", "I love the poorly educated.", "I have a great relationship with the blacks.", "@ariannahuff is unattractive both inside and out. I fully understand why her former husband left her for a man- he made a good decision.", " I've said that if Ivanka weren't my daughter, perhaps I would be dating her.", "I actually don't have a bad hairline.", "The Biden administration spent $8 million making mice transgender", "Canada should become our Cherished 51st State", "I don’t have a racist bone in my body.", "There’s nothing I love more than women, but they’re really a lot different than portrayed. They are far worse than men, far more aggressive", ""]
qotessure = ["Wrong!", "Fake news.", "Sad!", "Total disaster.", "Disgraceful.", "Pathetic.", "A complete joke.", "You’re fired.", "So bad.", "Very unfair.", "Rigged.", "Corrupt.", "Weak.", "Loser.", "A mess.", "Out of control.", "Incompetent.", "Dishonest.", "Terrible.", "So sad.", "Embarrassing.", "Clueless.", "A failure.", "Stupid decision.", "Really bad.", "Unbelievable.", "A joke.", "No idea.", "Failing.", "Disaster.", "Terribly run.", "Fake.", "Not good.", "Very weak.", "Hopeless.", "Shameful.", "Bad deal.", "Totally broken.", "Awful.", "A scam.", "Ridiculous.", "Nonsense.", "Wrong again.", "Very bad people.", "Low energy.", "Crooked.", "An embarrassment.", "Bad leadership.", "A total mess.", "Ghina", "I love women"]

BLOKK_STORELSE = 50
navn = "spiller"

# Font størrelse og utsene 

FONT = pg.font.SysFont("arial", 30)
TEKST = pg.font.SysFont("arial", 15)
QOTETEKST = pg.font.SysFont('arial', 15, bold=False) 

skjerm = pg.display.set_mode((SW, SH))

pg.display.set_caption("Klikker")
klokke = pg.time.Clock()
velg = True
while velg:
    skjerm.fill("black")
    tittel = FONT.render("TRUMP KLIKKER", True, "orange")
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
        self._klikerpris = 100
        self._klikkerkliks = 1
        self._klikerklikspris = 5
        self._defendgrønlandpris = 10
        self._grønnlandcoins = 0


    def klik(self):
        self._kliks += self._kliks_perklik
        self._alltidkliks += self._kliks_perklik

    def autoklik(self):
        self._kliks += (self._klikkerkliks * self._klikkere)

    def oppgradering(self, sendtin):
        global bilde
        global dragrønnland
        global grønlandkjøpt
        if sendtin == "Mer kliks per kliks":
            
            if self._merklikspris <= self._kliks:
                self._kliks -= self._merklikspris
                self._kliks_perklik += 1
                self._merklikspris = round(self._merklikspris * 1.1)
                return(f"Du kjøpte {sendtin}")
            else:
                return(f"Det koster {self._merklikspris}")
        if sendtin == "Klikkere":
            if self._klikerpris <= self._kliks:
                self._kliks -= self._klikerpris
                self._klikkere += 1
                self._klikerpris = round(self._klikerpris * 1.1)
                adklikerbilde()
                bilde = pg.image.load(f"Pygame/Klikker/bilder/Trump7.png").convert_alpha()

                
                return(f"Du kjøpte {sendtin}")
            else:
                return(f"Det koster {self._klikerpris}")
        if sendtin == "Klikkerper":
            if self._klikerklikspris <= self._grønnlandcoins:
                self._grønnlandcoins -= self._klikerklikspris
                self._klikkerkliks += 1
                self._klikerklikspris = self._klikerklikspris * 2
                return(f"Du kjøpte {sendtin}")
            else:
                return(f"Det koster {self._klikerklikspris} du har {self._grønnlandcoins} Grønnlandcoins")
        
        if sendtin == "Defend Grønnland":

            if self._defendgrønlandpris <= self._kliks and grønlandkjøpt == False:
                self._kliks -= self._defendgrønlandpris
                grønlandkjøpt = True
                self._defendgrønlandpris = 0
                return(f" {sendtin}")
            elif grønlandkjøpt == True:
                dragrønnland = True
                return("drar grønland")

            else:
                return(f"Det koster {self._klikerklikspris} du har bare {self._kliks}")
        
                
            
      

        
        return("Du har ikke råd")
spiller1 = Spiller(navn)

upgrades = [
{"navn": "Mer kliks per kliks","rect": pg.Rect(650, 50, 140, 40),"pris": spiller1._merklikspris},
{"navn": "Klikkere","rect": pg.Rect(650, 100, 140, 40), "pris": spiller1._klikerpris},
{"navn": "Klikkerper","rect": pg.Rect(650, 150, 140, 40), "pris": f"{spiller1._klikerklikspris}G"},
{"navn": "Defend Grønnland","rect": pg.Rect(650, 200, 140, 40), "pris": spiller1._defendgrønlandpris}
]





def tegnuppgrades():
    
    upgrades = [
    {"navn": "Mer kliks per kliks","rect": pg.Rect(650, 50, 140, 40),"pris": spiller1._merklikspris},
    {"navn": "Klikkere","rect": pg.Rect(650, 100, 140, 40), "pris": spiller1._klikerpris},
    {"navn": "Klikkerper","rect": pg.Rect(650, 150, 140, 40), "pris": f"{spiller1._klikerklikspris}G"},
    {"navn": "Defend Grønnland","rect": pg.Rect(650, 200, 140, 40), "pris": spiller1._defendgrønlandpris}
    ]

    for upgrade in upgrades:
        pg.draw.rect(skjerm, (80, 80, 80), upgrade["rect"] )
        pg.draw.rect(skjerm, "white", upgrade["rect"], 2)

        tekst = TEKST.render(upgrade["navn"] + f" {upgrade["pris"]}", True, "white")
        skjerm.blit(tekst,(upgrade["rect"].x + 5, upgrade["rect"].y + 10))

def tegntekstantall():
    tingduhar = [
    {"tekst": "Hvor mange kliks per klik du gjør:", "antall": spiller1._kliks_perklik, "rect": pg.Rect(25, 50, 140, 40)},
    {"tekst": "Hvor mange klikkere du har:", "antall": spiller1._klikkere, "rect": pg.Rect(25, 70, 140, 40)},
    {"tekst": "Hvor mange kliks en klikker gjør:", "antall": spiller1._klikkerkliks, "rect": pg.Rect(25, 90, 140, 40)}
    ]
    for ting in tingduhar:


        tekst = TEKST.render(ting["tekst"] + f" {ting["antall"]}", True, "white")
        skjerm.blit(tekst,(ting["rect"].x + 5, ting["rect"].y + 10))
bildexstørelse = 50
bildeystørelse = 50

def tegnkliker(bredde, høyde):
    for kliker in klikkers:
        bilde = pg.transform.scale(kliker["bilde"], (bredde, høyde))
        midt_x, midt_y = kliker["rect"].center
        nytt_rect = bilde.get_rect(center=(midt_x, midt_y))
        
        skjerm.blit(bilde, nytt_rect)


def adklikerbilde():

    bilder = ["Pygame/Klikker/bilder/Kamala.png", "Pygame/Klikker/bilder/vaksine.png", "Pygame/Klikker/bilder/Peace.png", "Pygame/Klikker/bilder/Pride.png", "Pygame/Klikker/bilder/Mandani.png", "Pygame/Klikker/bilder/Demokratene.png"]


    hvilken = random.randint(0, len(bilder)-1)
    bilde = pg.image.load(bilder[hvilken]).convert_alpha()
    bilde = pg.transform.scale(bilde, (50, 50))
    xplas = random.randint(50, 750 - bilde.get_width())
    yplas = random.randint(50, 550 - bilde.get_height())
    klikkers.append({"bilde": bilde, "rect":pg.Rect(xplas, yplas, 140, 40) })    

        

bildenå = pg.image.load("Pygame/Klikker/bilder/Trump1.png").convert_alpha()
grønlandbilde = pg.image.load("Pygame/Klikker/bilder/grønnland.png").convert_alpha()
grønlandbilde = pg.transform.scale(grønlandbilde, (radius*2, radius*2))
pilbilde = pg.image.load("Pygame/Klikker/bilder/pil.png").convert_alpha()
pilbilde = pg.transform.scale(pilbilde, (80, 50))

pil_rect = pilbilde.get_rect(center=(50, 40))
grønland_rect = grønlandbilde.get_rect(center=(sirkelx, sirkely))

bilde = bildenå
bilde_sirkel = pg.transform.scale(bilde, (radius*2, radius*2))

score = FONT.render("1", True, "white")
rando = random.randint(0, 48)
tekst2 = qotessure[rando]
tekstgi2 = TEKST.render(tekst2, True, "white")

rando = random.randint(0, 10)
tekst3 = qotes[rando]
qotestekst = QOTETEKST.render(tekst3, True, "white")

tekstgi = TEKST.render("", True, "white")

mål_x = SW//2
mål_y = SH//2
angripere = []

def nyttangrep():
    bildeangrip = pg.image.load("Pygame/Klikker/bilder/Trump1.png").convert_alpha()
    bildeangrip = pg.transform.scale(bildeangrip, (40, 40))

    side = random.choice(["Top", "Bun", "Høyre", "Venstre"])

    if side == "Top":
        x, y = random.randint(0, SW), -40
    elif side == "Bun":
        x, y = random.randint(0, SW), SH + 40
    elif side == "Høyre":
        x, y = SW + 40, random.randint(0, SH)
    elif side == "Venstre":
        x, y = -40, random.randint(0, SH)
    
    rect = bildeangrip.get_rect(center=(x, y))

    dx = mål_x - x
    dy = mål_y - y
    lengde = (dx **2 + dy ** 2) ** 0.5

    fart = 2

    vx = dx / lengde * fart
    vy = dy / lengde * fart

    angripere.append({"img": bildeangrip, "rect": rect, "vx": vx, "vy": vy})

def oppdaterangrep():
    for a in angripere:
        a["rect"].x += a["vx"]
        a["rect"].y += a["vy"]
        skjerm.blit(a["img"], a["rect"])

while True:
    bilde_sirkel = pg.transform.scale(bilde, (radius*2, radius*2))
    skjerm.fill('black')
    if spiller1._klikkere > 0:
        tegnkliker(bildexstørelse, bildeystørelse)

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
                bilde = bildenå
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

            if byttbilde < spiller1._alltidkliks and bnumer != 11:
                bnumer += 1
                bildenå = pg.image.load(f"Pygame/Klikker/bilder/Trump{bnumer}.png").convert_alpha()
                bilde = bildenå
                bilde_sirkelnå = pg.transform.scale(bilde, (radius*2, radius*2))
                byttbilde += 500
                if byttbilde > 1500:
                    byttbilde *= 1.1

    nerf += 1
    if nerf >= 20:
        if spiller1._klikkere > 0:
            spiller1.autoklik()
            nerf = 0

    teller += 1
    if teller >= 20:
        
        if spiller1._klikkere > 0:
            bildexstørelse = 60
            bildeystørelse = 60
            spiller1.autoklik()
            teller = 0                  
    if teller >= 10 and teller <= 20:
        bildexstørelse = 50
        bildeystørelse = 50
        

                    

    skjerm.blit(bilde_sirkel, (sirkelx - radius, sirkely - radius))

    score = FONT.render(f"Antal kliks: {spiller1._kliks}", True, "white")
    grøncoin = TEKST.render(f"Antal Grønncoins: {spiller1._grønnlandcoins}", True, "white")

    skjerm.blit(tekstgi, (SW/2 - tekstgi.get_width()//2, 70))
    skjerm.blit(tekstgi2, (SW/4 - tekstgi2.get_width()//2, 300))     
    skjerm.blit(grøncoin, (SW/2 - grøncoin.get_width()//2, 50))
    skjerm.blit(qotestekst, (SW/2 - qotestekst.get_width()//2, 450))
    skjerm.blit(score, (SW/2 - score.get_width()//2, 10))

    
    tegnuppgrades()
    tegntekstantall()
    while dragrønnland:
        skjerm.fill('black')
        skjerm.blit(pilbilde, (50 - pilbilde.get_width()//2, 40 - pilbilde.get_height()//2))
        skjerm.blit(grønlandbilde, (sirkelx - radius, sirkely - radius))
        for hendelse in pg.event.get():
            if hendelse.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if hendelse.type == pg.MOUSEBUTTONDOWN:
                mus = hendelse.pos
                if pil_rect.collidepoint(hendelse.pos):
                    dragrønnland = False
                for a in angripere:
                    if a["rect"].collidepoint(mus):
                        angripere.remove(a)
                        spiller1._grønnlandcoins += 1
        for a in angripere:
            if a["rect"].colliderect(grønland_rect):
                angripere.remove(a)
                if spiller1._grønnlandcoins > 0:
                    spiller1._grønnlandcoins -= 1
                else:
                    dragrønnland = False


        grøncoin = FONT.render(f"Antal Grønncoins: {spiller1._grønnlandcoins}", True, "white")
        skjerm.blit(grøncoin, (SW/2 - grøncoin.get_width()//2, 20))

        if random.randint(1, 60) == 1:
            nyttangrep()
        
        oppdaterangrep()

        pg.display.update()
        klokke.tick(60)



    pg.display.update()
    klokke.tick(60)


