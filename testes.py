num = "01234567899876543210"
str = ""

print(num[1])
#print(pivo)

a = 0
lng=4
x1 = 0
x2 = 4
#str = str + num[a]
for a in range(4):
    i = 0   
    for i in range(x1, lng):
        pivo = num[i]
        str = str + pivo
    
    x1+=1
    lng+=1


print(str)


