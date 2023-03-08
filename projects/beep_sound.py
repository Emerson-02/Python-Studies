import winsound
frequencia = int(input("Digite uma frequencia em hertz: "))
duracao = int(input("Digite um tempo em milissegundos: "))
vezes = int(input("Quantas vezes voce quer repetir o som: "))
for i in range(0, vezes):
    winsound.Beep(frequencia, duracao)