c = input("Podaj ciąg cyfr: ")
parzyste = 0
nieparzyste = 0
podzielne_3i7 = 0
podzielne_2i3 = 0
sortowane = []
podzielne_3 = []
if c:
    x = map(int, c.split(' '))
    for num in x:
        if num % 2 == 0:
            parzyste += num

        if num % 2 != 0:
            nieparzyste += num

        if num % 3 == 0 and num % 7 == 0:
            podzielne_3i7 += num

        if num % 2 == 0 and num % 3 == 0:
            podzielne_2i3 += num

        sortowane += [num]
        sortowane.sort()

        if num % 3 == 0:
            podzielne_3 += [num]
print(f"Suma liczb parzystych: {parzyste} \nSuma liczb nieparzystych: {nieparzyste}\nSuma liczb podzielnych prze 3 i 7: {podzielne_3i7} \nSuma liczb podzielna przez 2 i 3: {podzielne_2i3} \nPosortowany ciąg: {sortowane}\nCiąg liczb podzielnych przez 3: {podzielne_3}")
