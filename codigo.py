# input

print("===============================================================")
print("=======================calcular altura=========================")
print("===============================================================")

h=int(input("dijite el numero de la altura de la cual cae la pelota: "))

print("===============================================================")
print("===============================================================")

# processing

q = h / 5
i = 0

while i <= 5:
    h = h - (0.1*h)
    i = i + 1
    

# output

print("el quinto rebote de la pelota tendra una altura de: "+ str(h)+" metros")
print("===============================================================")