# Imports
import random
from Feedback import pins
from algoritme1 import eigen_algoritme

passw = []
while len(passw) < 4:
    passw.append(random.randint(1, 6))
def secret():
    gok = str(input("Raad 4 getallen tussen de 1 en 6: "))
    gok_list = [int(i) for i in gok]
    tel = 10
    while tel > 0:
        for a in gok_list:
            if a > 6 or a < 1:
                print("Alleen getallen tussen de 1 en 6, raad nogmaals")
                secret()
                break
        if len(gok_list) != 4:
            print("Raad 4 getallen, raad nogmaals")
            secret()
            break
        if gok_list == passw:
            print("GOED GERADEN!")
            break
        elif gok_list != passw:
            tel = tel - 1
            print(pins(gok_list, passw), "= (wit, zwart)\n{} pogingen over".format(tel))
            print(pins(gok_list, passw), "= (zwart, wit)")
            print(passw)
            secret()
            break


def menu():
    keuze = input(
        "Welkom bij Mastermind! Kies een gamemode. \n[a] Raad de geheime code \n[b] Wees de gamemaster \n[c] Spelregels\n")
    if keuze.lower() == "a":
        secret()
    elif keuze.lower() == "b":
        eigen_algoritme()
    elif keuze.lower() == "c":
        print("\n***Bij de gamemode -Raad de geheime code- wordt er een 4 cijferige code "
              "gegenereerd en is het aan u de taak om deze binnen 10 pogingen te raden."
              "\nLukt dat niet dan heeft de computer gewonnen.***"
              "\n\n***Bij de gamemode -Wees de gamemaster- mag uzelf een 4 cijferige code opmaken "
              "en raadt de computer d.m.v. algoritmes de geheime code."
              "\nLukt dat de computer niet in 10 pogingen dan bent u de winnaar!\n\n")
        menu()
menu()

