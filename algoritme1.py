import time
import random
from Feedback import pins


def heuristiek(ranglijst):
    set_ranglijst = set(ranglijst)
    length = len(set_ranglijst)
    ranglijst.append(length)
    return ranglijst


def make_list():
    list = []
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    this_code = [i, j, k, l]
                    updated_code = heuristiek(this_code)
                    list.append(updated_code)
    sorted_list = []
    for j in range(4, 0, -1):
        for x in list:
            if x[4] == j:
                sorted_list.append(x[0:4])
    return sorted_list


def eigen_algoritme():
    secret = input("Maak een geheime code aan met 4 getallen tussen de 1 en 6: ")
    secret_list = [int(i) for i in secret]  # input in list zetten
    for x in secret_list:
        if x > 6 or x < 1:
            secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
            print("Gebruik alleen getallen onder de 7.\n")
    if len(secret_list) != 4:
        secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
        print("Maak een 4 cijferige code aan.\n")
    print("Uw geheime code is", secret_list)
    time.sleep(1)
    print("De computer gaat nu beginnen met raden.")
    mogelijkheden = make_list()
    pogingen = 0
    gok = 0
    while gok != 1:
        pogingen += 1
        eerste_gok = mogelijkheden[0]
        eerste_feedback = pins(eerste_gok, secret_list)
        if eerste_feedback == (4, 0):  # feedback gebruiken om te checken of het is geraden
            gok = 1  # waarde van gok gebruiken om te bepalen of het is geraden
            break
        for i in mogelijkheden:
            verg_feedback = pins(i, eerste_gok)
            if verg_feedback != eerste_feedback:
                mogelijkheden.remove(i)
    time.sleep(1)
    print("Geraden in", pogingen, "poging(en).")
    time.sleep(1)
    if pogingen > 10:
        print("U heeft gewonnen!", eerste_gok)  # eerste_gok printen ter controle of de code echt is geraden
    if pogingen < 11:
        print("De computer heeft gewonnen :[", eerste_gok)  # eerste_gok printen ter controle of de code echt is geraden
