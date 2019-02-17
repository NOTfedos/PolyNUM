import polys


p = polys.Polynom('x+2')
s = polys.Polynom('x^2')
print(p)
print(s)
print(p * s)
print(polys.get_str('x^5 + x^6 + 2 + 1'))
