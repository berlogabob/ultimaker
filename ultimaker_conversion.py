import math

message = "Lenght of filament(in metrs)?\n"
p = math.pi
d = 2.85
r = d/2
round_up = math.ceil
listok = []

def start():
    h = float(input(message))
    h_mm = h * 1000.0
    v_mm = p * r**2 * h_mm
    v_sm = v_mm * 0.001
    v_round = round_up(v_sm)
    print(v_round)
    tap()

def tap():
    #input("hit any button")
    answer = int(input("press Zero to re enter or one to exit\n"))
    if answer == 0:
        start()
    else:
        return input("hit any key to exit\n")

    
start()

