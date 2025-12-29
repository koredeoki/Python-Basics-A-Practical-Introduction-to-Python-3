def convert_cel_to_far(C):
    F = C * 9/5 + 32
    return F
num = convert_cel_to_far(-7.0)
print(num)

def convert_far_to_cel(F):
    C = (F- 32) * 5/9
    return C
num = convert_far_to_cel(24.7)
print(num)
