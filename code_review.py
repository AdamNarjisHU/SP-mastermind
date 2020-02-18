# import itertools
#
#
# def maak_alle_mogelijkheden(): #dit maakt ALLE permutaties
#     kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
#     mogelijkheden_lijst = []
#     for prod in itertools.product(kleuren_lijst, repeat=4):
#         mogelijkheden_lijst.append(prod)
#     return mogelijkheden_lijst
#
# def input_secret_key():
#     k1 = input('Geef je 1e kleur: ')
#     k2 = input('Geef je 2e kleur: ')
#     k3 = input('Geef je 3e kleur: ')
#     k4 = input('Geef je 4e kleur: ')
#     secret_key = (k1, k2, k3, k4)
#     return secret_key
#
#
# def ai_mastermind_gok(ai_gok, tip, ai_opties_lijst, ronde):
#     mogelijkheden_dict = {}
#     if ronde == 0:
#         print('AI voert in: {}'.format(ai_opties_lijst[0]))
#         return ai_opties_lijst[0], ai_opties_lijst
#     else:
#         nieuwe_pogingen = []
#         for optie in ai_opties_lijst:
#             hints = []
#             for i in range(0, 4):
#                 if (optie[i] == ai_gok[i]):
#                     hints.append('wit')
#                 elif (optie[i] in ai_gok[i]):
#                     hints.append('zwart')
#
#             if hints.count('wit') == 3:
#                 hints = ['wit', 'wit', 'wit']
#
#             mogelijkheden_dict[optie] = hints
#         print(len(mogelijkheden_dict.items()))
#         for k, v in mogelijkheden_dict.items():
#             if v == tip:
#                 nieuwe_pogingen.append(k)
#         print('AI voert in: {}'.format(nieuwe_pogingen[0]))
#         return nieuwe_pogingen[0], nieuwe_pogingen
#
#
# def play_game():
#     secret_key = input_secret_key()
#     print('secret key is: {}'.format(secret_key))
#     pogingen = 0
#     ai_mogelijkheden = maak_alle_mogelijkheden()
#     gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=None, tip=None, ai_opties_lijst=ai_mogelijkheden, ronde=aantal_guesses)
#     if gok == secret_key:
#         print('Game over! AI heeft gewonnen.')
#     else:
#         play = True
#         while play:
#             tips = []
#             pogingen += 1
#             for i in range(0, 4):
#                 if (gok[i] == secret_key[i]):
#                     tips.append('wit')
#                 elif (gok[i] in secret_key[i]):
#                     tips.append('zwart')
#
#             if tips.count('wit') == 3:
#                 tips = ['wit', 'wit', 'wit']
#
#             if pogingen <= 10:
#                 print('ronde {}'.format(pogingen))
#                 gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=gok, tip=tips, ai_opties_lijst=ai_mogelijkheden, ronde=pogingen)
#                 if gok == secret_key:
#                     print('Game over! AI heeft gewonnen!')
#                     play = False
#             else:
#                 print('Meer dan 10 gokken, AI heeft verloren')
#                 break
#
# play_game()
import itertools
from collections import Counter


def evaluate(guess, secret):
    matches = sum((Counter(secret) & Counter(guess)).values())
    bullseye = sum(c == g for c, g in zip(secret, guess))
    return bullseye, matches - bullseye


def knuth(secret):
    """Run Knuth's 5-guess algorithm on the given secret."""
    all_codes = maak_alle_mogelijkheden()
    assert (secret in all_codes)
    codes = all_codes
    key = lambda g: max(Counter(evaluate(g, c) for c in codes).values())
    # key is de kleurencombinatie die het meest voorkomt
    # for g in codes:
    #   for c in codes:
    #       count_dict = Counter(evaluate(g, c))
    # max(count_dict.values())
    # Counter geeft een dict terug met telling bijv: {[rood, rood, rood, geel]: 100}
    # Counter doet count maken van elke code. Code is combinatie van kleuren
    guess = ('rood', 'rood', 'oranje', 'oranje')
    while True:
        feedback = evaluate(guess, secret)
        print("Guess {}: feedback {}".format(guess, feedback))
        if guess == secret:
            break
        codes = [c for c in codes if evaluate(guess, c) == feedback]
        # def evalueer codes:
        #   for c in codes:
        #         if evaluate(guess, c) == feedback
        #             codes.append(c)
        #  return codes
        if len(codes) == 1:
            guess = codes[0]
        else:
            guess = min(all_codes, key=key)  # wat doet dit precies?


def check_hints(item1, item2):
    hints = []
    for i in range(0, 4):
        if (item1[i] == item2[i]):
            hints.append('wit')
        elif (item1[i] in item2[i]):
            hints.append('zwart')

    if hints.count('wit') == 3:
        hints = ['wit', 'wit', 'wit']

    return hints


def bereken_worst_case(pogingen_lijst):
    worst_cases = {}
    for item in pogingen_lijst:
        for i in range(0, len(pogingen_lijst)):
            worst_cases[tuple(evaluate(item, pogingen_lijst[i]))] += 1
    print(len(worst_cases))


def maak_alle_mogelijkheden():
    kleuren_lijst = ['rood', 'oranje', 'geel', 'groen', 'blauw', 'paars']
    mogelijkheden_lijst = []
    for prod in itertools.product(kleuren_lijst, repeat=4):
        mogelijkheden_lijst.append(prod)
    return mogelijkheden_lijst


def input_secret_key():
    k1 = input('Geef je 1e kleur: ')
    k2 = input('Geef je 2e kleur: ')
    k3 = input('Geef je 3e kleur: ')
    k4 = input('Geef je 4e kleur: ')

    secret_key = (k1.lower(), k2.lower(), k3.lower(), k4.lower())
    print(secret_key)
    return secret_key


def ai_mastermind_gok(ai_gok, tip, ai_opties_lijst, ronde):
    mogelijkheden_dict = {}
    eersteGok = ('rood', 'rood', 'oranje', 'geel')
    if ronde == 0:
        print('AI voert in: {}'.format(eersteGok))
        return eersteGok, ai_opties_lijst
    else:
        nieuwe_pogingen = []
        for optie in ai_opties_lijst:
            hints = check_hints(optie, ai_gok)
            mogelijkheden_dict[optie] = hints
        print(len(mogelijkheden_dict.items()))
        for k, v in mogelijkheden_dict.items():
            if v == tip:
                nieuwe_pogingen.append(k)
        bereken_worst_case(nieuwe_pogingen)
        print('AI voert in: {}'.format(nieuwe_pogingen[0]))

        return nieuwe_pogingen[0], nieuwe_pogingen


def play_game():
    secret_key = input_secret_key()
    print('secret key is: {}'.format(secret_key))
    aantal_guesses = 0
    ai_mogelijkheden = maak_alle_mogelijkheden()
    gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=None, tip=None, ai_opties_lijst=ai_mogelijkheden,
                                              ronde=aantal_guesses)

    if gok == secret_key:
        print('Game over! AI heeft gewonnen.')
    else:
        play = True
        while play:
            aantal_guesses += 1
            tips = check_hints(gok, secret_key)

            if aantal_guesses <= 10:
                print('ronde {}'.format(aantal_guesses))
                gok, ai_mogelijkheden = ai_mastermind_gok(ai_gok=gok, tip=tips, ai_opties_lijst=ai_mogelijkheden,
                                                          ronde=aantal_guesses)
                if gok == secret_key:
                    print('Game over! AI heeft gewonnen!')
                    play = False
            else:
                print('Meer dan 10 gokken, AI heeft verloren')
                break


# ----------------------------------------------------------------------------------------------------------------
knuth(input_secret_key())
