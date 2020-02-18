import time
import random
from Feedback import pins


def computer():
    password = []
    secret = input("Maak een geheime code aan met 4 getallen tussen de 1 en 6: ")
    secret_list = [int(i) for i in secret]
    for x in secret_list:
        if x > 6 or x < 1:
            secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
            print("Gebruik alleen getallen onder de 7.\n", secret)
    if len(secret_list) != 4:
        secret = input("Maak een geheime code aan met 4 getallen tussen de 0 en 6: ")
        print("Maak een 4 cijferige code aan.\n", secret)
    print("Uw geheime code is", secret_list)
    time.sleep(1)
    print("De computer gaat nu beginnen met raden.")
    mogelijkheden = [[i, j, k, l] for i in range(1, 7) for j in range(1, 7) for k in range(1, 7) for l in range(1, 7)]
    clean_list = mogelijkheden[:]
    pogingen = 0
    for i in mogelijkheden:
        pogingen += 1
        eerste_gok = random.choice(mogelijkheden)
        eerste_feedback = pins(eerste_gok, secret_list)
        verg_feedback = pins(i, eerste_gok)
        if verg_feedback != eerste_feedback:
            clean_list.remove(i)
            print(eerste_gok)
        else:
            time.sleep(1)
            print("Geraden in", pogingen, "poging(en).")
            time.sleep(1)
            break
    if pogingen > 10:
        print("U heeft gewonnen!", eerste_gok)
    if pogingen < 11:
        print("De computer heeft gewonnen :[", eerste_gok)
computer()