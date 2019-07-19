def triangle(side1, side2, side3):
    circuit = 0
    p = 0
    area = 0
    if type(side1) == int or type(side1) == float and type(side2) == int or type(side2) == float and type(side3) == int or type(side3) == float:
        if side1+side2 > side3 and side2+side3 > side1 and side3+side1 > side2:
            circuit = side1+side2+side3
            p = circuit/2
            area = (p*(p-side1)*(p-side2)*(p-side3))**(1/2)
            return round(area, 2)
    else:
        raise ValueError("Side must be a number")


print(triangle(6, 8, 10))
