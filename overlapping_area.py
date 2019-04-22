coords1 = input("Enter bottom left coordinates for rectangle 1: ").split(",")
coords2 = input("Enter top right coordinates for rectangle 1: ").split(",")
coords3 = input("Enter bottom left coordinates for rectangle 2: ").split(",")
coords4 = input("Enter top right coordinates for rectangle 2: ").split(",")


a, b = float(coords2[0]) - float(coords1[0]), float(coords2[1]) - float(coords1[1])
c, d = float(coords3[0]) - float(coords1[0]), float(coords3[1]) - float(coords1[1])
e, f = float(coords4[0]) - float(coords1[0]), float(coords4[1]) - float(coords1[1])


if d <= 0:
    height = abs(f)
if d > 0:
    height = abs(b) - abs(d)
if c <= 0:
    length = abs(e)
if c > 0:
    length = abs(a) - abs(c)
    
    
if c >= a or d >= b or e <= 0 or f <= 0:
    area = 0
else:
    area = length * height
    
    
print(area)
