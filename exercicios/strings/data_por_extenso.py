a = input("Data de Nascimento: ")
a = a.split('/')
print(a[0])
print(a[1])
print(type(a[1]))
print(a[2])
dia = a[0]
mes = int(a[1])
ano = a[2]

if mes == 1:
    mes = 'Janeiro'
elif mes == 2:
    mes = 'Fevereiro'
elif mes == 3:
    mes = 'Março'
elif mes == 4:
    mes = 'Abril'
elif mes == 5:
    mes = 'Maio'
elif mes == 6:
    mes = 'Junho'
elif mes == 7:
    mes = 'Julho'
elif mes == 8:
    mes = 'Agosto'
elif mes == 9:
    mes = 'Setembro'
elif mes == 2:
    mes = 'Outubro'
elif mes == 2:
    mes = 'Novembro'
elif mes == 12:
    mes = 'Dezembro'
else:
    mes = False
    
print("Você nasceu em {} de {} de {}." .format(dia, mes, ano))