# a = 7
# b = 3
# print ("Test calculator")
# f = 34 + (2**3)
# print (f)
def rectangle(w, h):
    area = w * h
    return area

def triangle(w , h):
    return .5 * w * h

w = int(input("Weight = "))
h = int(input("Height = "))

print ("Area = ",rectangle(w, h))
print ("Triangle = ",triangle(w, h))
print ("Add this text one LINE")
