def pins(gok_list, passw):
    wit = wit_pin(gok_list, passw)
    zwart = zwart_pin(gok_list, passw)
    wit = wit - zwart
    return zwart, wit


def wit_pin(gok_list, passw):
    wit = 0
    wit_list = passw[:]
    for w in gok_list:
        if w in wit_list:
            wit_list.remove(w)
            wit += 1
    return wit


def zwart_pin(gok_list, passw):
    zwart = 0
    zwart_list = passw[:]
    teller = 0
    for z in gok_list:
        if z == zwart_list[teller]:
            zwart += 1
        teller += 1
    return zwart

# def pins(gok_list, passw):
#     wit = 0
#     zwart = 0
#     for i in range(0, 4):
#         for j in range(0, 4):
#             if i == j:
#                 if gok_list[i] == passw[j]:
#                     zwart += 1
#             else:
#                 if gok_list[i] == passw[j]:
#                     wit += 1
#     return zwart, wit