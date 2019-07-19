from math import gcd


def zad5(*args):
    parzyste = 0
    nieparzyste = 0
    sortowane = []
    for arg in args:
        if type(arg) is not int:
            raise TypeError("Dozwolone tylko cyfry")

        if arg % 2 == 0:
            parzyste += arg

        if arg % 2 != 0:
            nieparzyste += arg

        sortowane += [arg]
        sortowane.sort()

    # gcd = 1

    # if args[0] % args[1] == 0:
    #     gcd = args[1]

    # for k in range(int(args[1] / 2), 0, -1):
    #     if args[0] % k == 0 and args[1] % k == 0:
    #         gcd = k
    #         break

    return f"Suma liczb parzystych: {parzyste} \nSuma liczb nieparzystych: {nieparzyste}\nPosortowany ciąg: {sortowane} \nNajwiększy wspólny dzielnik: {gcd(args[0], args[1])}"


print(zad5(88, 20, 44, 33, 10, 22))
