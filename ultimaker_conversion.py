import math

message = "Lenght of filament(in metrs)?"
p = math.pi
d = 2.85
r = d/2

h = float(input(message))
h_mm = h * 1000.0
v_mm = p * r**2 * h_mm
v_sm = v_mm * 0.001

print(v_sm)
