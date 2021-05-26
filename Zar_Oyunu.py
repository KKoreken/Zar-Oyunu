import random

secim = 1
a = 1
skor = 0
puan = 0

pcEl = 0


def oynat():
    secim = int(input("Tek zar mı oynamak istersin? (1) çift zar mı? (2)"))
    if secim == 1:
        TekZar()
    else:
        CiftZar()


def bir():
    print("|  o  |")


def iki():
    print("|o   o|")


def uc():
    print("|  o  |")
    print("|  o  |")
    print("|  o  |")


def dort():
    print("|o   o|")
    print("|o   o|")


def bes():
    print("|o   o|")
    print("|  o  |")
    print("|o   o|")


def alti():
    print("|o   o|")
    print("|o   o|")
    print("|o   o|")


def skor_azalt():
    global skor
    skor -= 1
    print(skor)


def skor_artir():
    global skor
    skor += 1
    print(skor)


def TekZar():
    you = random.randint(1, 6)
    pc = random.randint(1, 6)
    print("Senin zarın {} geldi ".format(you))
    if you == 1:
        bir()
    elif you == 2:
        iki()
    elif you == 3:
        uc()
    elif you == 4:
        dort()
    elif you == 5:
        bes()
    elif you == 6:
        alti()
    print("Bilgisayar {} attı".format(pc))
    if pc == 1:
        bir()
    elif pc == 2:
        iki()
    elif pc == 3:
        uc()
    elif pc == 4:
        dort()
    elif pc == 5:
        bes()
    elif pc == 6:
        alti()
    if you < pc:
        print("Kaybettin!")
        skor_azalt()
    elif you == pc:
        print("Berabere! Skor değişmedi!")
        oynat()

    else:
        ("Kazandın!")
        skor_artir()


def CiftZar():
    pcEl = 0
    el = 0
    you = random.randint(1, 6)
    print("Senin zarın {} geldi ".format(you))
    if you == 1:
        bir()
    elif you == 2:
        iki()
    elif you == 3:
        uc()
    elif you == 4:
        dort()
    elif you == 5:
        bes()
    elif you == 6:
        alti()
    el += you
    you = random.randint(1, 6)
    print("Senin zarın {} geldi ".format(you))
    el += you
    if you == 1:
        bir()
    elif you == 2:
        iki()
    elif you == 3:
        uc()
    elif you == 4:
        dort()
    elif you == 5:
        bes()
    elif you == 6:
        alti()

    pc = random.randint(1, 6)
    pcEl = pcEl + pc
    print("Bilgisayar {} attı".format(pc))
    if pc == 1:
        bir()
    elif pc == 2:
        iki()
    elif pc == 3:
        uc()
    elif pc == 4:
        dort()
    elif pc == 5:
        bes()
    elif pc == 6:
        alti()
    pcEl += pc
    print("Bilgisayar {} attı".format(pc))
    if pc == 1:
        bir()
    elif pc == 2:
        iki()
    elif pc == 3:
        uc()
    elif pc == 4:
        dort()
    elif pc == 5:
        bes()
    elif pc == 6:
        alti()

    if you < pc:
        print("Kaybettin!")
        skor_azalt()
    elif you == pc:
        oynat()
    else:
        print("Kazandın!")
        skor_artir()


puan = int(input("Her raund 1 puan. Kaçta bitsin?"))
while a < 2:
    if puan == skor:
        break
    oynat()
