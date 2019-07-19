def zad4(*args):
    parzyste = 0
    nieparzyste = 0
    podzielne_3i7 = 0
    podzielne_2i3 = 0
    niepodz_3 = []
    for arg in args:
        if type(arg) is not int:
            raise TypeError("Dozwolone tylko cyfry")

        if arg % 2 == 0:
            parzyste += arg

        if arg % 2 != 0:
            nieparzyste += arg

        if arg % 3 == 0 and arg % 7 == 0:
            podzielne_3i7 += arg

        if arg % 2 == 0 and arg % 3 == 0:
            podzielne_2i3 += arg

        if arg % 3 != 0:
            niepodz_3 += [arg]
    return f"Suma liczb parzystych: {parzyste} \nSuma liczb nieparzystych: {nieparzyste}\nSuma liczb podzielnych prze 3 i 7: {podzielne_3i7} \nSuma liczb podzielna przez 2 i 3: {podzielne_2i3} \nCiąg bez liczb podzielnych przez 3: {niepodz_3}"
