from math import gcd


def zad6(procent, *args):
    parzyste = 0
    nieparzyste = 0
    na_procent = procent/100 + 1
    wieksza_liczba = []
    for arg in args:
        if type(arg) is not int:
            raise TypeError("Dozwolone tylko cyfry")

        if arg % 2 == 0:
            parzyste += arg

        if arg % 2 != 0:
            nieparzyste += arg

        if procent:
            wieksza_liczba += [na_procent*arg]

    return f"Suma liczb parzystych: {parzyste} \nSuma liczb nieparzystych: {nieparzyste}\nNajwiększy wspólny dzielnik: {gcd(args[0], args[1])} \nLiczby większe o podany procent: {wieksza_liczba}"


print(zad6(50, 2, 3, 6, 99, 10, 12))
