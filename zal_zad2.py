c = input("Podaj ciąg cyfr: ")
p = input("Podaj pozycję od której zaczniesz: ")
parzyste = 0
nieparzyste = 0
podzielne_3i7 = 0
podzielne_2i3 = 0
sortowane = []
podzielne_3 = []
if c:
    p = int(p)
    c = c.split(' ')
    #x = map(int, c.split(' '))
    for x in c[p::]:
        x = int(x)

        if x % 2 == 0:
            parzyste += x

        if x % 2 != 0:
            nieparzyste += x

        if x % 3 == 0 and x % 7 == 0:
            podzielne_3i7 += x

        if x % 2 == 0 and x % 3 == 0:
            podzielne_2i3 += x

        sortowane += [x]
        sortowane.sort()

        if x % 3 == 0:
            podzielne_3 += [x]
print(f"Suma liczb parzystych: {parzyste} \nSuma liczb nieparzystych: {nieparzyste}\nSuma liczb podzielnych prze 3 i 7: {podzielne_3i7} \nSuma liczb podzielna przez 2 i 3: {podzielne_2i3} \nPosortowany ciąg: {sortowane}\nCiąg liczb podzielnych przez 3: {podzielne_3}")
